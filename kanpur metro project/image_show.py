from tkinter import*
from PIL import Image,ImageTk
nayan=Tk()
nayan.geometry("1000x1000")
title=Label(text="My name is nayan , This is my first GUI")
#for png images--
# photo=PhotoImage(file="nayan.jpeg")
#for jpg images-
image=Image.open("nayan.jpeg")
photo=ImageTk.PhotoImage(image)
pic=Label(image=photo)
title.pack()
pic.pack()
nayan.mainloop()