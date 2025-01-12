import sys
import os
def partial():
    try:
        if(len(sys.argv)<4):
            raise ValueError("Argumente insuficiente.")
        file_name=sys.argv[1]
        a=int(sys.argv[2])
        list=sys.argv[3:]
        if(os.path.isfile(file_name)):
            raise FileExistsError("Fisierul exista deja.")
        else:
            try:
                with open(file_name, 'x') as f:
                    f.write("")
            except Exception as e:
                raise Exception(f"Eroare: {e}")
        dict={}
        for num in list:
            n=int(num)
            dict[n]=n%a
        dict=dict.items()
        dict=sorted(dict, key=lambda x:x[1], reverse=True)
        for key, value in dict:
            print(f"{key}")
        try:
            with open(file_name, 'w') as f:
                for key, value in dict:
                    f.write(f"{key}")
        except Exception as e:
            raise Exception(f"eroare:{e}")

    except Exception as e:
        raise Exception(f"Eroare: {e}")
        
if __name__=="__main__":
    partial()