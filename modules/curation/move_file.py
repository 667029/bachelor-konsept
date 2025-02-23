import shutil
import os

class MoveFileModule:
    def process(self, input_file, output_dir):
        new_file = os.path.join(output_dir, os.path.basename(input_file))
        shutil.move(input_file, new_file)
        print(f"🔄 Flyttet fil til: {new_file}")
        return new_file