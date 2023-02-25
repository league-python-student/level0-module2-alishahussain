import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    for i in range (10):
        random_number = random.randint(1, 5)

        print(random_number)

    # TODO 1) Use each value of random_number to give the user a random compliment

        if random_number == 1:
            messagebox.showinfo(title='comp1',message='ur so pretty')
        if random_number == 2:
            messagebox.showinfo(title='comp2',message='i love uuu')
        if random_number == 3:
            messagebox.showinfo(title='comp3',message='are u a model?')
        if random_number == 4:
            messagebox.showinfo(title='comp4',message='i love ur voice')
        if random_number == 5:
            messagebox.showinfo(title='comp5',message='i kinda love u ')
    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
