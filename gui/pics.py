from tkinter import *

imagelist = {
  'pencil': [r'C:\Users\marco\Documents\Python\SUMO_Hack\gui\img\pencil1.png', None],
}

def get(name):
  if name in imagelist:
    if imagelist[name][1] is None:
      print('loading image:', name)
      imagelist[name][1] = PhotoImage(file=imagelist[name][0])
    return imagelist[name][1]
  return None