import tkinter as tk
tasks = []

ventana = tk.Tk()
ventana.title("To-Do List")
ventana.geometry("400x600")

def add_task():
    entry = tk.Entry(ventana)
    entry.pack()
    
    def save_task():
        new_task = entry.get()
        tasks.append(new_task)
        entry.delete(0, tk.END)
        
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
    
    save_task_button = tk.Button(ventana, text="Save Task", command=save_task)
    save_task_button.pack()

add_task_button = tk.Button(ventana, text="Add Task", command=add_task)
add_task_button.pack()


ventana.mainloop()