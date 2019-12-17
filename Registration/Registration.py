from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry("300x500")
root.title("Login")

def registration():
    text = Label(text = "Registration")
    text_login = Label(text = "Login:")
    reg_login = Entry()
    text_password1 = Label(text = "Password:")
    reg_password1 = Entry(show = "*")
    text_password2 = Label(text = "Confirm your password:")
    reg_password2 = Entry(show = "*")
    reg_button = Button(text = "Register", command = lambda: save())
    text.pack()
    text_login.pack()
    reg_login.pack()
    text_password1.pack()
    reg_password1.pack()
    text_password2.pack()
    reg_password2.pack()
    reg_button.pack()

    def save():
        login_password_save = {}
        login_password_save[reg_login.get()] = reg_password1.get()
        f = open("login.txt", "wb")
        pickle.dump(login_password_save, f)
        f.close()
        login()

def login():
    text_login = Label(text = "Now you can enter to the system")
    text_enter_login = Label(text = "Login:")
    enter_login = Entry()
    text_enter_password = Label(text = "Password:")
    enter_password = Entry(show = "*")
    enter_button = Button(text = "Enter", command = lambda: login_password_check())
    text_login.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_password.pack()
    enter_password.pack()
    enter_button.pack()

    def login_password_check():
        f = open("login.txt", "rb")
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_password.get() == a[enter_login.get()]:
                messagebox.showinfo("Success!", "You are in the system!")
            else:
                messagebox.showerror("Error!", "Incorrect login or password!")
        else:
            messagebox.showerror("Error!", "Incorrect login!")

registration()

root.mainloop()
