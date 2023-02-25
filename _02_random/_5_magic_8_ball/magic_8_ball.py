import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    simpledialog.askstring(title='none',prompt='ask a yes/no question to the magic 8 ball')
    # Make a variable and initialize it to a random number between 0 and 3
    ball = random.randint(0,3)
    # If the random number is 0
    if ball == 0:
            messagebox.showinfo(title='none',message='yes')
        # tell the user "Yes"

    # If the random number is 1
    if ball == 1:
            messagebox.showinfo(title='none',message='no')
        # tell the user "No"

    # If the random number is 2
    if ball == 2:
            messagebox.showinfo(title='none',message='maybe u should ask google bestie')
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    if ball == 3:
            messagebox.showinfo(title='none',message='absolutely not bebs')
        # write your own answer
