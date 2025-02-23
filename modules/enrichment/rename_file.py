import os

class RenameFileModule:
    def process(self, input_file, output_dir, new_name):
        if not os.path.exists(input_file):
            print(f"❌ Fil ikke funnet: {input_file}")
            return None

        new_file_path = os.path.join(output_dir, new_name)

        try:
            os.rename(input_file, new_file_path)
            print(f"🔄 Filen ble omdøpt til: {new_file_path}")
            return new_file_path
        except Exception as e:
            print(f"❌ Feil ved omdøping av {input_file}: {e}")
            return None