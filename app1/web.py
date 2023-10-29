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

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a Task", placeholder="Add a new task", on_change=add_task, key="new_task")

print("Hello")

st.session_state