import sys
import os
def ex_2():
    try:
        if len(sys.argv) != 2:
            raise ValueError("Numar gresit de argumente.")
        dir = sys.argv[1]
        if not os.path.isdir(dir):
            raise FileNotFoundError(f"Folderul '{dir}' nu exista.")
        files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
        if not files:
            print(f"Nu s-au gasit fisiere in '{dir}'.")
            return
        files.sort()
        for i, file in enumerate(files, start=1):
            original_path = os.path.join(dir, file)
            new_name = f"file{i}{os.path.splitext(file)[1]}"
            new_path = os.path.join(dir, new_name)

            try:
                os.rename(original_path, new_path)
                print(f"Am redenumit '{file}' in '{new_name}'.")
            except OSError as e:
                print(f"Nu s-a putut redenumi '{file}': {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ex_2()