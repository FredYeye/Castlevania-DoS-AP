import os

def patch(self, output_directory: str) -> None:
    filename = f"{self.multiworld.get_out_file_name_base(self.player)}.patch"
    with open(os.path.join(output_directory, filename), 'w') as f:
        f.write("test")
