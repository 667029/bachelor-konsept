import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from modules.curation.move_file import MoveFileModule

if len(sys.argv) < 2:
    print("❌ Ingen fil spesifisert.")
    sys.exit(1)

input_dir = "storage/processed_data"
output_dir = "output"

if __name__ == "__main__":
    
    move_module = MoveFileModule()

    for file in sys.argv[1:]:  # Itererer over ALLE filene
        input_file = os.path.join(input_dir, file)
        move_module.process(input_file, output_dir)

    print("✅ Modul curation: Alle prosesserte filer flyttet til output/")