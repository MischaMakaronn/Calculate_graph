import tkinter as tk

win = tk.Tk()
width = 500
height = 600
win.title('Моё первое графическое приложение')
win.geometry(f"{width}x{height}+500+200")

label_1 = tk.Label(win, text="""Hello 
world!""",
                   bg='green',
                   fg ='white',
                   font=('Arial', 15, 'bold'),
                   padx=30,
                   pady=30,
                   width=20,
                   height=10,
                   anchor='nw',
                   relief=tk.RAISED,
                   bd=10,
                   justify=tk.RIGHT
                   )
label_1.pack()






win.mainloop()

