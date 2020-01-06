## OS and OS.path activity
___

1. sales employees regularly use the file path on the network access storage server. We want to check the last time a file from the path was accessed in unix time. Which funtions should be used?

* C) os.path.getctime()



2. The company recently connected to a server through telnet and we want to find out the operating system so we know what time of commads to use for it. We only know that python3 was recently installed on it. Which would be the best option to find out the current os of the server?

* D) os.name


3. We are going to give the sales team access to important documents, but we only want them to have read access. Only managers will retain the read write ability. Which method would work best for this scenario?

* A) os.chmod()


4. A software engineer on your team deleted crucial files on his local system. Your job is to check if some paths still exists before restoring from backup. What would be the best function to use for this scenario?

* A) os.path.exists()



5. We have a memory leak on one of the processes running on the servers and we cant access the machine with a GUI interface. One of the engineers had there ssh sessions open and can still communicate with the server. We have the current process id of the program. What would be the best function to use to stop the current program from continuing to run on the server?

* A) os.kill()


6. the new intern is learning the companies file structure, The boss wants a program to print current working directory every time the directory has been changed. What is the best function to use for thier script?

* A) os.getcwd()



