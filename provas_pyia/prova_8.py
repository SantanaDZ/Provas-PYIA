import os

for item in os.listdir():
    if os.path.isfile(item):
        print(f"Arquivo: {item}")
    elif os.path.isdir(item):
        print(f"Pasta: {item}")