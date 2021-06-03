from tkinter import *
from tkinter import messagebox

root = Tk()

root.config(bg="Dark Slate grey")

heading = Label(root,text="Please enter amount in years")
heading.place(x=10,y=0)

amount_entry = Entry(root)
amount_entry.place(x=20,y=30)

def amount():

    try:

        if int(amount_entry.get()) >= 3000:
            messagebox.showinfo(title=None,message="Congratulations! You qualify to go to Malaysia")
        else:
            raise ValueError

    except:
        messagebox.showerror(title=None,message="Please deposit more funds to this excursion")

def exit():
    root.destroy()


amount_btn = Button(root, text="Check qualification", command=amount)
amount_btn.place(x=20, y=60)

exit_btn = Button(root, text="exit", command=exit)
exit_btn.place(x=20,y=100)


root.mainloop()
