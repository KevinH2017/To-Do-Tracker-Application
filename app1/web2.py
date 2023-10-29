# To-Do Web Application

import streamlit as st
from modules import functions

todos = functions.read_file()

def add_task():
    task = st.session_state["new_task"] + "\n"
    todos.append(task)
    functions.write_file(todos)

st.title("My Tasks-To-Do App")
st.subheader("This is my Tasks-To-Do app.")
st.write("This app is to increase your productivity.")

for index, task in enumerate(todos):
    checkbox = st.checkbox(str(index + 1) + ' - ' + str(task), key=task)
    if checkbox:
        todos.pop(index)
        functions.write_file(todos)
        del st.session_state[task]
        st.rerun()

st.text_input(label="Enter a Task", placeholder="Add a new task", on_change=add_task, key="new_task")
