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

# 1️⃣ Flytt alle filer til raw_data/
print("✅ Initialiserer modul: Ingestion")
subprocess.run(["python3", "modules/ingestion/pipeline.py"] + input_files, check=True)

# 2️⃣ Pre-prosesserer filene 
raw_files = os.listdir("storage/raw_data")
print("✅ Initialiserer modul: preparation")
subprocess.run(["python3", "modules/preparation/pipeline.py"] + raw_files, check=True)

# 3️⃣ Beriker klassifiserte filer
filtered_files = os.listdir("storage/filtered_data")
print("✅ Initialiserer modul: Enrichment")
subprocess.run(["python3", "modules/enrichment/pipeline.py"] + filtered_files, check=True)

# 4️⃣ Flytter ferdigprosesserte filer til output/
processed_files = os.listdir("storage/processed_data")
print("✅ Initialiserer modul: Curation")
subprocess.run(["python3", "modules/curation/pipeline.py"] + processed_files, check=True)

print("✅ Hovedpipeline fullført! Sjekk output-mappen.")