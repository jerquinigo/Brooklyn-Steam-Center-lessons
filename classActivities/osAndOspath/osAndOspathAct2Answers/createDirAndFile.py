import os

userInput = input("enter name for project ")

os.mkdir("/Users/jonathan.e/Desktop/pythonActivityOS2/fileLocation")

os.chdir("/Users/jonathan.e/Desktop/pythonActivityOS2/fileLocation")

print(os.listdir(), "the dir")

with open("greetings.txt", "w+") as writeFile:
    writeFile.write(f"hello world, this is {userInput}\'s file'")

with open("greetings.txt", "r") as readFile:
    #fileRead = readFile.readlines()
    #print(fileRead)
    for line in readFile:
        print(line)
