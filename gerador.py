import random
from pathlib import Path

current_file = Path(__file__).resolve()
current_dir = current_file.parent
print(current_dir)

def main():
    size = input("Insira o intervalo dos numeros ex: 1:100_000: ")
    type = input("Insira o metodo de ordenação: \n[1] - Crescente\n[2] - Decrescente\n[3] - Aleatorio\n")
    
    ranges = size.split(":")
    start = int(ranges[0])
    end = int(ranges[1])
    
    file_path = f"{current_dir}/casos_de_teste/{end}-size.txt"
    
    if(type == "3"):
        random_list = random.sample(range(start, end + 1), end)
        
        with open(file_path, "w") as f:
            for n in random_list:
                f.write(f"{n}\n")
            
        return
    
    
    list = range(start, end + 1) if type == "1" else range(end, start - 1, -1) 
    
    with open(file_path, "w") as f:
        for n in list:
            f.write(f"{n}\n")
        f = f.rstrip("\n")

if (__name__ == "__main__"):
    main()