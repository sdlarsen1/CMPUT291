import sqlite3, os

def login(cursor):
    os.system('clear')
    result = None
    while (result == None):
        usr = raw_input("Input username >")
        pas = raw_input("Input password >")

        # password should be hashed in here

        cursor.execute('''
                        SELECT staff_id
                        FROM staff
                        WHERE login = ?
                        AND password = ?; ''', (usr, pas,))

        result = cursor.fetchone()

        if result == None:
            os.system('clear')
            print "Invalid login"

    staffID = result[0]
    return staffID

def getRole(cursor, staffID):
    cursor.execute('''
                SELECT role
                FROM staff
                WHERE staff_id = ?;''', (staffID,))
    result = cursor.fetchone()
    role = result[0]
    print role
    return role

def adminCommands(cursor):
    choice = int(raw_input('''Type integer of desired task\n
                        1. Perform task 1\n
                        2. Perform task 2\n
                        3. Perform task 3\n
                        4. Perform task 4\n
                        5. Log out\n'''))

    if choice == 1:
        print "Specify time periods in YYYY-MM-DD"
        start_time = raw_input("Specify starting time >")
        end_time = raw_input("Specify ending time >")

        cursor.execute('''
                        SELECT s.name, m.drug_name, sum(m.amount * (julianday(m.end_med) - julianday(m.start_med)))
                        FROM medications m, staff s
                        WHERE s.staff_id = m.staff_id
                        AND julianday(m.start_med) > julianday(?)
                        AND julianday(m.end_med) < julianday(?)
                        GROUP BY s.name, m.drug_name;''', (start_time, end_time,))
        rows = cursor.fetchall()
        print rows

    elif choice == 2:

    elif choice == 3:

    elif choice == 4:

    else:
        #logout


def main():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()

    staffID = login(cursor)
    os.system('clear')
    role = getRole(cursor, staffID)

    if role == 'D':

    elif role == 'N':

    elif role == 'A':
        # functions for admin commands


main()
