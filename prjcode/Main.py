import sqlite3
import os
from Admin import adminCommands
from LogInOut import login, getRole
from TableCommands import addUser
from Doctor import doctorCommands
from Nurse import nurseCommands


# This is the main function
def main():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()

    choice = raw_input("What would you like to do?\n1. Add user\n2. Login\n")

    if choice == '1':
        addUser(cursor)
        conn.commit()

    else:
        staffID = login(cursor)
        os.system('clear')
        role = getRole(cursor, staffID)

        if role == 'D':
            # functions for doctor commands
            doctorCommands(cursor, conn, staffID)

        elif role == 'N':
            # functions for nurse commands
            nurseCommands(cursor, conn, staffID)

        elif role == 'A':
            # functions for admin commands
            adminCommands(cursor)


if __name__ == "__main__":
    main()
