import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from components.data_capture import CaptureFileModule
from components.regex_extraction import RegexExFileModule

#TODO

if len(sys.argv) < 2:
    print("❌ Ingen fil spesifisert.")
    sys.exit(1)

input_dir = "storage/filtered_data"
output_dir = "storage/captured_data"

if __name__ == "__main__":
    
    capture_module = CaptureFileModule()
    regex_module = RegexExFileModule()
    
    for file in sys.argv[1:]:  # Itererer over ALLE filene
        
        input_file = os.path.join(input_dir, file)
        content = CaptureFileModule.read_file(input_file)
        output_file_path = os.path.join(output_dir, "extraction_"+file)
        
        email = RegexExFileModule.extract_emails(content)
        formatted_emails = "\n".join([f"E-Mail: {email}" for email in email])
        
        date = RegexExFileModule.extract_dates(content)
        formatted_date = "\n".join([f"Date: {date}" for date in date])
        
        result = "EXTRACTION DATA\n" + formatted_emails + "\n"
        result += formatted_date
        
        CaptureFileModule.write_file(output_file_path, result)
        
        
        
        print(f"🔄 Uttrekt nøkkelord av fil: {file}")
    
    print("✅ Modul extraction: Uttrekk av data er gjennomført")