import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END,task)
        entry.delete(0,tk.END)
    else:
        messagebox.showwarning("пустое поле",'введите задачу')
def del_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Ничего не выбрано", "Пожалуйста, выберите задачу для удаления")
window = tk.Tk()
window.title('дела')

frame_task = tk.Frame(window)
frame_task.pack()
listbox =tk.Listbox(frame_task,height=10,width=50)
listbox.pack(side=tk.LEFT)
scrollbar = tk.Scrollbar(frame_task)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
entry = tk.Entry(window,width=50)
entry.pack()
button_add = tk.Button(window,text="добавить дело",width=50,command=add_task)
button_add.pack()
button_delete = tk.Button(window,text="удалить дело",width=50,command=del_task)
button_delete.pack()
window.mainloop()