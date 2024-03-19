import os

print(os.listdir())

location = os.getcwd()
folder = os.path.dirname(location)

os.makedirs(f"{folder}//rep2")

for file in os.listdir() :
    if ".py" in file :
        print(file)