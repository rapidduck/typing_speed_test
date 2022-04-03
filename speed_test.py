from tkinter import messagebox
import random
import time
from math import floor
from tkinter import *

with open("words_alpha.txt") as r:
    ALL_WORDS = [line.strip() for line in r.readlines()]

FONT = "Arial"

class Test:

    def __init__(self):
        self.start_time = None
        self.single_word_time_start = None

        self.correct_words = 0

        self.current_word = ""

        self.window = Tk()
        self.window.title("Typing speed test")
        self.window.geometry("600x400")
        self.window.config(pady=40)

        Label(self.window, text="Are you Killua in typing?", font=(FONT, 30)).pack()

        self.typing_examples = Label(self.window, text="Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum ",
                                font=(FONT, 20), justify=CENTER, bg="white", relief="groove", width=30, height=4,
                                wraplength=400)
        self.get_new_line()
        self.typing_examples.pack(pady=15)

        Label(self.window, text="Type your text down below", font=(FONT, 12)).pack()

        entry_string = StringVar()
        entry_string.trace("w", lambda name, index, mode, sv=entry_string: self.user_typed(sv))

        user_entry = Entry(self.window, text="Input your text here", font=(FONT, 20), justify=CENTER, width=30,
                           textvariable=entry_string)
        user_entry.pack()

        self.current_wpm = Label(self.window, text="", font=(FONT, 15))
        self.current_wpm.pack(pady=10)

    def end_wpm(self):
        elapsed_minutes = (time.time() - self.start_time) / 60
        wpm = floor(self.correct_words / elapsed_minutes)
        messagebox.showinfo(title="Time's up!", message=f"Your average WPM is {wpm}.")

    def show_current_wpm(self):
        elapsed_time = (time.time() - self.single_word_time_start) / 60
        current_wpm = floor(1 / elapsed_time)
        self.current_wpm.config(text=f"{current_wpm} WPM")

    def user_typed(self, string_var):
        if self.start_time is None:
            self.start_time = time.time()

        if time.time() - self.start_time > 10:
            self.end_wpm()

        user_text = string_var.get()
        try:
            if len(user_text) == 1 and self.single_word_time_start is None:
                self.single_word_time_start = time.time()

            if user_text[-1] == " ":
                print(f"User wrote a word: {user_text}")
                string_var.set("")
                if user_text.strip() == self.current_word:
                    self.correct_words += 1
                    print(f"is correct on {self.current_word}")
                self.get_new_line()
                self.show_current_wpm()
                self.single_word_time_start = time.time()

        except IndexError:
            print(f"missing -1 in '{string_var}'")

    def get_new_line(self):
        self.current_word = random.choice(ALL_WORDS)
        self.typing_examples.config(text=self.current_word)
