import sqlite3
import hashlib as hl

'''
Functions within this file insert, remove, and update users in the staff table.
'''


def addUser(cursor):
    id = raw_input("Enter staff ID >")
    role = raw_input("Enter role (D, N, A) >").upper()
    name = raw_input("Enter the full name of the person you would like to add >")
    username = raw_input("Enter desired username >")
    password = raw_input("Enter desired password >")
    passwordConf = raw_input("Re-enter password to confirm >")

    if password == passwordConf:

        hashPass = hl.sha224(password)

        cursor.execute('''
                        INSERT INTO staff VALUES
                        (?,?,?,?,?);''', (id, role, name, username, hashPass,))


def main():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()

    addUser(cursor)


if __name__ == "__main__":
    main()
