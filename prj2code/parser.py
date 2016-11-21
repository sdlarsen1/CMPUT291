# File contains to read table and collect FDs
def stripper(input):
    for i in range(len(input)):
        hold = []
        for j in range(len(input[i])):
             hold.append(input[i][j].replace(",", ""))
        input[i] = hold
    return input


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

    inFDs = stripper(inFDs)
    # inRows = stripper(inRows)

    return inRows, inFDs