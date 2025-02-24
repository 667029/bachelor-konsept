from flask import Flask, render_template, request, redirect, url_for
import os
import subprocess
import platform
import glob

def get_python_command():
    # Oppdag hvilket OS programmet kjører på
    current_os = platform.system()
    
    # Sett python-kommando basert på hvilket OS det er
    if current_os == "Windows":
        return "python"   # som oftest python på Windows
    else:
        return "python3"  # som oftest python3 på Unix-baserte systemer
    
python_cmd = get_python_command()

app = Flask(__name__)
UPLOAD_FOLDER = "input"
ALLOWED_EXTENSIONS = {"txt", "csv", "json", "xml", "jpeg", "pdf"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Sjekk om filtypen er tillatt
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def upload_file():
    input_files = os.listdir("input")
   
    if not input_files:
        print("Ingen filer funnet i input-mappen.")
        input_files = os.listdir("storage/raw_data")
        subprocess.run([python_cmd, "modules/data_reset/pipeline.py"] + input_files, check=True)
        folder_path = "output"
        for file in glob.glob(f"{folder_path}/*"):  # Henter alle filer i mappen
            os.remove(file)  # Sletter hver fil

        

    if request.method == "POST":
        if "file" not in request.files:
            return "❌ Ingen fil valgt", 400

        file = request.files["file"]
        if file.filename == "":
            return "❌ Ingen fil valgt", 400

        if file and allowed_file(file.filename):
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)

            # 🟢 Kjør pipelinen etter opplasting
            subprocess.run([python_cmd, "main_pipeline.py"], check=True)

            return redirect(url_for("upload_success", filename=file.filename))

    return render_template("index.html")

#@app.route("/success/<filename>", methods=["GET", "POST"])
#def upload_success(filename):
#    return f"✅ Filen {filename} er lastet opp og behandlet!"

@app.route("/upload_success/<filename>")
def upload_success(filename):
    return render_template("upload_success.html", filename=filename)

@app.route("/back", methods=["POST"])
def back():
    # Kjør et annet script eller samme script på nytt i subprocess
    #subprocess.run([python_cmd, "some_other_script.py"], check=True)
    return redirect(url_for("upload_file"))

if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True, port=5000)