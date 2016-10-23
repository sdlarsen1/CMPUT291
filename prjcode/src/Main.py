import sqlite3
import os
from Admin import adminCommands
from LogInOut import login

'''
Function to get role.
'''


def getRole(cursor, staffID):
    cursor.execute('''
                SELECT role
                FROM staff
                WHERE staff_id = ?;''', (staffID,))
    result = cursor.fetchone()
    role = result[0]
    return role


'''
This is the main function.
'''


def main():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()

    staffID = login(cursor)
    os.system('clear')
    role = getRole(cursor, staffID)

    if role == 'D':
        return 0

    elif role == 'N':
        return 0

    elif role == 'A':
        # functions for admin commands
        adminCommands(cursor)


if __name__ == "__main__":
    main()
