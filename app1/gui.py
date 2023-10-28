from modules import functions
import PySimpleGUI as sg

label = sg.Text("Type in a task:")
input_box = sg.InputText(tooltip="Enter Task", key="task")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.read_file(), key="Tasks", 
                        enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")

window = sg.Window("My Tasks-To-Do App", 
                    layout=[[label], [input_box, add_button], 
                    [list_box, edit_button]], 
                    font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['Tasks'])
    match event:
        case "Add":
            todos = functions.read_file()
            new_todo = values["task"] + "\n"
            todos.append(new_todo)
            functions.write_file(todos)
            window["Tasks"].update(values = todos)

        case "Edit":
            todo_to_edit = values['Tasks'][0]
            new_todo = values['task']

            todos = functions.read_file()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_file(todos)
            window["Tasks"].update(values = todos)

        case "Tasks":
            window["task"].update(value=values["Tasks"][0])

        case sg.WIN_CLOSED:
            break

window.close()