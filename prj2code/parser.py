# File contains to read table and collect FDs
def getInput(inTable, inFD, cursor):
    cursor.execute('''
                    SELECT * FROM Input_R1;''')

    inRows = []
    temp = cursor.fetchall()
    for row in temp:
        inRows.append(row)

    cursor.execute('''
                    SELECT * FROM Input_FDs_R1;''')

    inFDs = []
    temp = cursor.fetchall()
    for row in temp:
        inFDs.append(row)

    return inRows, inFDs