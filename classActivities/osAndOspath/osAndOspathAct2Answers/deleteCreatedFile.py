import os

if os.path.exists("/Users/jonathan.e/Desktop/pythonActivityOS2/fileLocation"):
    os.chdir("/Users/jonathan.e/Desktop/pythonActivityOS2/fileLocation")
    os.unlink("greetings.txt")
    os.removedirs("/Users/jonathan.e/Desktop/pythonActivityOS2/fileLocation")
else:
    print("current path does not exist. It has either been deleted or did not exist")