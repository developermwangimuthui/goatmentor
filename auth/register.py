from tkinter import SOLID, TOP, Button, Entry, Frame, Label, Menu, StringVar, Tk
import tkinter.messagebox as tkMessageBox
import mysql.connector
from mysql.connector import Error

root = Tk()
root.title("Goat Mentor - Register Form")
width = 1200
height = 1000
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


# =======================================VARIABLES=====================================
EMAIL = StringVar()
PASS = StringVar()
CPASS = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()
ADDRESS = StringVar()
CITY = StringVar()
ZIPCODE = StringVar()
BIRTHDAY = StringVar()
PLAYERROLE = StringVar()
LANGUAGE = StringVar()

# =======================================METHODS=======================================


def Database():
    global conn, cursor
    conn = mysql.connector.connect(host='localhost',
                                         database='goatmentor',
                                         user='efode',
                                         password='root1234')
    cursor = conn.cursor()


def Exit():
    result = tkMessageBox.askquestion(
        'System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def Register():
    Database()
    if EMAIL.get == "" or PASS.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get() == ""or CITY.get() == ""or ZIPCODE.get() == ""or BIRTHDAY.get() == ""or PLAYERROLE.get() == ""or LANGUAGE.get() == "" or ADDRESS.get == "":
        lbl_result.config(
            text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `users` WHERE `email` = %s",([EMAIL.get()]))
        if cursor.fetchone() is not None:
            lbl_result.config(text="Username is already taken", fg="red")
        else:
            cursor.execute("INSERT INTO `users` (first_name, last_name, email,password,city,zipcode,birth_date,player_role,language,address) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (str(
                FIRSTNAME.get()), str(LASTNAME.get()), str(EMAIL.get()),str(PASS.get()),str(CITY.get()),str(ZIPCODE.get()),str(BIRTHDAY.get()),str(PLAYERROLE.get()),str(LANGUAGE.get()), str(ADDRESS.get())))
            conn.commit()
            FIRSTNAME.set("")
            LASTNAME.set("")
            EMAIL.set("")
            PASS.set("")
            CPASS.set("")
            CITY.set("")
            ZIPCODE.set("")
            BIRTHDAY.set("")
            PLAYERROLE.set("")
            LANGUAGE.set("")
            ADDRESS.set("")
            lbl_result.config(text="Successfully Created!", fg="green")
        cursor.close()
        conn.close()

# =====================================FRAMES====================================
TitleFrame=Frame(root, height=100, width=640, bd=1, relief=SOLID)
TitleFrame.pack(side=TOP)
RegisterFrame=Frame(root)
RegisterFrame.pack(side=TOP, pady=20)


# =====================================LABEL WIDGETS=============================
lbl_title=Label(TitleFrame, text="GOATMENTOR - Register Form",
                font=('arial', 18), bd=1, width=640)
lbl_title.pack()
lbl_firstname=Label(RegisterFrame, text="Firstname:", font=('arial', 18), bd=18)
lbl_firstname.grid(row=1)
lbl_lastname=Label(RegisterFrame, text="Lastname:", font=('arial', 18), bd=18)
lbl_lastname.grid(row=2)
lbl_email=Label(RegisterFrame, text="Email:", font=('arial', 18), bd=18)
lbl_email.grid(row=3)
lbl_city=Label(RegisterFrame, text="City:", font=('arial', 18), bd=18)
lbl_city.grid(row=4)
lbl_address=Label(RegisterFrame, text="Address:", font=('arial', 18), bd=18)
lbl_address.grid(row=5)
lbl_zipcode=Label(RegisterFrame, text="Zipcode:", font=('arial', 18), bd=18)
lbl_zipcode.grid(row=6)
lbl_birthday=Label(RegisterFrame, text="Birthday:", font=('arial', 18), bd=18)
lbl_birthday.grid(row=7)
lbl_playerrole=Label(RegisterFrame, text="Playerrole:", font=('arial', 18), bd=18)
lbl_playerrole.grid(row=8)
lbl_language=Label(RegisterFrame, text="Language:", font=('arial', 18), bd=18)
lbl_language.grid(row=9)
lbl_password=Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
lbl_password.grid(row=10)
lbl_cpassword=Label(RegisterFrame, text="Confrim Password:", font=('arial', 18), bd=18)
lbl_cpassword.grid(row=11)
lbl_result=Label(RegisterFrame, text="", font=('arial', 18))
lbl_result.grid(row=12, columnspan=2)


# =======================================ENTRY WIDGETS===========================
firstname=Entry(RegisterFrame, font=('arial', 20), textvariable=FIRSTNAME, width=15)
firstname.grid(row=1, column=1)
lastname=Entry(RegisterFrame, font=('arial', 20),textvariable=LASTNAME, width=15)
lastname.grid(row=2, column=1)
myemail=Entry(RegisterFrame, font=('arial', 20), textvariable=EMAIL, width=15)
myemail.grid(row=3, column=1)
city=Entry(RegisterFrame, font=('arial', 20),textvariable=CITY, width=15)
city.grid(row=4, column=1)
address=Entry(RegisterFrame, font=('arial', 20),textvariable=ADDRESS, width=15)
address.grid(row=5, column=1)
zipcode=Entry(RegisterFrame, font=('arial', 20),textvariable=ZIPCODE, width=15)
zipcode.grid(row=6, column=1)
birthday=Entry(RegisterFrame, font=('arial', 20),textvariable=BIRTHDAY, width=15)
birthday.grid(row=7, column=1)
playerrole=Entry(RegisterFrame, font=('arial', 20),textvariable=PLAYERROLE, width=15)
playerrole.grid(row=8, column=1)
language=Entry(RegisterFrame, font=('arial', 20),textvariable=LANGUAGE, width=15)
language.grid(row=9, column=1)
password=Entry(RegisterFrame, font=('arial', 20),textvariable=PASS, width=15,show="*")
password.grid(row=10, column=1)
cpassword=Entry(RegisterFrame, font=('arial', 20),textvariable=CPASS, width=15,show="*")
cpassword.grid(row=11, column=1)
# ========================================BUTTON WIDGETS=========================
btn_register=Button(RegisterFrame, font=('arial', 20),
                    text="Register", command=Register)
btn_register.grid(row=14, columnspan=2)
# ========================================MENUBAR WIDGETS==================================
menubar=Menu(root)
filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)


# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
