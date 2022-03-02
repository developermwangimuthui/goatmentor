from tkinter import *
from tkinter import messagebox
from loginDatabase import DatabaseConnection


class Login:
    window = Tk()
    window.title("Goatmentor Login")
    window.geometry("7000x3000")

    global entry1
    global entry2

    def validateLoginForms():
        username = entry1.get()
        passwd = entry2.get()

        if username == "" and passwd == "":
            messagebox.showwarning("", "Please enter your username and password")

        # calling the function
        else:
            databaseConn = DatabaseConnection()
            databaseConn.login(username)

    Label(window, text="Email:", fg="blue").place(x=750, y=200)
    Label(window, text="Password:", fg="blue").place(x=750, y=260)

    # This is the username
    entry1 = Entry(window, bd=7)
    entry1.place(x=900, y=200)

    # This is the password
    entry2 = Entry(window, bd=7)
    entry2.place(x=900, y=260)

    # This is the login button
    Button(window, text="Login", command=validateLoginForms, height=4, width=14, bd=8, font="Monaco 10", bg="orange",
           fg="black").place(x=900, y=320)


    window.mainloop()
