from pathlib import Path

def check():
    catalog = Path(".")
#Yo i know this code is dogshit but i was writing it like 1.40AM and after gym so im pretty tired. Alright?
    for thing in catalog: 
        if thing.is_file():
            print("yeah it is file")
            if thing.suffix == ".png":
                print(f"Yeah its .png file\nName: {thing.name}")
            elif thing.suffix == ".txt":
                print(f"Yeah its .txt file *meows gently\nName: {thing.name}")
    print(f"The file is {thing.name}")

check()
        
