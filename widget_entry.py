import tkinter as tk
def get_entry():
       value = name.get()
       if value:
           print(value)
       else:
           print('Empty Entry')

def delete_entry():
    name.delete(0, tk.END)

def submit():
    print(name.get())
    print(password.get())
    delete_entry()
    password.delete(0, tk.END)


win = tk.Tk()
photo = tk.PhotoImage(file="fun.png")
width = 500
height = 600
win.title('Widget Entry')
win.geometry(f"{width}x{height}+500+200")

tk.Label(win, text='Имя').grid(row=0, column=0, stick ='w')
name = tk.Entry(win)
name.grid(row=0, column=1)

tk.Label(win, text='Password').grid(row=1, column=0, stick='w')
password = tk.Entry(win,show='*')
password.grid(row=1, column=1)


btn_1 = tk.Button(win, text='get', command=get_entry).grid(row = 2, column=0,stick='we') #Вывод текста в терминал
btn_2 = tk.Button(win, text='delete', command=delete_entry).grid(row = 2, column=1,stick='we') # Удаление текста
btn_3 = tk.Button(win, text='submit', command=submit).grid(row = 3, column=0,stick='we') # Вывод и удаление
btn_4 = tk.Button(win, text='insert', command=lambda: name.insert(1,'Hello'))\
    .grid(row = 2, column=2,stick='we') # Вставка текста в поле


win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)



win.mainloop()