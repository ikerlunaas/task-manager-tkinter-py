import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
app = tk.Tk()
app.title("Task Manager")

# Task List
tasks = []

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")


# Function to edit a task
def edit_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        selected_task = selected_task[0]
        edited_task = task_entry.get()
        if edited_task:
            tasks[selected_task] = edited_task
            update_task_list()
            task_entry.delete(0, "end")
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to delete task
def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        selected_task = selected_task[0]
        tasks.pop(selected_task)
        update_task_list()


# Function to update the task list

def update_task_list():
    task_listbox.delete(0, "end")
    for task in tasks:
        task_listbox.insert("end", task)

# Task Entry Field
task_entry = tk.Entry(app, width=40)
task_entry.pack(pady=10)

# Add button
add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack()

# Edit Button
edit_button = tk.Button(app, text="Edit Task", command=edit_task)
edit_button.pack()

# Delete button
delete_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_button.pack()

# Task List
task_listbox = tk.Listbox(app, selectmode=tk.SINGLE, width=40)
task_listbox.pack(pady=10)

# Initialize the task list
update_task_list()

app.mainloop()
