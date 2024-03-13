import tkinter as tk

def say_hello():
    print("hello")

def add_label():
    label = tk.Label(win, text="new")
    label.pack()

def counter():
    global count
    count += 1
    btn4['text'] = f'Счётчик:{count}'

count = 0


win = tk.Tk()
photo = tk.PhotoImage(file="fun.png")
width = 500
height = 600
win.title('Моё первое графическое приложение')
win.geometry(f"{width}x{height}+500+200")
btn1 = tk.Button(win, text="Hello",
                 command=say_hello
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



win.mainloop()


