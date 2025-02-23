import subprocess
import os
import glob

print("✅ Starter hovedpipeline...")

# Opprett nødvendige mapper
os.makedirs("output", exist_ok=True)
os.makedirs("storage/raw_data", exist_ok=True)
os.makedirs("storage/filtered_data", exist_ok=True)
os.makedirs("storage/processed_data", exist_ok=True)

# Hent alle filer fra input-mappen
input_files = os.listdir("input")

# Tilbakestiller systemet og flytter filer tilbake
if not input_files:
    print("Ingen filer funnet i input-mappen.")
    input_files = os.listdir("storage/raw_data")
    subprocess.run(["python3", "modules/data_reset/pipeline.py"] + input_files, check=True)
    folder_path = "output"
    for file in glob.glob(f"{folder_path}/*"):  # Henter alle filer i mappen
        os.remove(file)  # Sletter hver fil

    exit(1)

# Flytt alle filer til raw_data/
print("✅ Initialiserer modul: ingestion")
subprocess.run(["python3", "modules/ingestion/pipeline.py"] + input_files, check=True)

# Pre-prosesserer filene 
raw_files = os.listdir("storage/raw_data")
print("✅ Initialiserer modul: preparation")
subprocess.run(["python3", "modules/preparation/pipeline.py"] + raw_files, check=True)

#TODO
# Fanger innholdet av filene 
#??? = os.listdir("storage/???")
#print("✅ Initialiserer modul: capture")
#subprocess.run(["python3", "modules/capture/pipeline.py"] + ???, check=True)

#TODO
# Klassifisering av filene 
#??? = os.listdir("storage/???")
#print("✅ Initialiserer modul: classification")
#subprocess.run(["python3", "modules/classification/pipeline.py"] + ???, check=True)

#TODO
# Data uttrekk av filene 
#??? = os.listdir("storage/???")
#print("✅ Initialiserer modul: extraction")
#subprocess.run(["python3", "modules/extraction/pipeline.py"] + ???, check=True)

#TODO
# Validering av uttrekt data
#??? = os.listdir("storage/???")
#print("✅ Initialiserer modul: validation")
#subprocess.run(["python3", "modules/validation/pipeline.py"] + ???, check=True)

# Beriker klassifiserte filer med uttrekt data
filtered_files = os.listdir("storage/filtered_data")
print("✅ Initialiserer modul: enrichment")
subprocess.run(["python3", "modules/enrichment/pipeline.py"] + filtered_files, check=True)

#TODO
# Generer innsikt av prosessert data
#??? = os.listdir("storage/???")
#print("✅ Initialiserer modul: insights")
#subprocess.run(["python3", "modules/insights/pipeline.py"] + ???, check=True)

# Flytter ferdigprosesserte filer til output/
processed_files = os.listdir("storage/processed_data")
print("✅ Initialiserer modul: curation")
subprocess.run(["python3", "modules/curation/pipeline.py"] + processed_files, check=True)

print("✅ Hovedpipeline fullført! Sjekk output-mappen.")