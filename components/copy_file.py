import shutil
import os

class CopyFileModule:
    def process(self, input_file, output_dir):
        new_file = os.path.join(output_dir, os.path.basename(input_file))
        shutil.copy(input_file, new_file)
        print(f"🔄 Fil kopiert til: {new_file}")
        return new_file