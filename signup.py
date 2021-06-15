# Author : Gideon Daniels
# Github :
# Replit :

# import tkinter library
from tkinter import *

# Login Screen Class


class LoginScreen:
    # slaving gender
    gender = StringVar
    # Storing input into variables
    # Storing Date Of Birth
    names = StringVar
    surname = StringVar
    id = IntVar
    email = StringVar
    days = StringVar
    months = StringVar
    years = StringVar

    def __init__(self):
        # create instance of frame
        self.window = Tk()

        # setting up window
        self.window.geometry("1080x720")
        self.window.config(bg="#3986d2")
        self.window.title("Sign Up Screen")

        # creating widgets
        # Header Frame
        self.labelframe_header = LabelFrame(self.window,bg="#ebec00", width=200, heigh=100)
        self.labelframe_header.pack(fill="both")
        # Header widget
        self.label_header = Label(self.labelframe_header, text="SIGN UP", bg="#ebec00", font="Times 30 bold")
        self.label_header.place(x=450, y=25)
        # Sign Up Frame
        self.labelframe_login = LabelFrame(self.window, bg="#ebec00", width=600, heigh=400)
        self.labelframe_login.place(x=250, y=150)
        self.label_login = Label(self.labelframe_login, font="Times 14", bg="#ebec00")
        self.label_login.place(y=10, x=270)
        # Name widget
        self.label_email = Label(self.labelframe_login, text="NAME", font="Times 14", bg="#ebec00")
        self.label_email.place(y=10, x=100)
        self.entry_email = Entry(self.labelframe_login, font="Times 12", bg="#3986d2", width=40)
        self.entry_email.place(y=10, x=250)
        # Surname widget
        self.label_email = Label(self.labelframe_login, text="SURNAME", font="Times 14", bg="#ebec00")
        self.label_email.place(y=50, x=100)
        self.entry_email = Entry(self.labelframe_login, font="Times 12", bg="#3986d2", width=40)
        self.entry_email.place(y=50, x=250)
        # i.d widget
        self.label_id = Label(self.labelframe_login, text="I.D", font="Times 16", bg="#ebec00")
        self.label_id.place(y=95, x=100)
        self.entry_id = Entry(self.labelframe_login, font="Times 12", bg="#3986d2", width=40)
        self.entry_id.place(y=95, x=250)
        # Email widget
        self.label_id = Label(self.labelframe_login, text="EMAIL", font="Times 16", bg="#ebec00")
        self.label_id.place(y=140, x=100)
        self.entry_id = Entry(self.labelframe_login, font="Times 12", bg="#3986d2", width=40)
        self.entry_id.place(y=140, x=250)
        # Gender Selection Widget
        self.label_id = Label(self.labelframe_login, text="GENDER", font="Times 16", bg="#ebec00")
        self.label_id.place(y=180, x=100)
        self.radio_button_male = Radiobutton(self.labelframe_login, text="MALE", value="MALE",
                                             textvariable=self.gender, font="Times 16", bg="#3986d2")
        self.radio_button_male.place(y=180, x=250)
        self.radio_button_female = Radiobutton(self.labelframe_login, text="FEMALE", value="FEMALE",
                                               textvariable=self.gender, font="Times 16", bg="#3986d2")
        self.radio_button_female.place(y=180, x=351)
        # Date of birth widgets
        self.date_of_birth = Label(self.labelframe_login, text="D.O.B", font="Times 16", bg="#ebec00")
        self.date_of_birth.place(y=220, x=100)
        self.label_days = Label(self.labelframe_login, text="DD", bg="#ebec00")
        self.label_days.place(y=220, x=250)
        self.label_months = Label(self.labelframe_login, text="MM", bg="#ebec00")
        self.label_months.place(y=220, x=310)
        self.label_years = Label(self.labelframe_login, text="YYYY", bg="#ebec00")
        self.label_years.place(y=220, x=375)
        self.entry_days = Entry(self.labelframe_login, textvariable=self.days, font="Times 12", bg="#3986d2",
                                width=2)
        self.entry_days.place(y=220, x=280)
        self.entry_months = Entry(self.labelframe_login, textvariable=self.months, font="Times 12", bg="#3986d2",
                                  width=2)
        self.entry_months.place(y=220, x=345)
        self.entry_years = Entry(self.labelframe_login, textvariable=self.years, font="Times 12", bg="#3986d2",
                                 width=4)
        self.entry_years.place(y=220, x=420)
        # buttons
        self.button_signup = Button(self.labelframe_login, text="SIGN UP", font="Times 16", bg="#3986d2")
        self.button_signup.place(y=300, x=150)
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