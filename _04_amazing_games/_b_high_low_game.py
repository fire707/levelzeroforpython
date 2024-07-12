from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)

    # 2. Print out the random variable that you made in step #1
    print(random_num)

    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range(10):

        dig=simpledialog.askstring(title='Greeter',prompt="Give me a guess")

    # 5. If the guess is correct
        if dig=='5':
            messagebox.showinfo(message="won")
            syst.exit(0)


            # 6. Win. Use 'sys.exit(0)' to end the program

        # 7. if the guess is high
        if dig>'5':
            messagebox.showinfo(message="you guess to high")
            # 8. Tell them it's too high

        # 9. Else if the guess is low
        if dig<'5':
            messagebox.showinfo(message="you guessed to low")


            # 10. Tell them it's too low

    #11. Outside of the loop, tell the user they lost
messagebox.showinfo(message="I guess you lost")

window.mainloop()
