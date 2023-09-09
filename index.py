import tkinter as tk
from tkinter import messagebox

tasks = []

def submit_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Task added successfully!")
    else:
        messagebox.showwarning("Empty Field", "Please enter a task.")

def edit_task():
    selected_index = listbox.curselection()
    if selected_index:
        task = entry.get()
        if task:
            index = selected_index[0]
            tasks[index] = task
            listbox.delete(index)
            listbox.insert(index, task)
            entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Task updated successfully!")
        else:
            messagebox.showwarning("Empty Field", "Please enter a task.")
    else:
        messagebox.showwarning("No Task Selected", "Please select a task to edit.")

def delete_task():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        confirmed = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this task?")
        if confirmed:
            listbox.delete(index)
            del tasks[index]
            messagebox.showinfo("Success", "Task deleted successfully!")
    else:
        messagebox.showwarning("No Task Selected", "Please select a task to delete.")

def select_task(event):
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        task = tasks[index]
        entry.delete(0, tk.END)
        entry.insert(tk.END, task)
root = tk.Tk()
root.title("To-Do List")

heading_label = tk.Label(root, text="To-Do List", font=("Helvetica", 24, "bold"),bg="black", fg="red",width="30")
heading_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

listbox = tk.Listbox(frame, width="40",height=10,font=("Helvetica", 18, "bold"),border=4)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, font=("Helvetica", 14), border=4,width="30")
entry.pack(pady=10)

submit_btn = tk.Button(root, text="Add Task", command=submit_task,bg="pale green",width="30",font=("Helvetica", 14, "bold"))
submit_btn.pack(pady=5)

edit_btn = tk.Button(root, text="Edit Task", command=edit_task, bg="pale green",width="30",font=("Helvetica", 14, "bold"))
edit_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task, bg = "pALE GREEN",width="30",font=("Helvetica", 14, "bold"))
delete_btn.pack(pady=5)

listbox.bind("<<ListboxSelect>>", select_task)

root.mainloop()
