import sys
import os
def ex_3():
    try:
        if(len(sys.argv) != 2):
            raise ValueError("Numar gresit de argumente.")
        dir = sys.argv[1]
        if not os.path.isdir(dir):
            raise FileNotFoundError(f"Folderul '{dir}' nu exista.")
        suma = 0
        for root, dirs, files in os.walk(dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    file_stats = os.stat(file_path)
                    suma += file_stats.st_size
                except PermissionError:
                    print(f"Permission denied: Cannot access '{file_path}'")
                except OSError as e:
                    print(f"Error with file '{file_path}': {e}")
        print(f"Suma dimensiunilor tuturor fisierelor din '{dir}': {suma} bytes")
        print(f"Suma dimensiunilor tuturor fisierelor din '{dir}': {suma / (1024*1024)} MB")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ex_3()