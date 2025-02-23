import os
import sys
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

#TODO

if len(sys.argv) < 2:
    print("❌ Ingen fil spesifisert.")
    sys.exit(1)

input_dir = ""
output_dir = ""

if __name__ == "__main__":
    

    for file in sys.argv[1:]:  # Itererer over ALLE filene
        input_file = os.path.join(input_dir, file)
        

    print("✅ Modul capture: Fanget innholdet av filene ")