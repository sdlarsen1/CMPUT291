#
# File contains functions to read table and collect FDs
#


# strips input data of commas
def stripper(input):
    for i in range(len(input)):
        hold = []
        for j in range(len(input[i])):
             hold.append(input[i][j].replace(",", ""))
        input[i] = hold
    return input


# make dictionary associating each row with the FD
def makeDict(inFDs):
    attributes = []
    newDict = {}
    for fds in inFDs:
        for side in fds:
            for char in side:
                if char not in attributes:
                    attributes.append(char)
    attributes.sort()

    for i in range(len(attributes)):
        newDict[attributes[i]] = i

    return newDict


def getInput(inTable, inFD, cursor):
    cursor.execute('''
                    SELECT * FROM %s;''' %(inTable))

    inRows = []
    temp = cursor.fetchall()
    for row in temp:
        inRows.append(row)

    cursor.execute('''
                    SELECT * FROM %s;''' %(inFD))

    inFDs = []
    temp = cursor.fetchall()
    for row in temp:
        inFDs.append(row)

    inFDs = stripper(inFDs)
    fdDict = makeDict(inFDs)
    # inRows = stripper(inRows)

    return inRows, inFDs, fdDict