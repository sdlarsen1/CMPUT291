from LogInOut import logout
from prettytable import PrettyTable
import os


# Commands for administrative staff
def adminCommands(cursor):

    loggedOut = False

    while not loggedOut:

        os.system("clear")
        choice = int(raw_input('''Type integer value of desired task:
                            1. Show prescriptions.
                            2. Show amount prescribed by category.
                            3. Search for prescribed drugs by diagnosis.
                            4. Search for diagnoses by drug.
                            5. Log out\n'''))

        os.system('clear')

        # perform task 1
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

            # format output
            table = PrettyTable()
            table.padding_width = 1
            table._set_field_names(["Doctor Name", "Drug Name", "Total Amount"])
            for r in rows:
                table.add_row([r[0], r[1], r[2]])
            print table

            raw_input("Press Enter to go back to menu.")  # return to menu

        # perform task 2
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
                            GROUP BY d.category;''', (start_date, end_date,))
            rows = cursor.fetchall()

            # format output
            table = PrettyTable()
            table.padding_width = 1
            table._set_field_names(["Category", "Total Amount"])
            for r in rows:
                table.add_row([r[0], r[1]])
            print table

            raw_input("Press Enter to go back to menu.")  # return to menu

        # perform task 3
        elif choice == 3:
            diagnosis = raw_input("What is the diagnosis? >").lower()

            cursor.execute('''
                            SELECT m.drug_name
                            FROM medications m, diagnoses d
                            WHERE m.hcno = d.hcno
                            AND JULIANDAY(m.mdate) > JULIANDAY(d.ddate)
                            AND lower(d.diagnosis) = ?
                            GROUP BY m.drug_name
                            ORDER BY COUNT(*);''', (diagnosis,))
            rows = cursor.fetchall()

            # format output
            table = PrettyTable()
            table.padding_width = 1
            table._set_field_names(["Drug"])
            for r in rows:
                table.add_row([r[0]])
            print table

            raw_input("Press Enter to go back to menu.")  # return to menu

        # perform task 4
        elif choice == 4:
            drug = raw_input("What drug are you interested in? >").lower()

            cursor.execute('''
                            SELECT d.diagnosis
                            FROM diagnoses d, medications m
                            WHERE m.hcno = d.hcno
                            AND JULIANDAY(d.ddate) < JULIANDAY(m.mdate)
                            AND lower(m.drug_name) = ?
                            GROUP BY d.diagnosis
                            ORDER BY avg(m.amount);''', (drug,))
            rows = cursor.fetchall()

            # format output
            table = PrettyTable()
            table.padding_width = 1
            table._set_field_names(["Diagnosis"])
            for r in rows:
                table.add_row([r[0]])
            print table

            raw_input("Press Enter to go back to menu.")  # return to menu

        # else logout
        else:
            loggedOut = logout()

    os.system("clear")
    print "Goodbye!"
