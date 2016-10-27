import sqlite3
import os
from Admin import adminCommands
from LogInOut import login, getRole
from TableCommands import addUser


# This is the main function
def main():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()

    choice = raw_input("What would you like to do?\n1. Add user\n2. Login\n")

    if choice == '1':
        addUser(cursor)

    else:
        staffID = login(cursor)
        os.system('clear')
        role = getRole(cursor, staffID)

        if role == 'D':
            # functions for doctor commands
            return 0

        elif role == 'N':
            # functions for nurse commands
            return 0

        elif role == 'A':
            # functions for admin commands
            adminCommands(cursor)


if __name__ == "__main__":
    main()
