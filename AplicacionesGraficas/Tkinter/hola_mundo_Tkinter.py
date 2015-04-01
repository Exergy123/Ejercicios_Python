from Tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

label = Label(frame, text="Hola mundo")
c1 = Checkbutton(frame, text="Uno")
c2 = Checkbutton(frame, text="Dos")
entry = Entry(frame)
button = Button(frame, text="Aceptar")

label.pack()
c1.pack()
c2.pack()
entry.pack()
button.pack()

root.mainloop()
