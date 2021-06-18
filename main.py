# Author : Gideon Daniels
# Github :
# Replit :

# import tkinter library
from tkinter import *


# Login Screen Class


class Main:
    def __init__(self):
        # create instance of frame
        self.window = Tk()

        # List
        self.my_list_one = []
        self.my_list_two = []
        self.my_list_three = []
        self.my_winning_list = [2, 5, 28, 38, 16, 75]

        # setting up window
        self.window.geometry("1080x720")
        self.window.config(bg="#3986d2")
        self.window.title("Main")

        # creating widgets
        # Header Frame
        self.labelframe_header = LabelFrame(self.window, bg="#ebec00", width=200, heigh=100)
        self.labelframe_header.pack(fill="both")
        # Header widget
        self.label_header = Label(self.labelframe_header, text="WELCOME", bg="#ebec00", font="Times 30 bold")
        self.label_header.place(x=450, y=10)
        # Frames
        self.labelframe_buttons = LabelFrame(self.window, bg="#ebec00", width=400, heigh=450)
        self.labelframe_buttons.place(y=120, x=100)
        # Display buttons within frames
        # ROW ONE
        self.button_one = Button(self.labelframe_buttons, text="1", font="Times 12", bg="#3986d2",
                                 command=lambda: self.displaying_numbers(1))
        self.button_one.place(y=10, x=90)
        self.button_two = Button(self.labelframe_buttons, text="2", font="Times 12", bg="#3986d2",
                                 command=lambda: self.displaying_numbers(2))
        self.button_two.place(y=10, x=130)
        self.button_three = Button(self.labelframe_buttons, text="3", font="Times 12", bg="#3986d2",
                                   command=lambda: self.displaying_numbers(3))
        self.button_three.place(y=10, x=170)
        self.button_four = Button(self.labelframe_buttons, text="4", font="Times 12", bg="#3986d2",
                                  command=lambda: self.displaying_numbers(4))
        self.button_four.place(y=10, x=210)
        self.button_five = Button(self.labelframe_buttons, text="5", font="Times 12", bg="#3986d2",
                                  command=lambda: self.displaying_numbers(5))
        self.button_five.place(y=10, x=250)
        # ROW TWO
        self.button_six = Button(self.labelframe_buttons, text="6", font="Times 12", bg="#3986d2",
                                 command=lambda: self.displaying_numbers(6))
        self.button_six.place(y=50, x=90)
        self.button_seven = Button(self.labelframe_buttons, text="7", font="Times 12", bg="#3986d2",
                                   command=lambda: self.displaying_numbers(7))
        self.button_seven.place(y=50, x=130)
        self.button_eight = Button(self.labelframe_buttons, text="8", font="Times 12", bg="#3986d2",
                                   command=lambda: self.displaying_numbers(8))
        self.button_eight.place(y=50, x=170)
        self.button_nine = Button(self.labelframe_buttons, text="9", font="Times 12", bg="#3986d2",
                                  command=lambda: self.displaying_numbers(9))
        self.button_nine.place(y=50, x=210)
        self.button_ten = Button(self.labelframe_buttons, text="10", font="Times 12", bg="#3986d2", width=1,
                                 command=lambda: self.displaying_numbers(10))
        self.button_ten.place(y=50, x=250)
        # ROW THREE
        self.button_eleven = Button(self.labelframe_buttons, text="11", font="Times 12", bg="#3986d2", width=1,
                                    command=lambda: self.displaying_numbers(11))
        self.button_eleven.place(y=90, x=90)
        self.button_twelve = Button(self.labelframe_buttons, text="12", font="Times 12", bg="#3986d2", width=1,
                                    command=lambda: self.displaying_numbers(12))
        self.button_twelve.place(y=90, x=130)
        self.button_thirteen = Button(self.labelframe_buttons, text="13", font="Times 12", bg="#3986d2", width=1,
                                      command=lambda: self.displaying_numbers(13))
        self.button_thirteen.place(y=90, x=170)
        self.button_fourteen = Button(self.labelframe_buttons, text="14", font="Times 12", bg="#3986d2", width=1,
                                      command=lambda: self.displaying_numbers(14))
        self.button_fourteen.place(y=90, x=210)
        self.button_fifteen = Button(self.labelframe_buttons, text="15", font="Times 12", bg="#3986d2", width=1,
                                     command=lambda: self.displaying_numbers(15))
        self.button_fifteen.place(y=90, x=250)
        # ROW FOUR
        self.button_sixteen = Button(self.labelframe_buttons, text="16", font="Times 12", bg="#3986d2", width=1,
                                     command=lambda: self.displaying_numbers(16))
        self.button_sixteen.place(y=130, x=90)
        self.button_seventeen = Button(self.labelframe_buttons, text="17", font="Times 12", bg="#3986d2", width=1,
                                       command=lambda: self.displaying_numbers(17))
        self.button_seventeen.place(y=130, x=130)
        self.button_eighteen = Button(self.labelframe_buttons, text="18", font="Times 12", bg="#3986d2", width=1,
                                      command=lambda: self.displaying_numbers(18))
        self.button_eighteen.place(y=130, x=170)
        self.button_nineteen = Button(self.labelframe_buttons, text="19", font="Times 12", bg="#3986d2", width=1,
                                      command=lambda: self.displaying_numbers(19))
        self.button_nineteen.place(y=130, x=210)
        self.button_twenty = Button(self.labelframe_buttons, text="20", font="Times 12", bg="#3986d2", width=1,
                                    command=lambda: self.displaying_numbers(20))
        self.button_twenty.place(y=130, x=250)
        # ROW FIVE
        self.button_twenty_one = Button(self.labelframe_buttons, text="21", font="Times 12", bg="#3986d2", width=1,
                                        command=lambda: self.displaying_numbers(21))
        self.button_twenty_one.place(y=170, x=90)
        self.button_twenty_two = Button(self.labelframe_buttons, text="22", font="Times 12", bg="#3986d2", width=1,
                                        command=lambda: self.displaying_numbers(22))
        self.button_twenty_two.place(y=170, x=130)
        self.button_twenty_three = Button(self.labelframe_buttons, text="23", font="Times 12", bg="#3986d2", width=1,
                                          command=lambda: self.displaying_numbers(23))
        self.button_twenty_three.place(y=170, x=170)
        self.button_twenty_four = Button(self.labelframe_buttons, text="24", font="Times 12", bg="#3986d2", width=1,
                                         command=lambda: self.displaying_numbers(24))
        self.button_twenty_four.place(y=170, x=210)
        self.button_twenty_five = Button(self.labelframe_buttons, text="25", font="Times 12", bg="#3986d2", width=1,
                                         command=lambda: self.displaying_numbers(25))
        self.button_twenty_five.place(y=170, x=250)
        # ROW SIX
        self.button_twenty_six = Button(self.labelframe_buttons, text="26", font="Times 12", bg="#3986d2", width=1,
                                        command=lambda: self.displaying_numbers(26))
        self.button_twenty_six.place(y=210, x=90)
        self.button_twenty_seven = Button(self.labelframe_buttons, text="27", font="Times 12", bg="#3986d2", width=1,
                                          command=lambda: self.displaying_numbers(27))
        self.button_twenty_seven.place(y=210, x=130)
        self.button_twenty_eight = Button(self.labelframe_buttons, text="28", font="Times 12", bg="#3986d2", width=1,
                                          command=lambda: self.displaying_numbers(28))
        self.button_twenty_eight.place(y=210, x=170)
        self.button_twenty_nine = Button(self.labelframe_buttons, text="29", font="Times 12", bg="#3986d2", width=1,
                                         command=lambda: self.displaying_numbers(29))
        self.button_twenty_nine.place(y=210, x=210)
        self.button_thirty = Button(self.labelframe_buttons, text="30", font="Times 12", bg="#3986d2", width=1,
                                    command=lambda: self.displaying_numbers(30))
        self.button_thirty.place(y=210, x=250)
        # ROW SEVEN
        self.button_thirty_one = Button(self.labelframe_buttons, text="31", font="Times 12", bg="#3986d2", width=1,
                                        command=lambda: self.displaying_numbers(31))
        self.button_thirty_one.place(y=250, x=90)
        self.button_thirty_three = Button(self.labelframe_buttons, text="32", font="Times 12", bg="#3986d2", width=1,
                                          command=lambda: self.displaying_numbers(32))
        self.button_thirty_three.place(y=250, x=130)
        self.button_thirty_four = Button(self.labelframe_buttons, text="33", font="Times 12", bg="#3986d2", width=1,
                                         command=lambda: self.displaying_numbers(33))
        self.button_thirty_four.place(y=250, x=170)
        self.button_thirty_four = Button(self.labelframe_buttons, text="34", font="Times 12", bg="#3986d2", width=1,
                                         command=lambda: self.displaying_numbers(34))
        self.button_thirty_four.place(y=250, x=210)
        self.button_thirty_five = Button(self.labelframe_buttons, text="35", font="Times 12", bg="#3986d2", width=1,
                                         command=lambda: self.displaying_numbers(35))
        self.button_thirty_five.place(y=250, x=250)
        # ROW EIGHT
        self.button_thirty_six = Button(self.labelframe_buttons, text="36", font="Times 12", bg="#3986d2", width=1,
                                        command=lambda: self.displaying_numbers(36))
        self.button_thirty_six.place(y=290, x=90)
        self.button_thirty_seven = Button(self.labelframe_buttons, text="37", font="Times 12", bg="#3986d2", width=1,
                                          command=lambda: self.displaying_numbers(37))
        self.button_thirty_seven.place(y=290, x=130)
        self.button_thirty_eight = Button(self.labelframe_buttons, text="38", font="Times 12", bg="#3986d2", width=1,
                                          command=lambda: self.displaying_numbers(38))
        self.button_thirty_eight.place(y=290, x=170)
        self.button_thirty_nine = Button(self.labelframe_buttons, text="39", font="Times 12", bg="#3986d2", width=1,
                                         command=lambda: self.displaying_numbers(39))
        self.button_thirty_nine.place(y=290, x=210)
        self.button_forty = Button(self.labelframe_buttons, text="40", font="Times 12", bg="#3986d2", width=1,
                                   command=lambda: self.displaying_numbers(40))
        self.button_forty.place(y=290, x=250)
        # ROW NINE
        self.button_forty_one = Button(self.labelframe_buttons, text="41", font="Times 12", bg="#3986d2", width=1,
                                       command=lambda: self.displaying_numbers(41))
        self.button_forty_one.place(y=330, x=90)
        self.button_forty_three = Button(self.labelframe_buttons, text="42", font="Times 12", bg="#3986d2", width=1,
                                         command=lambda: self.displaying_numbers(42))
        self.button_forty_three.place(y=330, x=130)
        self.button_forty_four = Button(self.labelframe_buttons, text="43", font="Times 12", bg="#3986d2", width=1,
                                        command=lambda: self.displaying_numbers(43))
        self.button_forty_four.place(y=330, x=170)
        self.button_forty_four = Button(self.labelframe_buttons, text="44", font="Times 12", bg="#3986d2", width=1,
                                        command=lambda: self.displaying_numbers(44))
        self.button_forty_four.place(y=330, x=210)
        self.button_forty_five = Button(self.labelframe_buttons, text="45", font="Times 12", bg="#3986d2", width=1,
                                        command=lambda: self.displaying_numbers(45))
        self.button_forty_five.place(y=330, x=250)
        # ROW TEN
        self.button_forty_six = Button(self.labelframe_buttons, text="46", font="Times 12", bg="#3986d2", width=1,
                                       command=lambda: self.displaying_numbers(46))
        self.button_forty_six.place(y=370, x=90)
        self.button_forty_seven = Button(self.labelframe_buttons, text="47", font="Times 12", bg="#3986d2", width=1,
                                         command=lambda: self.displaying_numbers(47))
        self.button_forty_seven.place(y=370, x=130)
        self.button_forty_eight = Button(self.labelframe_buttons, text="48", font="Times 12", bg="#3986d2", width=1,
                                         command=lambda: self.displaying_numbers(48))
        self.button_forty_eight.place(y=370, x=170)
        self.button_forty_nine = Button(self.labelframe_buttons, text="49", font="Times 12", bg="#3986d2", width=1,
                                        command=lambda: self.displaying_numbers(49))
        self.button_forty_nine.place(y=370, x=210)
        # Display Sets
        self.labelframe_display_sets = LabelFrame(self.window, bg="#ebec00", width=400, heigh=450)
        self.labelframe_display_sets.place(y=120, x=580)
        # Set One
        self.label_set_one = Label(self.labelframe_display_sets, text="FIRST SET OF NUMBERS", bg="#ebec00")
        self.label_set_one.place(y=10, x=100)
        self.label_display_set_one = Label(self.labelframe_display_sets, bg="#ebec00")
        self.label_display_set_one.place(y=40, x=110)
        # Set Two
        self.label_set_two = Label(self.labelframe_display_sets, text="SECOND SET OF NUMBERS", bg="#ebec00")
        self.label_set_two.place(y=70, x=100)
        self.label_display_set_two = Label(self.labelframe_display_sets, bg="#ebec00")
        self.label_display_set_two.place(y=100, x=110)
        # Set Three
        self.label_set_two = Label(self.labelframe_display_sets, text="THIRD SET OF NUMBERS", bg="#ebec00")
        self.label_set_two.place(y=130, x=100)
        self.label_display_set_three = Label(self.labelframe_display_sets, bg="#ebec00")
        self.label_display_set_three.place(y=160, x=110)
        # Generating Lotto Numbers
        self.button_display_lotto_numbers = Button(self.labelframe_display_sets, bg="#ebec00", text="DISPLAY LOTTO "
                                                                                                    "NUMBERS",
                                                   command=self.display_lotto_numbers)
        self.button_display_lotto_numbers.place(y=200, x=90)
        # Displaying Prizes
        self.button_display_prizes = Button(self.labelframe_display_sets, bg="#ebec00", text="DISPLAY PRIZES",
                                            command=self.display_prizes)
        self.button_display_prizes.place(y=260, x=110)
        # buttons
        self.button_play_again = Button(self.window, text="PLAY AGAIN", font="Times 12", bg="#ebec00",
                                        command=self.play)
        self.button_play_again.place(y=580, x=250)
        self.button_cash_out = Button(self.window, text="CASH OUT", font="Times 12", bg="#ebec00",
                                      command=self.cash_out)
        self.button_cash_out.place(y=580, x=485)
        self.button_exit = Button(self.window, text="EXIT", font="Times 12", bg="#ebec00",
                                  command=self.exit_button)
        self.button_exit.place(y=580, x=750)
        # FOOTER
        self.labelframe_footer = LabelFrame(self.window, bg="#ebec00", width=200, heigh=100)
        self.labelframe_footer.pack(fill="both", side=BOTTOM)
        # runs screen
        self.window.mainloop()

    # Function for each button
    def display_lotto_numbers(self):
        label_display_lottoNumbers = Label(self.labelframe_display_sets, text=self.my_winning_list)
        label_display_lottoNumbers.place(y=235, x=130)

    def display_prizes(self):
        label_first_set_winning = Label(self.labelframe_display_sets, text="Winnings From Set One ", bg="#ebec00")
        label_first_set_winning.place(y=300, x=10)
        label_second_set_winning = Label(self.labelframe_display_sets, text="Winnings From Set Two ", bg="#ebec00")
        label_second_set_winning.place(y=350, x=10)
        label_third_set_winning = Label(self.labelframe_display_sets, text="Winnings From Set Three ", bg="#ebec00")
        label_third_set_winning.place(y=400, x=10)

    def displaying_numbers(self, num):
        if len(self.my_list_one) < 6 and num not in self.my_list_one:
            self.my_list_one.append(num)
            self.label_display_set_one.config(text=str(self.my_list_one))
        elif len(self.my_list_two) < 6 and len(self.my_list_one) == 6 and num not in self.my_list_two and num not in \
                self.my_list_one:
            self.my_list_two.append(num)
            self.label_display_set_two.config(text=str(self.my_list_two))
        elif len(self.my_list_three) < 6 and len(self.my_list_two) == 6 and len(self.my_list_one) == 6 and num not in\
                self.my_list_three and num not in self.my_list_two and num not in self.my_list_one:
            self.my_list_three.append(num)
            self.label_display_set_three.config(text=str(self.my_list_three))

    # Functions for buttons
    def play(self):
        pass

    def cash_out(self):
        self.window.destroy()
        import claiming_prizes

    def exit_button(self):
        self.window.destroy()


# Runs Login Screen
Main()
