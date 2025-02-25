import os

class CaptureFileModule:
    def read_file(file_path, encoding='utf-8'):
        """
        Leser innholdet i en fil og returnerer det som en streng.
        """
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except Exception as e:
            raise Exception(f"Kunne ikke lese filen {file_path}: {e}")

    def write_file(file_path, content, encoding='utf-8'):
        """
        Skriver innholdet til en fil.
        """
        try:
            with open(file_path, 'w', encoding=encoding) as f:
                f.write(content)
        except Exception as e:
            raise Exception(f"Kunne ikke skrive til filen {file_path}: {e}")