import tkinter as tk
tasks = []


try:
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    pass


ventana = tk.Tk()
ventana.title("To-Do List")
ventana.geometry("400x600")


existing_tasks_label = tk.Label(ventana, text="My Tasks:")
existing_tasks_label.pack()

existing_tasks_listbox = tk.Listbox(ventana)
for task in tasks:
    existing_tasks_listbox.insert(tk.END, task)
existing_tasks_listbox.pack()


entry = tk.Entry(ventana, width=40)
entry.pack()


message_label = tk.Label(ventana, text="", fg="green")
message_label.pack()


def save_task_to_file():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def save_task():
    new_task = entry.get().strip()
    if new_task != "":
        tasks.append(new_task)
        entry.delete(0, tk.END)
        message_label.config(text="Task saved successfully!", fg="green")

        existing_tasks_listbox.insert(tk.END, new_task)
        save_task_to_file()
        
    else:
        message_label.config(text="Task cannot be empty!", fg="red" )


def delete_task():
    selected_index = existing_tasks_listbox.curselection()
    if not selected_index:
        message_label.config(text="Please select a task to delete!", fg="red")
    else:
        index = selected_index[0]
        del tasks[index]
        existing_tasks_listbox.delete(index)
        save_task_to_file()
        message_label.config(text="Task deleted successfully!", fg="green")


save_task_button = tk.Button(ventana, text="Save Task", command=save_task)
save_task_button.pack()


del_task_button = tk.Button(ventana, text="Delete Task", command= delete_task)
del_task_button.pack()


ventana.mainloop()