import sqlite3
from parser import parse


def main():
    database = raw_input("Enter name of .db file >")
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    done = False
    while not done:
        inTable = raw_input("Enter name of input table or q to quit >")

        if inTable == 'q':
            break

        inFD = raw_input("Enter name of FD table or q to quit >")
        parse(inTable, inFD, cursor)


if __name__ == "__main__":
    main()