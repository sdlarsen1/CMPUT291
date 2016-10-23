import sqlite3
'''
Functions within this file insert, remove, and update users in the staff table.
'''

def addUser(cursor):
    staff_id = raw_input("Enter staff ID >")
    role = raw_input("Enter role (D, N, A) >")
    name = raw_input("Enter the full name of the person you would like to add >")
    username = raw_input("Enter desired username >")
    password = raw_input("Enter desired password >")
    passwordConf = raw_input("Re-enter password >")

    if password == passwordConf:
        return 0


def main():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()

    

if __name__ == "__main__":
    main()
