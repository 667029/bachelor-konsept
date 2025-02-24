```
pip install -r requirements.txt
```

Starte server:
```
Mac:      python3 app.py
Windows:  python app.py
```

Starte/Kjøre gjennom terminal:
```
Mac:      python3 main_pipeline.py
Windows:  python main_pipeline.py
```
Serveren: http://localhost:5000/ || http://127.0.0.1:5000


```
root
├─ input/                   # Filene som skal prosesseres
│  ├─ input0.png
│  ├─ input1.png
│  ├─ input2.txt
│  ├─ input3.txt
│  ├─ input4.log
│  └─ input5.csv
├─ output/                  # Filene som er ferdig prosessert
├─ components/              # Funksjonelle komponenter som benyttes i modulene sin prosessering
│  ├─ rename_file.py
│  ├─ copy_file.py
│  ├─ data_capture.py
│  ├─ regex_extraction.py
│  └─ move_file.py
├─ modules/
│  ├─ __init__py
│  ├─ data_reset/           # Setter filene tilbake til utgangspunkt
│  │  ├─ __init__.py
│  │  └─ pipeline.py
│  ├─ ingestion/            # Flytt alle filer til raw_data/
│  │  ├─ __init__.py
│  │  └─ pipeline.py
│  ├─ preparation/          # Pre-prosesserer filene 
│  │  ├─ __init__.py
│  │  └─ pipeline.py
│  ├─ capture/              # Fanger innholdet av filene 
│  │  ├─ __init__.py
│  │  └─ pipeline.py
│  ├─ classification/       # Klassifisering av filene 
│  │  ├─ __init__.py
│  │  └─ pipeline.py
│  ├─ extraction/           # Data uttrekk av filene 
│  │  ├─ __init__.py
│  │  └─ pipeline.py
│  ├─ validation/           # Validering av uttrekt data
│  │  ├─ __init__.py
│  │  └─ pipeline.py
│  ├─ enrichment/           # Beriker klassifiserte filer med uttrekt data
│  │  ├─ __init__.py
│  │  └─ pipeline.py
│  ├─ insights/             # Generer innsikt av prosessert data
│  │  ├─ __init__.py
│  │  └─ pipeline.py
│  └─ curation/             # Flytter ferdigprosesserte filer til output/
│  │  ├─ __init__.py
│  │  └─ pipeline.py
├─ storage/                 # Lagringssone for data
│  ├─ raw_data/
│  ├─ captured_data/
│  ├─ filtered_data/
│  └─ processed_data/
├─ tests/                   # Tester til system
│  └─ test_pipeline.py
├─ templates/               # Interface til nettsiden
│  ├─ index.html
│  └─ upload_success.html
├─ main_pipeline.py         # Pipelineprogrammet
├─ app_pipeline.py          # Hovedprogrammet som starter server og interface
├─ README.md
└─ requirements.txt
```
