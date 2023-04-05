from tkinter import * 

master = Tk()

w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.set(100)
w.pack()

mainloop()