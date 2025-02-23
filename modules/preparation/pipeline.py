import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from modules.preparation.copy_file import CopyFileModule

INCLUDED_EXTENSIONS = [".txt", ".png"]  # Inkluderer spesifikke filtyper
MAX_FILE_SIZE_MB = 1  # Ekskluder filer større enn 1 MB

if len(sys.argv) < 2:
    print("❌ Ingen fil spesifisert.")
    sys.exit(1)

input_dir = "storage/raw_data"
output_dir = "storage/filtered_data"

if __name__ == "__main__":
    
    copy_module = CopyFileModule()
    
    for file in sys.argv[1:]:  # Itererer over ALLE filene
        input_file = os.path.join(input_dir, file)

        # 1️⃣ Filtrér basert på filtype
        if not any(file.endswith(ext) for ext in INCLUDED_EXTENSIONS):
            print(f"❌ Hopper over {file} (filtype ekskludert)")
            continue

        # 2️⃣ Filtrér basert på innhold i filen
        file_size_mb = os.path.getsize(input_file) / (1024 * 1024)
        if file_size_mb > MAX_FILE_SIZE_MB:
            print(f"❌ Hopper over {file} (for stor: {file_size_mb:.2f} MB)")
            continue
        
        copy_module.process(input_file, output_dir)

    
    print("✅ Modul preparation: Alle filer kopiert til temp-filtered/")