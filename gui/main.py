import tkinter as tk
from settings import *
from pics import *

print("hello world")

root =tk.Tk()

#photo database
pencil = tk.PhotoImage(file = ".\img\photo1.png")

# Resizing image to fit on button
pencil = pencil.subsample(3, 3)


canvas= tk.Canvas(root, height= HEIGHT,width= WIDTH)
canvas.pack()

frame = tk.Frame(root, bg=BG_COLOUR)
frame.place(relx=0.5, rely=0,relwidth=1,relheight=1, anchor='n')

#buttons
pic_learn_button = tk.Button(frame, text ="pic", bg="orange", fg="white",image=pencil,border=0)
pic_learn_button.place(relx=0.5,rely=0.3,relwidth=0.2,relheight=0.1,anchor='n')

text_learn_button = tk.Button(frame, text ="ABC", bg="orange", fg="white")
text_learn_button.place(relx=0.5,rely=0.6,relwidth=0.2,relheight=0.1,anchor='n')

label = tk.Label(frame, text= "TANCOS", bg= BUTTON_COLOUR)
label.place(relx=0.5,rely=0.1,relwidth=0.2,relheight=0.1,anchor='n')

#drop down

variable = tk.StringVar(root)
variable.set("one") # default value

drop1= tk.OptionMenu(root, variable, "one", "two", "three")
drop1.config(bg='orange')
drop1["menu"].config(bg="orange")
drop1.place(relx=0.1,rely=0.8,width=100,height=100,anchor='n')

drop2= tk.OptionMenu(root, variable, "one", "two", "three",)
drop2.place(relx=0.9,rely=0.8,width=100,height=100,anchor='n')


root.mainloop()