import tkinter as tk
from random import random


def say_hello():
    print("hello") #Вывод текста в терминал

def add_label():
    label = tk.Label(win, text="new") #Вывод текста в окне
    label.pack()

def counter():
    global count
    count += 1
    btn4['text'] = f'Счётчик:{count}' #Счётчик




count = 0

win = tk.Tk()
photo = tk.PhotoImage(file="fun.png")
width = 500
height = 600
win.title('Моё первое графическое приложение')
win.geometry(f"{width}x{height}+500+200")
win.config(bg='#DB9FF9')
win.minsize(300,400)
win.maxsize(800,900)
win.iconphoto(False,photo)
win.resizable(True, True)
label_1 = tk.Label(win, text="""Hello 
world!""",
                   bg='green',
                   fg ='white',
                   font=('Arial', 15, 'bold'),
                   padx=30,
                   pady=30,
                   width=20,
                   height=10,

                   relief=tk.RAISED,
                   bd=10,
                   justify=tk.RIGHT
                   )


btn1 = tk.Button(win, text="Hello",
                 command=say_hello,

                 )

btn2 = tk.Button(win, text="World",
                 command=add_label
                 )

btn3 = tk.Button(win, text="Lambda function",
                 command=lambda: tk.Label(win, text="new lambda").pack()
                 )

btn4 = tk.Button(win, text=f'Счётчик:{count}',
                 command=counter,
                 activebackground="blue",
                 bg="darkred",
                 state=tk.NORMAL
                 )

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
label_1.pack()



win.mainloop()
