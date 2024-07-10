from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
    
    # Make a new window variable, window = Tk()
window=Tk()
    
    # Hide the window using the window's .withdraw() method
window.withdraw()
    
    # 1. Ask the user if they know how to write code.
pow=simpledialog.askstring(title='Greeter',prompt="can you write code")
    
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.
if pow=='yes':
    messagebox.showinfo(message="you will rule the world")


    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
if pow=='no':
    messagebox.showinfo(message="Join the leauge")
    
    # Run the window's .mainloop() method'
window.mainloop()
