use std::{error::Error, ffi::CString};
use sysinfo::System;
use windows::{core::s, Win32::{
    Foundation::*,
    System::{Diagnostics::Debug::WriteProcessMemory,
    LibraryLoader::*,
    Memory::*,
    Threading::*,
}}};

fn main() {
    if let Err(e) = inject() {
        println!("{}", e);
    }
}

fn inject() -> Result<(), Box<dyn Error>> {
    // todo: maybe check if already injected?

    if let Some(pid) = get_pid() {
        unsafe {
            let process = OpenProcess(PROCESS_ALL_ACCESS, false, pid)?;

            let mut dll_path = std::env::current_exe()?;
            dll_path.set_file_name("cvdos_lib.dll");
            if !dll_path.exists() {
                println!("Cannot find cvdos_lib.dll");
                return Ok(());
            }

            let dll_path_str = dll_path.to_str().expect("Failed to convert dll string");
            let dll_path_c = CString::new(dll_path_str).unwrap();

            let remote_mem = VirtualAllocEx(
                process,
                None,
                dll_path_c.as_bytes_with_nul().len(),
                MEM_COMMIT | MEM_RESERVE,
                PAGE_READWRITE,
            );

            if remote_mem.is_null() {
                println!("VirtualAllocEx failed: {:?}", GetLastError());
                return Err(Box::new(windows::core::Error::from_thread()));
            }

            WriteProcessMemory(
                process,
                remote_mem,
                dll_path_c.as_bytes_with_nul().as_ptr() as _,
                dll_path_c.as_bytes_with_nul().len(),
                None,
            )?;

            let kernel32 = GetModuleHandleA(s!("kernel32.dll"))?;
            let load_lib = GetProcAddress(kernel32, s!("LoadLibraryA")).unwrap();

            let thread_handle = CreateRemoteThread(
                process,
                None,
                0,
                Some(std::mem::transmute(load_lib)),
                Some(remote_mem),
                0,
                None,
            )?;

            WaitForSingleObject(thread_handle, 800);
            CloseHandle(process)?;
        }

        Ok(())
    } else {
        return Err("game2_aslr_disabled.exe must be running".into())
    }
}

fn get_pid() -> Option<u32> {
    let mut sys = System::new_all();
    sys.refresh_all();

    for (pid, process) in sys.processes() {
        if process.name() == "game2_aslr_disabled.exe" {
            return Some(pid.as_u32())
        }
    }

    None
}
