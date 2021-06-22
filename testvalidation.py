# Author : Gideon Daniels
# Github :
# Replit :
import unittest
from tkinter import messagebox
# Validates that all inputs are filled in
# Validates that I.D entry have 13 digits
# Validates age is greater or equal to 18
import unittest


class TestValidation(unittest.TestCase):
    def validate_email(self, email):
        if "@" not in email:
            self.assertTrue(id)
            messagebox.showwarning("ERROR", "PLEASE ENTER VAlID EMAIL WITH @")

    def validate_id(self,id):
        if len(id) != 13:
            self.assertTrue(id)
            messagebox.showwarning("ERROR", "PLEASE ENTER VALID ID CONTAINING 13 DIGITS")

    def validate_entries(self, name, surname, day, month, year, id, email):
        if name == "" or surname == "" or id == "" or day == "" or month == "" or year == "" or id == "" or email == "":
            messagebox.showwarning("ERROR", "PLEASE FILL OUT ALL ENTRIES")

