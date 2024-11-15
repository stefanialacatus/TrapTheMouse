import sys
import os
def ex_4():
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
        
        ext_count = {}
        
        for file in files:
            ext = file.split('.')[-1] if '.' in file else ''
            if ext:
                ext_count[ext] = ext_count.get(ext, 0) + 1
        if ext_count:
            print("Numarul de fisiere pe extensii:")
            for ext, count in ext_count.items():
                print(f".{ext}: {count} fisier(e)")
        else:
            print("0 fisiere cu extensii gasite.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ex_4()