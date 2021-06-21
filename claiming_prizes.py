# Author : Gideon Daniels
# Github :
# Replit :

# import tkinter library
from tkinter import *
from signup import *
from login import *
# Claim Prizes Screen


class ClaimPrizes:
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
        self.label_header = Label(self.labelframe_header, text="BANKING DETAILS", bg="#ebec00", font="Times 30 bold")
        self.label_header.place(x=430, y=50)

        # Log In Frame
        self.labelframe_login = LabelFrame(self.window, bg="#ebec00", width=600, heigh=400)
        self.labelframe_login.place(x=20, y=150)
        self.label_login = Label(self.labelframe_login, text="LOGIN", font="Times 20", bg="#ebec00")
        self.label_login.place(y=10, x=270)
        # Account holder name widget
        self.label_account_holder = Label(self.labelframe_login, text="Account Holder name", font="Times 16",
                                          bg="#ebec00")
        self.label_account_holder.place(y=120, x=20)
        self.entry_account_holder = Entry(self.labelframe_login, font="Times 16", bg="#3986d2")
        self.entry_account_holder.place(y=120, x=250)
        # Bank account widget
        self.label_id = Label(self.labelframe_login, text="Bank Account Number", font="Times 16", bg="#ebec00")
        self.label_id.place(y=170, x=20)
        self.entry_id = Entry(self.labelframe_login, font="Times 16", bg="#3986d2")
        self.entry_id.place(y=170, x=250)
        # Currency Converter
        self.labelframe_converter= LabelFrame(self.window, bg="#ebec00", width=400, heigh=400)
        self.labelframe_converter.place(x=650, y=150)
        self.label_currency_converter = Label(self.labelframe_converter, text="CURRENCY CONVERTER", font="Times 20",
                                              bg="#ebec00")
        self.label_currency_converter.place(y=10, x=50)
        # buttons
        self.button_play_again = Button(self.labelframe_login, text="PLAY AGAIN", font="Times 16", bg="#3986d2")
        self.button_play_again.place(y=300, x=100)
        self.button_approve = Button(self.labelframe_login, text="APPROVE", font="Times 16", bg="#3986d2")
        self.button_approve.place(y=300, x=280)
        self.button_exit = Button(self.labelframe_login, text="EXIT", font="Times 16", bg="#3986d2",
                                  command=self.exit_button)
        self.button_exit.place(y=300, x=420)
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
ClaimPrizes()
