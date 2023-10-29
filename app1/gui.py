from modules import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

# Sets up widgets for application, input box and buttons
sg.theme("Dark2")
clock = sg.Text("", key="clock")

label = sg.Text("Type in a task:")
input_box = sg.InputText(tooltip="Enter Task", key="task")
add_button = sg.Button(size=2, image_source="./app1/images/add.png", mouseover_colors="LightBlue2", tooltip="Add Task", key="Add")
list_box = sg.Listbox(values=functions.read_file(), key="Tasks", enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")
complete_button = sg.Button(image_source="./app1/images/complete.png", mouseover_colors="LightBlue2", tooltip="Complete Task", key="Complete")
exit_button = sg.Button("Exit")

# Creates application window and layout of buttons, each list is a different line in the application
layout = [[clock], [label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]]

window = sg.Window("My Tasks-To-Do App", layout=layout, font=("Helvetica", 20))

while True:
    # timeout is required to update time value in application, uses millisecond intervals
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.read_file()
            new_todo = values["task"] + "\n"
            todos.append(new_todo)
            functions.write_file(todos)
            window["Tasks"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['Tasks'][0]
                new_todo = values['task']

                todos = functions.read_file()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_file(todos)
                window["Tasks"].update(values=todos)
            # popup appears when user doesn't select a Task and tries to Edit
            except IndexError:
                sg.popup("Please select a Task first.", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values["Tasks"][0]
                todos = functions.read_file()
                todos.remove(todo_to_complete)
                functions.write_file(todos)
                window['Tasks'].update(values=todos)
                window['task'].update(value='')
            # popup appears when user doesn't select a Task and tries to Complete
            except IndexError:
                sg.popup("Please select a Task first.", font=("Helvetica", 20))

        case "Exit":
            break

        case "Tasks":
            window["task"].update(value=values["Tasks"][0])

        case sg.WIN_CLOSED:
            break

window.close()