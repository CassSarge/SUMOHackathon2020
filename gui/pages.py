#Source: CJ van der Smissen
#Source: https://github.com/introtocomputerscience/TKinterExample
from tkinter import *
from settings import *
from pics import *
from random import randint
import string
import sys
import os

#flags
global pic_learn

#os specific filepath separator (e.g. \ or /)
s = os.sep
#teaching dictionary

teachingDic={}
for letter in list(string.ascii_uppercase):
    teachingDic[letter]= ["." + s + "img" + s + "text"+ s + "text_"+letter+".png","." + s + "img" + s + "signs"+ s +"sign_"+letter+".png"]

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        #Setup Frame
        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.resizable(width=False, height=False)


        self.frames = {}

        for F in (StartPage, Modules, Profile,learn,demo1,demo2):
            if F==learn:
                for key in teachingDic:
                    frame = learn(self.container, self, key, teachingDic[key][0], teachingDic[key][1])
            else:
                frame = F(self.container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame(StartPage)

    def show_frame(self, context):

        frame = self.frames[context]
        frame.tkraise()

    def show_learn_frame(self, context,teachingItem):

        key=teachingItem
        frame= learn(self.container, self, key, teachingDic[key][0], teachingDic[key][1])
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # photo database
        self.pic2sign = PhotoImage(file=pic_2_sign_img)
        self.text2sign = PhotoImage(file=text_2_sign_img)
        self.logo = PhotoImage(file=logo_img)
        self.steve = PhotoImage(file=steve_img)
        self.logoText = PhotoImage(file=logo_text_img)
        self.signButton = PhotoImage(file=signButton)
        self.textButton = PhotoImage(file=textButton)

        # Resizing image to fit on button
        self.pic2sign = self.pic2sign.subsample(2, 2)
        self.text2sign = self.text2sign.subsample(2, 2)
        self.logo = self.logo.subsample(7, 7)
        self.steve = self.steve.subsample(3, 3)
        self.logoText= self.logoText.subsample(3, 3)
        self.signButton = self.signButton.subsample(3, 3)
        self.textButton= self.textButton.subsample(3, 3)


        canvas = Canvas(self, height=HEIGHT, width=WIDTH, bg=BG_COLOUR)
        canvas.pack()

        self.back=Frame(self, bg=BG_COLOUR)
        self.back.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')
        self.frame = Frame(self, bg=WHITE)
        self.frame.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.8, anchor='n')
        self.header=Frame(self, bg=BLUE)
        self.header.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor='n')

        # buttons
        pic_learn_button = Button(self.frame, text="pic",bg="white", fg="white", image=self.pic2sign, border=0,command=lambda:controller.show_frame(demo1))
        pic_learn_button.place(relx=0.05, rely=0.2, width=200, height=200, anchor='nw')

        text_learn_button = Button(self.frame, text="ABC", bg="white", fg="white",image=self.text2sign,border=0,command=lambda:controller.show_learn_frame(learn,chr(randint(65,90))))
        text_learn_button.place(relx=0.95, rely=0.2, width=200, height=200, anchor='ne')

        #images
        logoLabel= Label(self.header, text="TANCOS", border=0, image= self.logo)
        logoLabel.place(x=0,y=0)
        logoLabel= Label(self.header, text="TANCOS", border=0, image= self.logoText)
        logoLabel.place(relx=0.5,rely=0,anchor='n')
        steveLabel= Label(self.frame, text="steve", border=0, image= self.steve)
        steveLabel.place(relx=0.5,rely=0.4,anchor='n')
        dropLabel= Label(self.frame, text="TANCOS", border=0, image= self.textButton)
        dropLabel.place(relx=0.2,rely=0.75,anchor='n')
        dropLabel= Label(self.frame, text="TANCOS", border=0, image= self.signButton)
        dropLabel.place(relx=0.8,rely=0.75,anchor='n')



        #label = Label(self.frame, text="TANCOS", bg=BUTTON_COLOUR)
        #label.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.1, anchor='n')

        # drop down
        '''
        variable = StringVar(self)
        variable.set("one")  # default value

        drop1 = OptionMenu(self, variable, "Auslan", "ASL", "BSL")
        drop1.config(bg='orange')
        drop1["menu"].config(bg="orange")
        drop1.place(relx=0.1, rely=0.8, width=100, height=100, anchor='n')

        drop2 = OptionMenu(self, variable, "one", "two", "three", )
        drop2.place(relx=0.9, rely=0.8, width=100, height=100, anchor='n')


		label = Label(self, text="Start Page")
		label.pack(padx=10, pady=10)
		page_one = Button(self, text="Page One", command=lambda:controller.show_frame(PageOne))
		page_one.pack()
		page_two = Button(self, text="Page Two", command=lambda:controller.show_frame(PageTwo))
		page_two.pack()
		'''

