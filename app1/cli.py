# To-Do List Application
from modules import functions

while True:
    # Gets user input and strips space characters from it, capitalizes the first letter to match cases
    user_input = input("Add, Show, Edit, Complete or Exit: ").capitalize()
    user_input = user_input.strip()

    # User adds a task to the list
    if user_input.startswith("Add"):
        task = user_input[4:]

        to_dos = functions.read_file()

        to_dos.append(task + "\n")

        functions.write_file(to_dos)

    # Shows the current list of tasks
    elif user_input.startswith("Show"):

        to_dos = functions.read_file()

        # List comprehension, for loop to populate list variable new_todos
        new_todos = [item.strip('\n') for item in to_dos]

        # enumerate() goes through the list and separates index number and value
        for index, item in enumerate(new_todos):
            row = f"{index + 1} - {item}"
            print(row)
        print("Length of to do is", len(to_dos), "tasks.")

    # Allows user to edit task at index number
    elif user_input.startswith("Edit"):   
        try:
            number  = int(user_input[5:])

            to_dos = functions.read_file()
            
            print("Here are the current tasks", to_dos)

            new_to_do = input("Add new task: ")
            to_dos[number - 1] = new_to_do + '\n'
            print("New list of tasks", to_dos)

            functions.write_file(to_dos)
        except ValueError:
            print("ERROR INVALID COMMAND")
            continue
        except IndexError:
            print("There is no task with that number!")
            continue

    # Removes task if you have completed it
    elif user_input.startswith("Complete"):
        try:
            number = int(user_input[9:])

            to_dos = functions.read_file()

            index = number - 1
            to_do_removed = to_dos[index].strip('\n')
            to_dos.pop(index)

            functions.write_file(to_dos)

            print(f"Task {to_do_removed} was removed from the list.")
        except IndexError:
            print("There is no task with that number!")
            continue

    # Breaks while loop, exiting the program
    elif user_input.startswith("Exit"):
        break

    # Activates when error occurs, as a catch-all error case
    else:
        print("Error, unknown command!")

print("Exiting...")