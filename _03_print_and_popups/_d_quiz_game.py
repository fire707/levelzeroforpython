from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
    
    # Make a new window variable, window = Tk()
window=Tk()
    
    # Hide the window using the window's .withdraw() method
window.withdraw()
    
    # 1. Create a variable to hold the user's score. Set it equal to zero.
jol=0

    # ASK A QUESTION AND CHECK THE ANSWER


    #      // 2.  Ask the user a question
hag=simpledialog.askstring(title='Greeter',prompt="give me the correct number 1-5")
    
    #      // 3.  Use an if statement to check if their answer is correct
if hag==3:
        jol+1


    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
