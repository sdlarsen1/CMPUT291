import hashlib as hl
import os


# Login function appears upon starting application. Called from Main.
def login(cursor):
    os.system('clear')
    result = None
    print "Welcome to the hospital database!"
    while result is None:

        usr = raw_input("Input username >").lower()
        pas = raw_input("Input password >")

        # fetch hashed password, then verify
        cursor.execute('''
                        SELECT password
                        FROM staff
                        WHERE login = ?; ''', (usr,))

        passResult = cursor.fetchone()
        password = passResult[0]
        hashPass = hl.sha224(pas)

        if password.digest() == hashPass.digest():  # verify password
            cursor.execute('''
                            SELECT staff_id
                            FROM staff
                            WHERE login = ?
                            AND password = ?; ''', (usr, pas,))

            result = cursor.fetchone()
        else:
            print "Invalid password!"

        if result is None:
            os.system('clear')
            print "Invalid login!"

    staffID = result[0]
    return staffID


# Function to logout, returns True
def logout():
    return True


# Function to get user's role after logging in
def getRole(cursor, staffID):
    cursor.execute('''
                SELECT role
                FROM staff
                WHERE staff_id = ?;''', (staffID,))
    result = cursor.fetchone()
    role = result[0]
    return role
