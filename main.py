# Author : Gideon Daniels
# Github :
# Replit :
# NOTES : - playing sound when button is clicked slows down program
# import modules
from tkinter import *
from tkinter import messagebox
import random

import read_write_to_file
from read_write_to_file import writing_file
from playsound import playsound


class Main:
    def __init__(self):
        # create instance of frame
        self.window = Tk()
        self.winnings = 0
        # position set for widgets
        self.button_posx = 20
        self.button_posy = 20
        self.label_posx = 100
        self.label_posy = 20
        # index counter for widgets
        self.count_buttons = 0
        self.count_labels_set_one = 0
        self.count_labels_set_two = 0
        self.count_labels_set_three = 0
        # List
        # list used to store objects
        self.buttons = []
        self.labels_set_one = []
        self.labels_set_two = []
        self.labels_set_three = []
        self.labels_set_lotto_numbers = []
        # list used to store numbers // will be used in for final results
        self.set_list_one = []
        self.set_list_two = []
        self.set_list_three = []
        self.set_lotto_draw = []
        # counter used to iterate to next label index
        self.counter_one = 0
        self.counter_two = 0
        self.counter_three = 0
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
        self.labelframe_buttons = LabelFrame(self.window, bg="#ebec00", width=325, heigh=320)
        self.labelframe_buttons.place(y=200, x=100)
        # Display buttons within frames
        # creates 49 buttons
        for x in range(1, 50):
            self.button = Button(self.labelframe_buttons, text=str(x), width=3, font="12", bg="#3986d2", padx=2)
            self.buttons.append(self.button)
            self.buttons[self.count_buttons].place(x=self.button_posx, y=self.button_posy)
            self.count_buttons += 1
            self.button_posx += 40
            if self.button_posx == 300:
                self.button_posy += 40
                self.button_posx = 20
        # configure each button to a command //
        self.buttons[0].config(command=lambda: self.button_clicked(1))
        self.buttons[1].config(command=lambda: self.button_clicked(2))
        self.buttons[2].config(command=lambda: self.button_clicked(3))
        self.buttons[3].config(command=lambda: self.button_clicked(4))
        self.buttons[4].config(command=lambda: self.button_clicked(5))
        self.buttons[5].config(command=lambda: self.button_clicked(6))
        self.buttons[6].config(command=lambda: self.button_clicked(7))
        self.buttons[7].config(command=lambda: self.button_clicked(8))
        self.buttons[8].config(command=lambda: self.button_clicked(9))
        self.buttons[9].config(command=lambda: self.button_clicked(10))
        self.buttons[10].config(command=lambda: self.button_clicked(11))
        self.buttons[11].config(command=lambda: self.button_clicked(12))
        self.buttons[12].config(command=lambda: self.button_clicked(13))
        self.buttons[13].config(command=lambda: self.button_clicked(14))
        self.buttons[14].config(command=lambda: self.button_clicked(15))
        self.buttons[15].config(command=lambda: self.button_clicked(16))
        self.buttons[16].config(command=lambda: self.button_clicked(17))
        self.buttons[17].config(command=lambda: self.button_clicked(18))
        self.buttons[18].config(command=lambda: self.button_clicked(19))
        self.buttons[19].config(command=lambda: self.button_clicked(20))
        self.buttons[20].config(command=lambda: self.button_clicked(21))
        self.buttons[21].config(command=lambda: self.button_clicked(22))
        self.buttons[22].config(command=lambda: self.button_clicked(23))
        self.buttons[23].config(command=lambda: self.button_clicked(24))
        self.buttons[24].config(command=lambda: self.button_clicked(25))
        self.buttons[25].config(command=lambda: self.button_clicked(26))
        self.buttons[26].config(command=lambda: self.button_clicked(27))
        self.buttons[27].config(command=lambda: self.button_clicked(28))
        self.buttons[28].config(command=lambda: self.button_clicked(29))
        self.buttons[29].config(command=lambda: self.button_clicked(30))
        self.buttons[30].config(command=lambda: self.button_clicked(31))
        self.buttons[31].config(command=lambda: self.button_clicked(32))
        self.buttons[32].config(command=lambda: self.button_clicked(33))
        self.buttons[33].config(command=lambda: self.button_clicked(34))
        self.buttons[34].config(command=lambda: self.button_clicked(35))
        self.buttons[35].config(command=lambda: self.button_clicked(36))
        self.buttons[36].config(command=lambda: self.button_clicked(37))
        self.buttons[37].config(command=lambda: self.button_clicked(38))
        self.buttons[38].config(command=lambda: self.button_clicked(39))
        self.buttons[39].config(command=lambda: self.button_clicked(40))
        self.buttons[40].config(command=lambda: self.button_clicked(41))
        self.buttons[41].config(command=lambda: self.button_clicked(42))
        self.buttons[42].config(command=lambda: self.button_clicked(43))
        self.buttons[43].config(command=lambda: self.button_clicked(44))
        self.buttons[44].config(command=lambda: self.button_clicked(45))
        self.buttons[45].config(command=lambda: self.button_clicked(46))
        self.buttons[46].config(command=lambda: self.button_clicked(47))
        self.buttons[47].config(command=lambda: self.button_clicked(48))
        self.buttons[48].config(command=lambda: self.button_clicked(49))

        # Display Results
        self.labelframe_display_results = LabelFrame(self.window, bg="#ebec00", width=400, heigh=450)
        self.labelframe_display_results.place(y=120, x=580)
        self.label_lotto_draw_heading = Label(self.labelframe_display_results, bg="#ebec00")
        self.label_lotto_draw_heading.place(y=185, x=10)
        # Create 6 labels for set one
        for x in range(0, 6):
            self.label_number = Label(self.labelframe_display_results, bg="#ebec00", text="")
            self.labels_set_one.append(self.label_number)
            self.labels_set_one[self.count_labels_set_one].place(x=self.label_posx, y=self.label_posy)
            self.label_posx += 40
            if self.count_labels_set_one >= 5:
                self.label_posy += 50  # distance between next set on y-axis
                self.label_posx = 100  # resets position on x-axis
            self.count_labels_set_one += 1
        # Create 6 labels for set two
        for x in range(0, 6):
            self.label_number = Label(self.labelframe_display_results, bg="#ebec00", text="")
            self.labels_set_two.append(self.label_number)
            self.labels_set_two[self.count_labels_set_two].place(x=self.label_posx, y=self.label_posy)
            self.label_posx += 40
            if self.count_labels_set_two >= 5:
                self.label_posy += 50  # distance between next set on y-axis
                self.label_posx = 100  # resets position on x-axis
            self.count_labels_set_two += 1

        # Create 6 labels for set three
        for x in range(0, 6):
            self.label_number = Label(self.labelframe_display_results, bg="#ebec00", text="")
            self.labels_set_three.append(self.label_number)
            self.labels_set_three[self.count_labels_set_three].place(x=self.label_posx, y=self.label_posy)
            self.label_posx += 40
            self.count_labels_set_three += 1

        # buttons
        self.button_play = Button(self.window, text="PLAY", font="Times 12", bg="#ebec00",
                                  command=self.play)
        self.button_play.place(y=300, x=480)
        self.button_play_again = Button(self.window, text="PLAY AGAIN", font="Times 12", bg="#ebec00",
                                        command=self.play_again)
        self.button_play_again.place(y=580, x=250)
        self.button_cash_out = Button(self.window, text="CASH OUT", font="Times 12", bg="#ebec00",
                                      command=self.cash_out)
        self.button_cash_out.place(y=580, x=485)
        self.button_exit = Button(self.window, text="EXIT", font="Times 12", bg="#ebec00",
                                  command=self.exit_button)
        self.button_exit.place(y=580, x=750)
        self.button_display_prizes = Button(self.window, text="DISPLAY PRIZES", font="Times 12", bg="#ebec00",
                                            command=self.display_prizes)
        self.button_display_prizes.place(y=350, x=425)
        # FOOTER
        self.labelframe_footer = LabelFrame(self.window, bg="#ebec00", width=200, heigh=100)
        self.labelframe_footer.pack(fill="both", side=BOTTOM)
        # runs screen
        self.window.mainloop()

    # Function for each button
    def button_clicked(self, num):
        self.buttons[num - 1].config(state=DISABLED)
        # Condition for set one
        if len(self.set_list_one) <= 6 and self.counter_one < 6:
            self.labels_set_one[self.counter_one].config(text=str(num), width=3, bg="#3986d2")
            self.counter_one += 1
            self.set_list_one.append(num)
            if len(self.set_list_one) == 6:
                messagebox.showinfo("INFO", "Start Choosing Second Set")
        # Condition for set two
        elif len(self.set_list_one) >= 6 and len(self.set_list_two) <= 6 and self.counter_two < 6:
            self.labels_set_two[self.counter_two].config(text=str(num), width=3, bg="#3986d2")
            self.counter_two += 1
            self.set_list_two.append(num)
            if len(self.set_list_two) == 6:
                messagebox.showinfo("INFO", "Start Choosing Third Set")
        # Condition for set three
        elif len(self.set_list_one) >= 6 and len(self.set_list_two) >= 6 and len(
                self.set_list_three) <= 6 and self.counter_three < 6:
            self.labels_set_three[self.counter_three].config(text=str(num), width=3, bg="#3986d2")
            self.counter_three += 1
            self.set_list_three.append(num)
        if len(self.set_list_three) == 6:
            messagebox.showinfo("INFO", "ALL SETS COMPLETED , PRESS PLAY")
            for y in range(len(self.buttons)):
                self.buttons[y].config(state=DISABLED)
        # playsound("button_clicked_sound.mp3")

    def display_prizes(self):
        try:
            set_prize_one = []
            set_prize_two = []
            set_prize_three = []
            label_prize_one = Label(self.labelframe_display_results, text="", bg="#3986d2")
            label_prize_two = Label(self.labelframe_display_results, text="", bg="#3986d2")
            label_prize_three = Label(self.labelframe_display_results, text="", bg="#3986d2")
            for x in self.set_lotto_draw:
                if x in self.set_list_one:
                    set_prize_one.append(x)
                elif x in self.set_list_two:
                    set_prize_two.append(x)
                elif x in self.set_list_three:
                    set_prize_three.append(x)
            # Condition for set one
            if len(set_prize_one) == 2:
                label_prize_one.config(text="You have 2 correct in set one.Your prize is R20.", )
                label_prize_one.place(x=20, y=250)
                self.winnings += 20.00
            elif len(set_prize_one) == 3:
                label_prize_one.config(text="You have 3 correct in set one.Your prize is R100.50")
                label_prize_one.place(x=20, y=250)
                self.winnings += 100.50
            elif len(set_prize_one) == 4:
                label_prize_one.config(text="You have 4 correct in set one.Your prize is R2 384")
                label_prize_one.place(x=20, y=250)
                self.winnings += 2384.00
            elif len(set_prize_one) == 5:
                label_prize_one.config(text="You have 5 correct in set one.Your prize is R8584.00")
                label_prize_one.place(x=20, y=250)
                self.winnings += 8584.00
            elif len(set_prize_one) == 6:
                label_prize_one.config(text="You have 6 correct in set one.Your prize is R10000000.00")
                label_prize_one.place(x=20, y=250)
                self.winnings += 10000000.00
            else:
                label_prize_one.config(text="YOU HAVE ZERO WINNINGS IN SET ONE. PLAY AGAIN?")
                label_prize_one.place(x=20, y=250)
            # condition winnings in set two
            if len(set_prize_two) == 2:
                label_prize_two.config(text="You have 2 correct in set two.Your prize is R20")
                label_prize_two.place(x=20, y=300)
                self.winnings += 20.00
            elif len(set_prize_two) == 3:
                label_prize_two.config(text="You have 3 correct in set two.Your prize is R100.50")
                label_prize_two.place(x=20, y=300)
                self.winnings += 100.50
            elif len(set_prize_two) == 4:
                label_prize_two.config(text="You have 4 correct in set two.Your prize is R2 384")
                label_prize_two.place(x=20, y=300)
                self.winnings += 2384.00
            elif len(set_prize_two) == 5:
                label_prize_two.config(text="You have 5 correct in set two.Your prize is R8584.00")
                label_prize_two.place(x=20, y=300)
                self.winnings += 8584.00
            elif len(set_prize_two) == 6:
                label_prize_two.config(text="You have 6 correct in set two.Your prize is R10000000.00")
                label_prize_two.place(x=20, y=300)
                self.winnings += 10000000.00
            else:
                label_prize_two.config(text="YOU HAVE ZERO WINNINGS IN SET TWO. PLAY AGAIN?")
                label_prize_two.place(x=20, y=300)
            # condition winnings in set 3
            if len(set_prize_three) == 2:
                label_prize_three.config(text="You have 2 correct in set three.Your prize is R20")
                label_prize_three.place(x=20, y=350)
                self.winnings += 20.00
            elif len(set_prize_three) == 3:
                label_prize_three.config(text="You have 3 correct in set three.Your prize is R100.50")
                self.winnings += 100.50
                label_prize_three.place(x=20, y=350)
            elif len(set_prize_three) == 4:
                label_prize_three.config(text="You have 4 correct in set four.Your prize is R2 384")
                self.winnings += 2384.00
                label_prize_three.place(x=20, y=350)
            elif len(set_prize_three) == 5:
                label_prize_three.config(text="You have 5 correct in set five.Your prize is R8584.00")
                self.winnings += 8584.00
                label_prize_three.place(x=20, y=350)
            elif len(set_prize_three) == 6:
                label_prize_three.config(text="You have 6 correct in set six.Your prize is R10000000.00")
                self.winnings += 10000000.00
                label_prize_three.place(x=20, y=350)
            else:
                label_prize_three.config(text="YOU HAVE ZERO WINNINGS IN SET THREE. PLAY AGAIN?")
                label_prize_three.place(x=20, y=350)
            if self.winnings > 0:
                playsound("winnings.mp3")
            else:
                self.button_cash_out.config(state=DISABLED)
            self.button_display_prizes.config(state=DISABLED)
            label_winnings = Label(self.labelframe_display_results, text=f"TOTAL WINNINGS : R {str(self.winnings)}",
                                   font="20", bg="#3986d2")
            label_winnings.place(x=100, y=390)
            writing_file(f"{str(self.winnings)}")
        except:
            pass

    # Functions for buttons
    def play(self):
        if len(self.set_list_three) == 6:
            posx = 200
            posy = 185
            self.label_lotto_draw_heading.config(text="LOTTO DRAW NUMBERS : ", bg="#3986d2")
            for x in range(0, 6):
                numbers = random.randint(1, 49)
                self.set_lotto_draw.append(numbers)
                label_lotto_draw = Label(self.labelframe_display_results, text=str(numbers), width=2, bg="#3986d2")
                label_lotto_draw.place(x=posx, y=posy)
                posx += 30
            print(self.set_lotto_draw)
            self.button_play.config(state=DISABLED)
        else:
            messagebox.showwarning("WARNING", "PLEASE SELECT ALL SETS FIRST")

    def play_again(self):
        self.window.destroy()
        import main

    def cash_out(self):
        f = open("winnings.txt", "w+")
        try:
            f.write(str(self.winnings))
            messagebox.showinfo("BANK DETAILS NEEDED", "WE WILL NEED YOUR BANKING DETAILS")
            self.window.destroy()
            import claiming_prizes
        finally:
            f.close()

    def exit_button(self):
        self.window.destroy()


# Runs Login Screen
Main()
