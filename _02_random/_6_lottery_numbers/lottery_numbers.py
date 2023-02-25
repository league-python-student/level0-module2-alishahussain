import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    lotterynum= ''
    # TODO 1) Get 6 random numbers to put on your lottery ticket
    for i in range (6):
        lottery = random.randint(1,100)
        lotterynum=lotterynum+ str(lottery)+ ' '
    # TODO 2) Display the selected numbers to the user in a pop-up

    messagebox.showinfo(title='lottery ticket!', message=lotterynum)
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
