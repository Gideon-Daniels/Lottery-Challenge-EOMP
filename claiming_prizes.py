# Author : Gideon Daniels
# Github :
# Replit :

# import tkinter library
import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests
# from signup import *
# from login import *
# Claim Prizes Screen
# Importing modules to send email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Importing currency converter


class ClaimPrizes:
    def __init__(self):
        # create instance of frame
        self.window = Tk()
        # setting up window
        self.window.geometry("1080x720")
        self.window.config(bg="#3986d2")
        self.window.title("Login Screen")
        # currency converter
        self.amount_converted = StringVar()
        self.re = requests.get('https://v6.exchangerate-api.com/v6/6698980fefc5cd611ec51be2/latest/USD')
        self.result = self.re.json()

        self.converting_rate = self.result['conversion_rates']
        self.currencies = []
        self.currencies_two = []
        for i in self.converting_rate.keys():
            self.currencies.append(i)
            for x in self.converting_rate.keys():
                self.currencies_two.append(x)

        # variables used for email
        self.mailers_id = "gideondaniels.dragoonix@gmail.com"
        self.email_receiver_id = ["gideon.daniels@yahoo.com", "thepelo@lifechoices.co.za", "aslamedien9@gmail.com",
                                  "sithandathuzipho@gmail.com"]
        # variables used for dropdown box
        self.menu = StringVar()
        self.menu.set("Standard Bank")

        self.options = ["Standard Bank", "Absa", "Capitech", ]

        # creating widgets
        # Header Frame
        self.labelframe_header = LabelFrame(self.window, bg="#ebec00", width=200, heigh=100)
        self.labelframe_header.pack(fill="both")
        # Header widget
        self.label_header = Label(self.labelframe_header, text="BANKING DETAILS", bg="#ebec00", font="Times 30 bold")
        self.label_header.place(x=430, y=50)
        # Log In Frame
        self.labelframe_details = LabelFrame(self.window, bg="#ebec00", width=600, heigh=400)
        self.labelframe_details.place(x=20, y=150)
        self.label_header_details = Label(self.labelframe_details, text="DETAILS", font="Times 20", bg="#ebec00")
        self.label_header_details.place(y=10, x=270)
        # drop down menu widget
        self.label_bank = Label(self.labelframe_details, text="Bank", font="Times 16", bg="#ebec00")
        self.label_bank.place(y=220, x=20)
        self.option_menu_banks = OptionMenu(self.labelframe_details, self.menu, *self.options)
        self.option_menu_banks.config(font=" 16", bg="#3986d2")
        self.option_menu_banks.place(y=220, x=250)
        self.option_menu_banks["menu"].config(bg="#3986d2")
        # Account holder name widget
        self.label_account_holder = Label(self.labelframe_details, text="Account Holder name", font="Times 16",
                                          bg="#ebec00")
        self.label_account_holder.place(y=120, x=20)
        self.entry_account_holder = Entry(self.labelframe_details, font="Times 16", bg="#3986d2")
        self.entry_account_holder.place(y=120, x=250)
        # Bank account widget
        self.label_id = Label(self.labelframe_details, text="Bank Account Number", font="Times 16", bg="#ebec00")
        self.label_id.place(y=170, x=20)
        self.entry_id = Entry(self.labelframe_details, font="Times 16", bg="#3986d2")
        self.entry_id.place(y=170, x=250)
        # Currency Converter
        self.labelframe_converter = LabelFrame(self.window, bg="#ebec00", width=400, heigh=400)
        self.labelframe_converter.place(x=650, y=150)
        self.label_currency_converter = Label(self.labelframe_converter, text="CURRENCY CONVERTER", font="Times 20",
                                              bg="#ebec00")

        self.label_currency_converter.place(y=10, x=50)
        self.label_winning = Label(self.labelframe_converter, text="WINNINGS", font="Times 16",
                                   bg="#ebec00")
        self.label_winning.place(y=120, x=20)
        self.label_from_currency = Label(self.labelframe_converter, text="Convert From", font="Times 16",
                                         bg="#ebec00")
        self.label_from_currency.place(y=190, x=20)

        self.label_to_currency = Label(self.labelframe_converter, text="Convert To", font="Times 16",
                                       bg="#ebec00")
        self.label_to_currency.place(y=250, x=20)

        self.label_converted_amount = Label(self.labelframe_converter, text="Converted Amount", font="Times 16",
                                            bg="#ebec00")
        self.label_converted_amount.place(y=300, x=20)

        self.entry_input_amount = Entry(self.labelframe_converter, font="Times 16",
                                        bg="#3986d2", width=8)
        self.entry_input_amount.place(y=120, x=220)

        self.combobox_currency_one = ttk.Combobox(self.labelframe_converter, values=self.currencies, state="read-only")
        self.combobox_currency_one.set("Select Currency")
        self.combobox_currency_one.place(x=200, y=190)

        self.combobox_currency_two = ttk.Combobox(self.labelframe_converter, values=self.currencies_two,
                                                  state="read-only")
        self.combobox_currency_two.set("Select Currency")
        self.combobox_currency_two.place(x=200, y=250)
        self.entry_output_amount = Entry(self.labelframe_converter, textvariable=self.amount_converted, font="Times 12",
                                         bg="#3986d2", width=8)
        self.entry_output_amount.place(y=300, x=220)

        # buttons
        self.button_convert = Button(self.labelframe_converter, text="CONVERT", font="Times 16", bg="#3986d2",
                                     command=self.convert)
        self.button_convert.place(y=350, x=20)
        self.button_clear = Button(self.labelframe_converter, text="CLEAR", font="Times 16", bg="#3986d2",
                                   command=self.clear)
        self.button_clear.place(y=350, x=250)
        self.button_play_again = Button(self.labelframe_details, text="PLAY AGAIN", font="Times 16", bg="#3986d2",
                                        command=self.play_again)
        self.button_play_again.place(y=350, x=100)
        self.button_approve = Button(self.labelframe_details, text="APPROVE", font="Times 16", bg="#3986d2",
                                     command=self.approve)
        self.button_approve.place(y=350, x=280)

        self.button_exit = Button(self.labelframe_details, text="EXIT", font="Times 16", bg="#3986d2",
                                  command=self.exit_button)
        self.button_exit.place(y=350, x=420)
        # FOOTER
        self.labelframe_footer = LabelFrame(self.window, bg="#ebec00", width=200, heigh=100)
        self.labelframe_footer.pack(fill="both", side=BOTTOM)

        # runs screen
        self.window.mainloop()
    # Functions for buttons

    def convert(self):
        amount = float(self.entry_input_amount.get())
        currency_one = self.combobox_currency_one.get()
        currency_two = self.combobox_currency_one.get()
        converted_amount = round(amount*self.converting_rate[currency_two], 2)
        self.amount_converted.set(converted_amount)

    def clear(self):
        pass

    def play_again(self):
        pass

    def approve(self):
        if self.entry_id.get() == "" and len(self.entry_id.get()) != 13:
            messagebox.showinfo("Warning", "Invalid I.D")
        elif self.entry_account_holder.get() == "":
            messagebox.showinfo("Warning", "Please fill out all fields")
        else:
            password = input("Enter your password")
            subject = "Greetings"
            msg = MIMEMultipart()
            msg['From'] = subject
            msg['To'] = ", ".join(self.email_receiver_id)
            body = f"Hello {self.entry_account_holder.get()}"
            body = body + f"Your prize have been send."
            msg.attach(MIMEMultipart(body, 'plain'))
            text = msg.as_string()
            s = smtplib.SMTP("smtp.gmail.com", 587)
            s.starttls()
            s.login(self.mailers_id, password)  # Authentication
            s.starttls()
            s.login(self.mailers_id, password)  # message to be send
            s.sendmail(self.mailers_id, self.email_receiver_id, text)  # send the mail
            s.quit()

    def exit_button(self):
        self.window.destroy()


# Runs Login Screen
ClaimPrizes()
