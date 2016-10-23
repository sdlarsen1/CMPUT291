import hashlib as hl
import os

'''
Login function appears upon starting application.
'''


def login(cursor):
    os.system('clear')
    result = None
    while result == None:
        print "Welcome to the hospital database!"
        usr = raw_input("Input username >").lower()
        pas = raw_input("Input password >")

        # fetch hashed password, then verify
        cursor.execute('''
                        SELECT password
                        FROM staff
                        WHERE login = ?; ''', (usr,))

        passResult = cursor.fetchone()
        hash = passResult[0]
        hashPass = hl.sha224(pas)

        if hash.digest() == hashPass.digest():
            cursor.execute('''
                            SELECT staff_id
                            FROM staff
                            WHERE login = ?
                            AND password = ?; ''', (usr, pas,))

            result = cursor.fetchone()
        else:
            print "Invalid password!"

        if result == None:
            os.system('clear')
            print "Invalid login!"

    staffID = result[0]
    return staffID


def logout():
    return 0