import sqlite3
import os
from parser import getInput
from threenf import convert3nf
from compare import compareFDs
from bcnf import convertbcnf


def main():
    database = raw_input("Enter name of .db file >")
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute('''
                    SELECT COUNT(*) FROM SQLITE_MASTER;''')
    nTables = cursor.fetchone()
    nTables = (nTables[0])/2  # account for input table + FD table

    initScreen = raw_input("Please select an option:\n1. Compare FD tables\n2. Normalize a table\n")

    if initScreen == '1':
        print compareFDs(cursor)

    elif initScreen == '2':
        i = 0
        while i < nTables:  # loop for multiple tables within db, subject to change condition
            inTable = raw_input("Enter name of input table or q to quit >")

            if inTable == 'q':  # break from loop if user wishes to quit
                break

            inFDtable = raw_input("Enter name of FD table >")
            inRows, inFDs, fdDict = getInput(inTable, inFDtable, cursor)

            os.system("clear")
            choice = raw_input("Please choose one of the following "
                               "(entering anything else will terminate the program):\n"
                               "1. Convert to BCNF\n2. Convert to 3NF\n")
            if choice == '1':
                # convert to BCNF
                convertbcnf(inRows, inFDs, cursor, conn, fdDict, inTable[5:])
            elif choice == '2':
                # convert to 3nf
                convert3nf(inRows, inFDs, cursor, conn, fdDict, inTable[5:])
            else:
                # quit
                return

            i += 1

if __name__ == "__main__":
    main()
