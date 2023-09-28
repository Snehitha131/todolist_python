import tkinter as tk
from tkinter import messagebox

def add_todo():
    todo = entry.get()
    if todo:
        todo_list.insert(tk.END, todo)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_todo():
    try:
        selected_todo_index = todo_list.curselection()[0]
        todo_list.delete(selected_todo_index)
    except IndexError:
        pass

def clear_todos():
    todo_list.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=30, command=add_todo)
add_button.pack()
delete_button = tk.Button(root, text="Delete Task", width=30, command=delete_todo)
delete_button.pack()

todo_list = tk.Listbox(root, height=10, width=40)
todo_list.pack()

clear_button = tk.Button(root, text="Clear All Tasks", width=30, command=clear_todos)
clear_button.pack()

root.mainloop()
