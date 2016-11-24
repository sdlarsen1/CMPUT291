#
# contains code for bcnf conversion
#


# function determines if a specified FD violates BCNF
def violatesbcnf(inFDs, elements, fd):
    pass


# function populates the new tables
def populateTable():
    pass


# create new tables based on the new FDs
def makeTable():
    pass


# make a list of all elements
# inFDs is a list of tuples of the fds, ie [(LHS,RHS),(LHS,RHS),...]
def makeElements(inFDs):
    elements = []
    for i in range(len(inFDs)):
        for j in range(len(inFDs[i])):
            if inFDs[i][j] not in elements:
                elements.append(inFDs[i][j])
    return elements


# recursive BCNF converter
# inFDs is a list of tuples of the fds, ie [(LHS,RHS),(LHS,RHS),...]
# elements is a list of the elements, ie ['a','b',...]
def converter(elements, inFDs):
    for fd in inFDs:
        if violatesbcnf(inFDs, elements, fd):
            A = [[makeElements([fd]), [fd]]]
            for char in fd[1]:
                elements.remove(char)
            newFDs = []
            inFDs.remove(fd)

            for fd in inFDs:
                violatesLHS = False
                for char in fd[0]:
                    if char not in elements:
                        violatesLHS = True
                if violatesLHS:
                    continue

                newFD = [fd[0], '']
                for char in fd[1]:
                    if char in elements:
                        newFD[1] += char

                if len(newFD[1]) > 0:
                    newFDs.append(newFD)

            for relation in converter(elements, newFDs):
                A.append(relation)
            return A


# main function for convertbcnf
def convertbcnf(inRows, inFDs, cursor, conn, fdDict, inTable):

    elements = makeElements(inFDs)  # get elements

    # step 1, find a violation of BCNF
    for i in range(len(inFDs)):
        fd = inFDs.pop(i)
        if violatesbcnf(inFDs, elements, fd):
            # do something
            pass
        else:
            inFDs.insert(i, fd)

    # step 2, make the schema (?)
    # TODO

