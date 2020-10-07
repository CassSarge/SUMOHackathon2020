#Source: CJ van der Smissen
#Source: https://github.com/introtocomputerscience/TKinterExample
from tkinter import *
from settings import *
from pics import *

#flags
global pic_learn


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        #Setup Frame
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}

        for F in (StartPage, Modules, Profile,picture_learn_letter_A,picture_test_letter_A,text_learn_letter_A):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage,False)

    def show_frame(self, context,picFlag):
        if picFlag==0:
            global pic_learn
            pic_learn = 0
        elif picFlag==1:
            pic_learn = 1

        frame = self.frames[context]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # photo database
        self.pencil = PhotoImage(file=".\img\photo1.png")
        # Resizing image to fit on button
        self.pencil = self.pencil.subsample(3, 3)

        canvas = Canvas(self, height=HEIGHT, width=WIDTH)
        canvas.pack()

        self.frame = Frame(self, bg=BG_COLOUR)
        self.frame.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')

        # buttons
        pic_learn_button = Button(self.frame, text="pic", bg="orange", fg="white", image=self.pencil, border=0,command=lambda:controller.show_frame(Modules,1))
        pic_learn_button.place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')

        text_learn_button = Button(self.frame, text="ABC", bg="orange", fg="white",command=lambda:controller.show_frame(Modules,0))
        text_learn_button.place(relx=0.5, rely=0.6, relwidth=0.2, relheight=0.1, anchor='n')

        label = Label(self.frame, text="TANCOS", bg=BUTTON_COLOUR)
        label.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.1, anchor='n')

        # drop down
        variable = StringVar(self)
        variable.set("one")  # default value

        drop1 = OptionMenu(self, variable, "Auslan", "ASL", "BSL")
        drop1.config(bg='orange')
        drop1["menu"].config(bg="orange")
        drop1.place(relx=0.1, rely=0.8, width=100, height=100, anchor='n')

        drop2 = OptionMenu(self, variable, "one", "two", "three", )
        drop2.place(relx=0.9, rely=0.8, width=100, height=100, anchor='n')

        '''
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

        canvas = Canvas(self, height=HEIGHT, width=WIDTH)
        canvas.pack()

        #frames
        self.menu = Frame(self, bg=BG_COLOUR)
        self.menu.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor='n')
        self.frame1 = Frame(self, bg=BG_COLOUR_2)
        self.frame1.place(relx=0.5, rely=0.1, relwidth=1, relheight=0.3, anchor='n')
        self.frame2 = Frame(self, bg=BG_COLOUR)
        self.frame2.place(relx=0.5, rely=0.4, relwidth=1, relheight=0.3, anchor='n')
        self.frame3 = Frame(self, bg=BG_COLOUR_2)
        self.frame3.place(relx=0.5, rely=0.7, relwidth=1, relheight=0.3, anchor='n')

        #buttons
        start_page = Button(self, text="Start Page", command=lambda:controller.show_frame(StartPage,False))
        start_page.place(relx=0.1,rely=0.9,anchor='n')
        profile = Button(self, text="Page Two", command=lambda:controller.show_frame(Profile,False))
        profile.place(relx=0.9,rely=0.9,anchor='n')
        module1 = Button(self.frame1, text="Module 1", command=lambda : controller.show_frame(picture_learn_letter_A,2) if pic_learn==1 else controller.show_frame(text_learn_letter_A,2))
        module1.place(relx=0.2,rely=0.5,anchor='n')


class Profile(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Page Two")
        label.pack(padx=10, pady=10)
        start_page = Button(self, text="Start Page", command=lambda:controller.show_frame(StartPage,2))
        start_page.pack()
        page_one = Button(self, text="Page One", command=lambda:controller.show_frame(Modules,2))
        page_one.pack()

class picture_learn_letter_A(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        canvas = Canvas(self, height=HEIGHT, width=WIDTH)
        canvas.pack()

        #frames
        self.menu = Frame(self, bg=BG_COLOUR)
        self.menu.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor='n')
        self.pic_frame = Frame(self, bg=BG_COLOUR)
        self.pic_frame.place(relx=0.15, rely=0.1, relwidth=0.35, relheight=0.7)
        self.sign_frame = Frame(self, bg=BG_COLOUR_2)
        self.sign_frame.place(relx=0.5, rely=0.1, relwidth=0.35, relheight=0.7)
        self.progress_frame = Frame(self, bg=BG_COLOUR_2)
        self.progress_frame.place(relx=0.5, rely=0.9, relwidth=1, relheight=0.2, anchor='n')


        #buttons
        self.back = Button(self.menu, text="Back", command=lambda:controller.show_frame(Modules,2))
        self.back.place(relx=0,rely=0)
        self.next = Button(self.progress_frame, text="Next", command=lambda:controller.show_frame(StartPage,2))
        self.next.place(relx=0.9,rely=0.1,anchor='c')
        self.test = Button(self.progress_frame, text="Test", command=lambda:controller.show_frame(picture_test_letter_A,2))
        self.test.place(relx=0.5,rely=0.1,anchor='c')


class text_learn_letter_A(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        canvas = Canvas(self, height=HEIGHT, width=WIDTH)
        canvas.pack()

        #frames
        self.menu = Frame(self, bg=BG_COLOUR)
        self.menu.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor='n')
        self.text_frame = Frame(self, bg=BG_COLOUR)
        self.text_frame.place(relx=0.15, rely=0.1, relwidth=0.35, relheight=0.7)
        self.sign_frame = Frame(self, bg=BG_COLOUR_2)
        self.sign_frame.place(relx=0.5, rely=0.1, relwidth=0.35, relheight=0.7)
        self.progress_frame = Frame(self, bg=BG_COLOUR_2)
        self.progress_frame.place(relx=0.5, rely=0.9, relwidth=1, relheight=0.2, anchor='n')


        #buttons
        self.back = Button(self.menu, text="Back", command=lambda:controller.show_frame(Modules,2))
        self.back.place(relx=0,rely=0)
        self.next = Button(self.progress_frame, text="Next", command=lambda:controller.show_frame(StartPage,2))
        self.next.place(relx=0.9,rely=0.1,anchor='c')
        self.test = Button(self.progress_frame, text="Test", command=lambda:controller.show_frame(picture_test_letter_A,2))
        self.test.place(relx=0.5,rely=0.1,anchor='c')

        #labels
        self.text=Label(self.text_frame, text="This is the text module")
        self.text.place(relx=0.5,rely=0.5,anchor='c')

class picture_test_letter_A(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        canvas = Canvas(self, height=HEIGHT, width=WIDTH,bg=BG_COLOUR)
        canvas.pack()

        #frames
        self.menu = Frame(self, bg=BG_COLOUR)
        self.menu.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor='n')
        self.input_frame = Frame(self, bg=BG_COLOUR_2)
        self.input_frame.place(relx=0.5, rely=0.1, relwidth=0.6, relheight=0.7,anchor='n')
        self.score_frame = Frame(self, bg=BG_COLOUR)
        self.score_frame.place(relx=0, rely=0.1, relwidth=0.2, relheight=0.7)
        self.progress_frame = Frame(self, bg=BG_COLOUR)
        self.progress_frame.place(relx=0.5, rely=0.9, relwidth=1, relheight=0.2, anchor='n')


        #buttons
        self.back = Button(self.menu, text="Back", command=lambda:controller.show_frame(Modules,2))
        self.back.place(relx=0,rely=0)
        self.next = Button(self.progress_frame, text="Next", command=lambda:controller.show_frame(StartPage,2))
        self.next.place(relx=0.9,rely=0.1,anchor='c')
        self.learn = Button(self.progress_frame, text="Learn", command=lambda:controller.show_frame(picture_learn_letter_A,2))
        self.learn.place(relx=0.5,rely=0.1,anchor='c')





app = App()
app.mainloop()