# Author : Gideon Daniels
# Github :
# Replit :

from tkinter import messagebox
# Validates that all inputs are filled in
# Validates that I.D entry have 13 digits
# Validates age is greater or equal to 18


def validate_email(self, ):
    if "@" not in self.email:
        messagebox.showwarning("ERROR", "PLEASE ENTER VAlID EMAIL WITH @")


def validate_id(self):
    if len(self.id) != 13:
        messagebox.showwarning("ERROR", "PLEASE ENTER VALID ID CONTAINING 13 DIGITS")


def validate_entries(self, name, surname, day, month, year, id, email):
    if name == "" or surname == "" or id == "" or day == "" or month == "" or year == "" or id == "" or email == "":
        messagebox.showwarning("ERROR", "PLEASE FILL OUT ALL ENTRIES")
