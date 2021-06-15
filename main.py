# Author : Gideon Daniels
# Github :
# Replit :

# import tkinter library
from tkinter import *

# Login Screen Class


class LoginScreen:
    def __init__(self):
        # create instance of frame
        self.window = Tk()

        # setting up window
        self.window.geometry("1080x720")
        self.window.config(bg="#3986d2")
        self.window.title("Login Screen")

        # creating widgets
        # Header Frame
        self.labelframe_header = LabelFrame(self.window,bg="#ebec00", width=200, heigh=100)
        self.labelframe_header.pack(fill="both")
        # Header widget
        self.label_header = Label(self.labelframe_header, text="WELCOME", bg="#ebec00", font="Times 30 bold")
        self.label_header.place(x=450, y=10)
        self.label_header = Label(self.labelframe_header, text="TO LOTTERY", bg="#ebec00", font="Times 30 bold")
        self.label_header.place(x=430, y=50)
        # Log In Frame
        self.labelframe_login = LabelFrame(self.window, bg="#ebec00", width=600, heigh=400)
        self.labelframe_login.place(x=250, y=150)
        self.label_login = Label(self.labelframe_login, text="LOGIN", font="Times 20", bg="#ebec00")
        self.label_login.place(y=10, x=270)
        # Email widget
        self.label_email = Label(self.labelframe_login, text="EMAIL", font="Times 16", bg="#ebec00")
        self.label_email.place(y=120, x=150)
        self.entry_email = Entry(self.labelframe_login, font="Times 16", bg="#3986d2")
        self.entry_email.place(y=120, x=250)
        # i.d widget
        self.label_id = Label(self.labelframe_login, text="I.D", font="Times 16", bg="#ebec00")
        self.label_id.place(y=170, x=150)
        self.entry_id = Entry(self.labelframe_login, font="Times 16", bg="#3986d2")
        self.entry_id.place(y=170, x=250)
        # buttons
        self.button_login = Button(self.labelframe_login, text="LOGIN", font="Times 16", bg="#3986d2")
        self.button_login.place(y=300, x=150)
        self.button_signup = Button(self.labelframe_login, text="SIGN UP", font="Times 16", bg="#3986d2")
        self.button_signup.place(y=300, x=250)
        self.button_exit = Button(self.labelframe_login, text="EXIT", font="Times 16", bg="#3986d2",
                                  command=self.exit_button)
        self.button_exit.place(y=300, x=365)
        # FOOTER
        self.labelframe_footer = LabelFrame(self.window, bg="#ebec00", width=200, heigh=100)
        self.labelframe_footer.pack(fill="both", side=BOTTOM)
        # runs screen
        self.window.mainloop()

    # Functions for buttons
    def login_button(self):
        pass

    def signup_button(self):
        pass

    def exit_button(self):
        self.window.destroy()


# Runs Login Screen
LoginScreen()