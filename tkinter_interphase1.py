from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Authentication")
root.geometry("500x500")
root.config(bg="DeepSkyBlue4")

heading= Label(root, text="Please enter your login details")
heading.pack()

user_label = Label(root, text="Enter user name")
user_label.pack()
user_entry = Entry(root)
user_entry.pack()

pass_label = Label(root, text="Enter password")
pass_label.pack()
pass_entry = Entry(root)
pass_entry.pack()


def pass_check():



    user_dict ={"001":"Mzwa","002":"Zipho","003":"Masi","004":"Thando","005":"Karabo"}
    found = False
    for i in user_dict:
        if i == user_entry.get() and user_dict[i] == pass_entry.get():
            found = True

    if found == True:
        messagebox.showinfo(title=None, message="Correct Login details")
        root.destroy()
        import Interphase_2

    else:
        messagebox.showinfo(title=None,message="Please enter correct details")


def clear():
    user_entry.delete(0,END)
    pass_entry.delete(0,END)


pass_btn = Button(root, text="Login", command=pass_check)
pass_btn.place(x=250, y=120)

clear_btn = Button(root, text="try again", command = clear)
clear_btn.place(x=250,y=170)






root.mainloop()
