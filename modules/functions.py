def read_file(filepath="./files/todos-2.txt"):
    """ Read a text file and return a list of tasks """
    with open(filepath, "r") as file_local:
        to_dos_local = file_local.readlines()
    return to_dos_local
    
def write_file(todos_arg, filepath="./files/todos-2.txt"):
    """ Writes tasks to the text file """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

# Only executes the code below if functions.py is ran directly
if __name__ == "__main__":
    print("Hello from functions.py")
    print(read_file())