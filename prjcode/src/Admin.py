from LogInOut import logout

'''
Commands for admin staff.
'''


def adminCommands(cursor):

    choice = int(raw_input('''Type integer value of desired task:
                        1. Perform task 1
                        2. Perform task 2
                        3. Perform task 3
                        4. Perform task 4
                        5. Log out\n'''))

    os.system('clear')
    if choice == 1:
        print "Specify time periods in YYYY-MM-DD HH:MM:SS format."
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
        print "Specify time periods in YYYY-MM-DD HH:MM:SS format."
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

        cursor.execute('''
                        SELECT DISTINCT d.diagnosis
                        FROM diagnoses d, medications m
                        WHERE m.hcno = d.hcno
                        AND JULIANDAY(d.ddate) < JULIANDAY(m.mdate)
                        AND m.drug_name = ?;''', (drug,))
        rows = cursor.fetchall()
        print rows

    else:
        logout()
