from modules import functions
import PySimpleGUI as sg

label = sg.Text("Type in a task:")
input_box = sg.InputText(tooltip="Enter Task", key="task")
add_button = sg.Button("Add")

window = sg.Window("My Tasks-To-Do App", 
                    layout=[[label], [input_box, add_button]], 
                    font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.read_file()
            new_todo = values["task"] + "\n"
            todos.append(new_todo)
            functions.write_file(todos)

        case sg.WIN_CLOSED:
            break

window.close()