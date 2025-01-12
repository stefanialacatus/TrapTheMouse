import sys
import os
def partial1():
    try:
        if len(sys.argv) != 4:
            raise ValueError("Numar gresit de argumente.")
        path1 = sys.argv[1]
        path2 = sys.argv[2]
        nr = int(sys.argv[3])
        try:
            with open(path1, 'r') as f1:
                content1 = f1.read()
        except Exception as e:
            raise Exception(f"Erare la citire '{path1}': {e}")
        try:
            with open(path2, 'r') as f2:
                content2 = f2.read()
        except Exception as e:
            raise Exception(f"Eroare la citire '{path2}': {e}")
        for i in range(0, len(content1), nr):
            if content1[i:i+nr] == content2[i:i+nr]:
                continue
            else:
                print(f"{i}|-|{content1[i:i+nr]}|-|{content2[i:i+nr]}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    partial1()

def partial2():
    try:
        if(len(sys.argv)!=4):
            raise ValueError("Numar gresit de argumente.")
        file_path = sys.argv[1]
        flag = sys.argv[2]
        sort = sys.argv[3]
        try:
            with open(file_path, 'r') as f:
                content = f.read()
        except Exception as e:
            raise Exception("Eroare la citire.")
        if flag == "char":
            dict = {}
            for i in range(0, len(content)):
                dict[content[i]] = dict.get(content[i], 0) + 1
            if sort == "true":
                dict = dict.items()
                dict = sorted(dict, key=lambda x: x[1], reverse=True)
            if sort == "false":
                dict = dict.items()
                dict = sorted(dict, key=lambda x: x[0], reverse=False)
            for key, value in dict:
                print(f"{key} {value}")
        if flag == "word":
            dict ={}
            words = content.split()
            for word in words:
                dict[word]=dict.get(word, 0)+1
            if sort == "true":
                dict=dict.items()
                dict=sorted(dict, key=lambda x:x[1], reverse=True)
            if sort == "false":
                dict=dict.items()
                dict=sorted(dict, key=lambda x:x[0], reverse=False)
            for key, value in dict:
                print(f"{key} {value}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    partial2()


def partial3():
    try:
        if(len(sys.argv)!=3):
            raise ValueError("Numar gresit de variabile.")
        dir = sys.argv[1]
        result = sys.argv[2]
        min=100
        max=0
        dict = {}
        for root, dirs, files in os.walk(dir):
            for file in files:
                file_name=file.split(".")
                if(len(file_name[0])>max):
                    max=len(file_name[0])
                    max_name=file_name[0]
                if(len(file_name[0])<min):
                    min=len(file_name[0])
                    min_name=file_name[0]
                ext = file.split(".")[-1] if "." in file else ""
                if ext:
                    dict[ext]=dict.get(ext, 0) + 1
        dict=dict.items()
        dict=sorted(dict, key=lambda x:x[1], reverse=True)
        try:
            with open(result, "w") as f:
                for key, value in dict:
                    write=f.write("\n")
                    write=f.write(f"{key}: {value}")
                    write=f.write("\n")
                write=f.write("\n")
                write=f.write(f"Longest file name: {max_name}")
                write=f.write("\n")
                write=f.write(f"Shortest file name: {min_name}")
                write=f.write("\n")
        except Exception as e:
            raise Exception(f"Nu se poate deschide/scrie in fisierul result: {e}")
    except Exception as e:
        raise Exception(f"Eroare: {e}")

if __name__ == "__main__":
    partial3()

import time
def partial4():
    try:
        if(len(sys.argv)!=2):
            raise ValueError("Numar gresit de argumente.")
        dir = sys.argv[1]
        if not os.path.isdir(dir):
            raise FileNotFoundError(f"Folderul {dir} nu exista.")
        file_info={}
        min=time.strftime("%Y-%M-%D", time.localtime(time.time()))
        for root, dirs, files in os.walk(dir):
            for file in files:
                ext=file.split(".")[-1] if "." in file else ""
                file_path=os.path.join(dir, file)
                file_stats=os.stat(file_path)
                last_date=file_stats.st_mtime
                date=time.strftime("%Y-%M-%D", time.localtime(last_date))
                file_info[file]={"FILE_NAME":file, "FILE_SIZE":file_stats.st_size, "FILE_TYPE":ext, "LAST_MODIFIED_DATE":date}
        for file_data in file_info.values():
            if(file_data["LAST_MODIFIED_DATE"]<min):
                min=file_data["LAST_MODIFIED_DATE"]
                min_file=file_data["FILE_NAME"]
        for key in file_info.values():
            print(f"{key}:")
            print()
            for key, value in file_info.items():
                print(f"{key}: {value}")
        print(f"The oldest file is: {min_file}")
    except Exception as e:
        raise Exception(f"Eroare: {e}")
    
if __name__ == "__main__":
    partial4()

            
        
