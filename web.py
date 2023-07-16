import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state['todo']
    todos.append(todo_local + "\n")
    functions.write_todos(todos)


st.title("My Todo List")

for index, todo in enumerate(todos):
    st.checkbox(label=todo, key=index)

st.text_input(label="Enter a new todo", placeholder="Add a new todo...",
              on_change=add_todo, label_visibility=False,
              key="todo")
