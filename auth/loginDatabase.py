import mysql.connector
class DatabaseConnection:


    def login(username):
        db = mysql.connector.connect(
                host="localhost",
                user="efode",
                passwd="root1234",
                database="goatmentor"
            )

        mycursor = db.cursor()
        mycursor.execute(
            "SELECT first_name, last_name, email, password FROM users WHERE email = %s", (username))

        # If result, continue
        for x in mycursor:
            print(x)
            return True
