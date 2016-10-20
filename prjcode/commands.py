import sqlite3, os, hashlib as hl

def login(cursor):
    os.system('clear')
    result = None
    while (result == None):
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
        else: print "Invalid password!"

        if result == None:
            os.system('clear')
            print "Invalid login!"

    staffID = result[0]
    return staffID

def getRole(cursor, staffID):
    cursor.execute('''
                SELECT role
                FROM staff
                WHERE staff_id = ?;''', (staffID,))
    result = cursor.fetchone()
    role = result[0]
    #print role
    return role

def logout():
    # TODO

def adminCommands(cursor):
    choice = int(raw_input('''Type integer value of desired task:
                        1. Perform task 1
                        2. Perform task 2
                        3. Perform task 3
                        4. Perform task 4
                        5. Log out\n'''))

    os.system('clear')
    if choice == 1:
        print "Specify time periods in YYYY-MM-DD format"
        start_date = raw_input("Specify starting date >")
        end_date = raw_input("Specify ending date >")

        cursor.execute('''
                        SELECT s.name, m.drug_name, sum(m.amount * (JULIANDAY(m.end_med) - JULIANDAY(m.start_med)))
                        FROM medications m, staff s
                        WHERE s.staff_id = m.staff_id
                        AND julianday(m.start_med) > julianday(?)
                        AND julianday(m.end_med) < julianday(?)
                        GROUP BY s.name, m.drug_name;''', (start_date, end_date,))
        rows = cursor.fetchall()
        print rows

    elif choice == 2:
        print "Specify time periods in YYYY-MM-DD format"
        start_date = raw_input("Specify starting date >")
        end_date = raw_input("Specify ending date >")

        cursor.execute('''
                        SELECT d.category, SUM(m.amount * (JULIANDAY(m.end_med) - JULIANDAY(m.start_med)))
                        FROM medications m, drugs d
                        WHERE m.drug_name = d.drug_name
                        AND JULIANDAY(m.start_med) > JULIANDAY(?)
                        AND JULIANDAY(m.end_med) < JULIANDAY(?)
                        GROUP BY d.category;''', (end_date, start_date,))
        rows = cursor.fetchall()
        print rows

    elif choice == 3:
        diagnosis = raw_input("What is the diagnosis? >").lower()

        cursor.execute('''
                        SELECT m.drug_name
                        FROM medications m, diagnoses d
                        WHERE m.hcno = d.hcno
                        AND (m.mdate = d.ddate OR JULIANDAY(m.mdate) > JULIANDAY(d.ddate))
                        AND d.diagnosis = ?
                        GROUP BY drug_name
                        ORDER BY COUNT(*) DESC;''', (diagnosis,))
        rows = cursor.fetchall()
        print rows


    elif choice == 4:
        drug = raw_input("What drug are you interested in? >").lower()

    else:
        logout()

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

    elif role == 'N':

    elif role == 'A':
        # functions for admin commands
        adminCommands(cursor)


if __name__ == "__main__":
    main()