class Modules(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        canvas = Canvas(self, height=HEIGHT, width=WIDTH, bg=BG_COLOUR)
        canvas.pack()

        #frames
        self.menu = Frame(self, bg=BG_COLOUR)
        self.menu.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor='n')
        self.frame1 = Frame(self, bg=BG_COLOUR)
        self.frame1.place(relx=0.5, rely=0.1, relwidth=1, relheight=0.3, anchor='n')
        self.frame2 = Frame(self, bg=BG_COLOUR)
        self.frame2.place(relx=0.5, rely=0.4, relwidth=1, relheight=0.3, anchor='n')
        self.frame3 = Frame(self, bg=BG_COLOUR)
        self.frame3.place(relx=0.5, rely=0.7, relwidth=1, relheight=0.3, anchor='n')

        #buttons
        start_page = Button(self, text="Start Page", command=lambda:controller.show_frame(StartPage))
        start_page.place(relx=0.1,rely=0.9,anchor='n')
        profile = Button(self, text="Page Two", command=lambda:controller.show_frame(Profile))
        profile.place(relx=0.9,rely=0.9,anchor='n')
        module1 = Button(self.frame1, text="Module 1", command=lambda : controller.show_learn_frame(learn,'A',teachingDic['A'][0],teachingDic['A'][1]) )
        module1.place(relx=0.2,rely=0.5,anchor='n')


class Profile(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Page Two")
        label.pack(padx=10, pady=10)
        start_page = Button(self, text="Start Page", command=lambda:controller.show_frame(StartPage))
        start_page.pack()
        page_one = Button(self, text="Page One", command=lambda:controller.show_frame(Modules))
        page_one.pack()

class learn(Frame):
    def __init__(self, parent, controller,teaching_item,image,sign_image):
        Frame.__init__(self, parent)
        self.teaching_item=teaching_item
        self.image=PhotoImage(file=image)
        self.sign_image = PhotoImage(file=sign_image)
        self.back_img=PhotoImage(file=back_img)
        self.next_img = PhotoImage(file=next_img)

        # Resizing image to fit on button
        self.image = self.image.subsample(3, 3)
        self.sign_image=self.sign_image.subsample(4,4)
        self.back_img = self.back_img.subsample(8, 8)
        self.next_img = self.next_img.subsample(8, 8)


        canvas = Canvas(self, height=HEIGHT, width=WIDTH, bg= BG_COLOUR)
        canvas.pack()

        #frames
        self.back=Frame(self, bg=BG_COLOUR)
        self.back.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')
        self.menu = Frame(self, bg=BLUE)
        self.menu.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor='n')
        self.pic_frame = Frame(self, bg=WHITE)
        self.pic_frame.place(relx=0.15, rely=0.15, relwidth=0.35, relheight=0.7)
        self.sign_frame = Frame(self, bg=WHITE)
        self.sign_frame.place(relx=0.5, rely=0.15, relwidth=0.35, relheight=0.7)
        self.progress_frame = Frame(self, bg=BG_COLOUR)
        self.progress_frame.place(relx=0.5, rely=0.9, relwidth=1, relheight=0.2, anchor='n')

        #buttons
        self.back = Button(self.menu, text="Back", bg= BLUE, image=self.back_img, border=0, command=lambda:controller.show_frame(StartPage))
        self.back.place(relx=0,rely=0)
        #self.next = Button(self.progress_frame, text="Next", command=lambda:controller.show_learn_frame(learn,chr(randint(65,90))))
        #self.next.place(relx=0.9,rely=0,relwidth=0.2, relheight=0.3,anchor='n')
        self.next = Button(self.menu, text="Next",bg= BLUE, image=self.next_img, border=0, command=lambda:controller.show_learn_frame(learn,chr(randint(65,90))))
        self.next.place(relx=1,rely=0,anchor='ne')
        self.test = Button(self.progress_frame, text="Test")
        self.test.place(relx=0.5,rely=0,relwidth=0.2, relheight=0.3,anchor='n')


        #images
        self.imageLabel=Label(self.pic_frame,text="pic",image=self.image,border=0)
        self.imageLabel.place(relx=0.5,rely=0.5,anchor='c')
        self.signLabel=Label(self.sign_frame,text="pic",image=self.sign_image,border=0)
        self.signLabel.place(relx=0.5,rely=0.5,anchor='c')

