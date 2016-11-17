import sqlite3
from parser import getInput
from threenf import convert3nf


def main():
    database = raw_input("Enter name of .db file >")
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute('''
                    SELECT COUNT(*) FROM SQLITE_MASTER;''')
    nTables = cursor.fetchone()
    nTables = (nTables[0])/2  # account for input table + FD table

    i = 0
    while i < nTables:  # loop for multiple tables within db, subject to change condition
        inTable = None #raw_input("Enter name of input table or q to quit >")

        if inTable == 'q':  # break from loop if user wishes to quit
            break

        inFD = None #raw_input("Enter name of FD table >")
        inRows, inFDs = getInput(inTable, inFD, cursor)

        choice = raw_input("Please choose one of the following:\n1. Convert to BCNF\n2. Convert to 3NF\n")
        if choice == '1':
            # convert to BCNF
            pass
        elif choice == '2':
            # convert to 3nf
            convert3nf(inFDs)
            pass
        else:
            #quit
            pass


        i += 1

if __name__ == "__main__":
    main()
