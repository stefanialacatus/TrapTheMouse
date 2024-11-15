import sys
import os
def ex_1():
    try:
        if len(sys.argv) != 3:
            raise ValueError("Numar gresit de argumente.")
        dir = sys.argv[1]
        extension = sys.argv[2].lstrip(".")
        if not os.path.isdir(dir):
            raise FileNotFoundError(f"Folderul '{dir}' nu exista.")
        if not extension.isalnum():
            raise ValueError("Extensia unui fisier poate contine doar litere si cifre.")
        found_files = False
        for root, dirs, files in os.walk(dir):
            for file in files:
                ext= file.split(".")
                if ext[1] == extension:
                    found_files = True
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r') as f:
                            print()
                            print(f"Continutul fisierului {file_path}:\n")
                            print(f.read())
                            print("-" * 50)
                    except Exception as e:
                        print(f"Error reading file '{file_path}': {e}")
        if not found_files:
            print(f"Nu s-au gasit fisiere cu extensia '{extension}' in '{dir}'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ex_1()
            