import subprocess
import os
import glob
import platform

def get_python_command():
    # Oppdag hvilket OS programmet kjører på
    current_os = platform.system()
    
    # Sett python-kommando basert på hvilket OS det er
    if current_os == "Windows":
        return "python"   # som oftest python på Windows
    else:
        return "python3"  # som oftest python3 på Unix-baserte systemer
    
python_cmd = get_python_command()

print("✅ Starter hovedpipeline...")

# Opprett nødvendige mapper
os.makedirs("output", exist_ok=True)
os.makedirs("storage/raw_data", exist_ok=True)
os.makedirs("storage/filtered_data", exist_ok=True)
os.makedirs("storage/processed_data", exist_ok=True)
os.makedirs("storage/captured_data", exist_ok=True)

# Hent alle filer fra input-mappen
input_files = os.listdir("input")

# Tilbakestiller systemet og flytter filer tilbake
if not input_files:
    print("Ingen filer funnet i input-mappen.")
    input_files = os.listdir("storage/raw_data")
    subprocess.run([python_cmd, "modules/data_reset/pipeline.py"] + input_files, check=True)
    folder_path = "output"
    for file in glob.glob(f"{folder_path}/*"):  # Henter alle filer i mappen
        os.remove(file)  # Sletter hver fil
    
    folder_path = "storage/captured_data"
    for file in glob.glob(f"{folder_path}/*"):  # Henter alle filer i mappen
        os.remove(file)  # Sletter hver fil

    exit(1)

# Flytt alle filer til raw_data/
print("✅ Initialiserer modul: ingestion")
subprocess.run([python_cmd, "modules/ingestion/pipeline.py"] + input_files, check=True)

# Pre-prosesserer filene 
raw_files = os.listdir("storage/raw_data")
print("✅ Initialiserer modul: preparation")
subprocess.run([python_cmd, "modules/preparation/pipeline.py"] + raw_files, check=True)

# Fanger innholdet av filene 
filtered_files = os.listdir("storage/filtered_data")
print("✅ Initialiserer modul: capture")
subprocess.run([python_cmd, "modules/capture/pipeline.py"] + filtered_files, check=True)

# Klassifisering av filene 
filtered_files = os.listdir("storage/filtered_data")
print("✅ Initialiserer modul: classification")
subprocess.run([python_cmd, "modules/classification/pipeline.py"] + filtered_files, check=True)

# Data uttrekk av filene 
filtered_files = os.listdir("storage/filtered_data")
print("✅ Initialiserer modul: extraction")
subprocess.run([python_cmd, "modules/extraction/pipeline.py"] + filtered_files, check=True)

# Validering av uttrekt data
filtered_files = os.listdir("storage/filtered_data")
print("✅ Initialiserer modul: validation")
subprocess.run([python_cmd, "modules/validation/pipeline.py"] + filtered_files, check=True)

# Beriker klassifiserte filer med uttrekt data
filtered_files = os.listdir("storage/filtered_data")
print("✅ Initialiserer modul: enrichment")
subprocess.run([python_cmd, "modules/enrichment/pipeline.py"] + filtered_files, check=True)

# Generer innsikt av prosessert data
processed_files = os.listdir("storage/processed_data")
print("✅ Initialiserer modul: insights")
subprocess.run([python_cmd, "modules/insights/pipeline.py"] + processed_files, check=True)

# Flytter ferdigprosesserte filer til output/
processed_files = os.listdir("storage/processed_data")
print("✅ Initialiserer modul: curation")
subprocess.run([python_cmd, "modules/curation/pipeline.py"] + processed_files, check=True)

print("✅ Hovedpipeline fullført! Sjekk output-mappen.")