class demo1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.back_img=PhotoImage(file=back_img)
        self.cheese_img=PhotoImage(file=cheese_img)
        self.cheese_sign_img=PhotoImage(file=cheese_sign_img)
        self.next_img = PhotoImage(file=next_img)

        # Resizing image to fit on button
        self.back_img = self.back_img.subsample(8, 8)
        self.next_img = self.next_img.subsample(8, 8)
        self.cheese_img = self.cheese_img.subsample(1,1)
        self.cheese_sign_img = self.cheese_sign_img.subsample(2,2)

        canvas = Canvas(self, height=HEIGHT, width=WIDTH, bg= BG_COLOUR)
        canvas.pack()

        #frames
        self.back=Frame(self, bg=BG_COLOUR)
        self.back.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')
        self.menu = Frame(self, bg=BLUE)
        self.menu.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor='n')
        self.pic_frame = Frame(self, bg=WHITE)
        self.pic_frame.place(relx=0.15, rely=0.15, relwidth=0.35, relheight=0.7)
        self.sign_frame = Frame(self, bg=WHITE)
        self.sign_frame.place(relx=0.5, rely=0.15, relwidth=0.35, relheight=0.7)
        self.progress_frame = Frame(self, bg=BG_COLOUR)
        self.progress_frame.place(relx=0.5, rely=0.9, relwidth=1, relheight=0.2, anchor='n')

        #buttons
        self.back = Button(self.menu, text="Back", bg= BLUE, image=self.back_img, border=0, command=lambda:controller.show_frame(StartPage))
        self.back.place(relx=0,rely=0)
        self.next = Button(self.menu, text="Next",bg= BLUE, image=self.next_img, border=0, command=lambda:controller.show_frame(demo2))
        self.next.place(relx=1,rely=0,anchor='ne')
        #self.test = Button(self.progress_frame, text="Test")
        #self.test.place(relx=0.5,rely=0,relwidth=0.2, relheight=0.3,anchor='n')

        #images
        self.imageLabel=Label(self.pic_frame,text="pic",image=self.cheese_img,border=0)
        self.imageLabel.place(relx=0.5,rely=0.5,anchor='c')
        self.signLabel=Label(self.sign_frame,text="pic",image=self.cheese_sign_img,border=0)
        self.signLabel.place(relx=0.5,rely=0.5,anchor='c')

class demo2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.back_img=PhotoImage(file=back_img)
        self.next_img = PhotoImage(file=next_img)
        self.dog_img=PhotoImage(file=dog_img)
        self.dog_sign_img=PhotoImage(file=dog_sign_img)

        # Resizing image to fit on button
        self.back_img = self.back_img.subsample(8, 8)
        self.next_img = self.next_img.subsample(8, 8)
        self.dog_img = self.dog_img.subsample(1, 1)
        self.dog_sign_img = self.dog_sign_img.subsample(2, 2)


        canvas = Canvas(self, height=HEIGHT, width=WIDTH, bg= BG_COLOUR)
        canvas.pack()

        #frames
        self.back=Frame(self, bg=BG_COLOUR)
        self.back.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')
        self.menu = Frame(self, bg=BLUE)
        self.menu.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor='n')
        self.pic_frame = Frame(self, bg=WHITE)
        self.pic_frame.place(relx=0.15, rely=0.15, relwidth=0.35, relheight=0.7)
        self.sign_frame = Frame(self, bg=WHITE)
        self.sign_frame.place(relx=0.5, rely=0.15, relwidth=0.35, relheight=0.7)
        self.progress_frame = Frame(self, bg=BG_COLOUR)
        self.progress_frame.place(relx=0.5, rely=0.9, relwidth=1, relheight=0.2, anchor='n')

        #buttons
        self.back = Button(self.menu, text="Back", bg= BLUE, image=self.back_img, border=0, command=lambda:controller.show_frame(demo1))
        self.back.place(relx=0,rely=0)
        #self.test = Button(self.progress_frame, text="Test")
        #self.test.place(relx=0.5,rely=0,relwidth=0.2, relheight=0.3,anchor='n')

        #images
        self.imageLabel=Label(self.pic_frame,text="pic",image=self.dog_img,border=0)
        self.imageLabel.place(relx=0.5,rely=0.5,anchor='c')
        self.signLabel=Label(self.sign_frame,text="pic",image=self.dog_sign_img,border=0)
        self.signLabel.place(relx=0.5,rely=0.5,anchor='c')



app = App()
app.mainloop()
