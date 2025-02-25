import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from components.data_capture import CaptureFileModule

#TODO

if len(sys.argv) < 2:
    print("❌ Ingen fil spesifisert.")
    sys.exit(1)

input_dir = "storage/filtered_data"
output_dir = "storage/captured_data"

if __name__ == "__main__":
    
    capture_module = CaptureFileModule()
    
    for file in sys.argv[1:]:  # Itererer over ALLE filene
        
        input_file = os.path.join(input_dir, file)
        content = CaptureFileModule.read_file(input_file)
        output_file_path = os.path.join(output_dir, "capturedData_"+file)
        CaptureFileModule.write_file(output_file_path, content)
        print(f"🔄 Datafangst av fil: {file}")
        
    print("✅ Modul capture: Fanget innholdet av filene ")