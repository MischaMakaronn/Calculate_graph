import tkinter as tk

win = tk.Tk()
width = 600
height = 600
win.title('Моё первое графическое приложение')
win.geometry(f"{width}x{height}+500+200")

for i in range(8):
    for j in range(3):
        tk.Button(win,text=f'Hello {i} {j}').grid(row=i, column=j, stick = 'we')

# btn1 = tk.Button(win, text="helo1")
# btn2 = tk.Button(win, text="helo2")
# btn3 = tk.Button(win, text="helo3")
# btn4 = tk.Button(win, text="heloworld")
# btn5 = tk.Button(win, text="helo5")
# btn6 = tk.Button(win, text="helo6")
# btn7 = tk.Button(win, text="helo7")
# btn8 = tk.Button(win, text="helo8")

# btn1.grid(row=0, column=0)
# btn2.grid(row=0, column=1, stick='we')
# btn3.grid(row=1, column=0, stick='we')
# btn4.grid(row=1, column=1)
# btn5.grid(row=2, column=0)
# btn6.grid(row=2, column=1, stick='ew')
# btn7.grid(row=3, column=0, columnspan=2, stick='we')
# btn8.grid(row=0, column=2, rowspan=4,stick='ns')

win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=200)
win.grid_columnconfigure(2, minsize=200)



win.mainloop()