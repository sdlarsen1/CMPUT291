#
# Contains functions necessary to compare two tables of FDs
#
from parser import stripper
from threenf import minCover


# get the user's data and find min cover
def getData(inTable, cursor):
    cursor.execute('''
                    SELECT * FROM %s;''' %(inTable))

    inFDs = []
    temp = cursor.fetchall()
    for row in temp:
        inFDs.append(row)

    inFDs = minCover(stripper(inFDs))
    return inFDs


# main function for compare.py
def compareFDs(cursor):
    inFD1 = raw_input("Enter the name of the first table >")
    inFD2 = raw_input("Enter the name of the second table >")
    print "Are the tables identical?"

    # compare the min cover of the FDs
    fd1 = getData(inFD1, cursor)
    fd2 = getData(inFD2, cursor)

    if len(fd1) != len(fd2):
        return False
    else:
        for i in range(len(fd1)):
            if fd1[i] not in fd2:
                return False

        for i in range(len(fd2)):
            if fd2[i] not in fd1:
                return False
        return True
