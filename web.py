import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state['todo']
    todos.append(todo_local + "\n")
    functions.write_todos(todos)


st.title("My Todo List")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(label=todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a new todo", placeholder="Add a new todo...",
              on_change=add_todo, label_visibility='hidden',
              key="todo")
