#
# contains code for 3nf conversion
#


# determine the min cover
def minCover(inFDs):
    cover = []
    for dep in inFDs:  # step 1 to find min cover
        for i in range(len(dep[1])):  # split
            cover.append((dep[0], dep[1][i]))

    for i in range(len(cover)): # step 2 to find min cover
        for j in range(i+1, len(cover)):
            if cover[i][1] == cover[j][1]:
                if cover[i][0] in cover[j][0]:
                    cover.remove(cover[j])
                elif cover[j][0] in cover[i][0]:
                    cover.remove(cover[i])

    for fd in cover:  # step 3 to find min cover
        cover.remove(fd)
        closure = makeClosure(cover, fd[0])
        if fd[1] not in closure:
            cover.append(fd)

    return cover


# find the closure
def makeClosure(cover, start):
    closure = set()
    old = []

    for char in start:
        closure.add(char)

    while closure != old:
        old = closure
        for fd in cover:
            leftInClosure = True
            rightInClosure = True

            for char in fd[0]:
                if char not in closure:
                    leftInClosure = False

            for char in fd[1]:
                if char not in closure:
                    rightInClosure = False

            if leftInClosure and not rightInClosure:
                for char in fd[1]:
                    closure.add(char)

    return closure


# create the partitions of the min cover
def partition(cover):
    parts = []

    for i in range(len(cover)):
        inList = False

        for list in parts:
            if cover[i] in list:
                inList = True
        if not inList:
            parts.append([cover[i]])

        for j in range(i+1, len(cover)):
            if cover[i][0] == cover[j][0]:
                for list in parts:
                    if list[0][0] == cover[j][0]:
                        list.append(cover[j])
    return parts


# creates the tables based on the partition
def makeTable(part, cursor, inTable):
    elements = []
    keyList = []
    for char in part[0][0]:
        elements.append(char)
        keyList.append(char)
    for fd in part:
        elements.append(fd[1])

    name = "Output"+inTable+'_'+''.join(elements)
    fdName = "Output_FDs"+inTable+'_'+''.join(elements)
    attStr = ','.join(elements)
    keyStr = ','.join(keyList)

    cursor.execute('''
                    CREATE TABLE %s (%s, PRIMARY KEY (%s));''' %(name, attStr, keyStr))

    cursor.execute('''
                    CREATE TABLE %s (LHS, RHS);''' %(fdName))

    for fd in part:
        cursor.execute('''
                        INSERT INTO %s VALUES (%s, %s);''' %(fdName, "'"+fd[0]+"'", "'"+fd[1]+"'"))

    return elements


# populates the new tables with the input data
def populateTable(elements, inRows, cursor, fdDict, inTable):
    # this populates the table
    name = "Output"+inTable+'_'+''.join(elements)

    for row in inRows:
        valueStr = ''
        for element in elements:
            valueStr += "'" + str(row[fdDict[element]]) + "'" + ','
        valueStr = valueStr[:-1]

        try:
            cursor.execute('''
                        INSERT INTO %s VALUES (%s)''' %(name, valueStr))
        except Exception, e:
            print e


# find the super key of the relation
def findSuper(listElem, potKey, cover):
    B = []
    for i in range(len(potKey)):
        char = potKey[i]
        potKey.remove(char)
        if len(listElem) == len(makeClosure(cover, potKey)):
            # print "1st if", potKey
            for element in findSuper(listElem, potKey, cover):
                B.append(element)
            potKey.insert(i, char)
        else:
            # print "else", potKey
            potKey.insert(i, char)
    return B+[potKey]


# makes total list of all table elements
def combineElements(elements):
    total = []
    for i in range(len(elements)):
        for j in range(len(elements[i])):
            if elements[i][j] not in total:
                total.append(elements[i][j])
    return total


# main function for converting input data into 3nf
def convert3nf(inRows, inFDs, cursor, conn, fdDict, inTable):
    # make the schema
    cover = minCover(inFDs)  # step 1, find min cover
    parts = partition(cover)  # step 2, create partition

    #  step 3, make the tables
    elements = []  # multi-d list of attributes for each output table
    for i in range(len(parts)):
        elements.append(makeTable(parts[i], cursor, inTable))

    # step 4, find a superkey
    foundSuper = False
    for part in parts:
        if len(inRows[0]) == len(makeClosure(cover, part[0][0])):
            foundSuper = True
    if not foundSuper:
        superKeys = findSuper(combineElements(elements), combineElements(elements), cover)
        print min(superKeys)

    # after making table, give user the option to populate them
    choice = str(raw_input("Would you like to populate the tables?\n1. Yes\n2. No\n"))
    if choice == '1':
        # populate each table
        for i in range(len(parts)):
            populateTable(elements[i], inRows, cursor, fdDict, inTable)
            conn.commit()
    else:
        # quit
        return
