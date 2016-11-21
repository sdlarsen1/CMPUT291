# contains code for 3nf conversion
def minCover(inFDs):
    cover = []
    for dep in inFDs:  # step 1
        for i in range(len(dep[1])):  # split
            cover.append((dep[0], dep[1][i]))
    print "step 1\n", cover

    for i in range(len(cover)): # step 2
        for j in range(i+1, len(cover)):
            if cover[i][1] == cover[j][1]:
                if cover[i][0] in cover[j][0]:
                    cover.remove(cover[j])
                elif cover[j][0] in cover[i][0]:
                    cover.remove(cover[i])
    print "step 2\n", cover

    for fd in cover:  # step 3
        cover.remove(fd)
        closure = makeClosure(cover, fd[0])
        if fd[1] not in closure:
            cover.append(fd)

    print "step 3\n", cover
    return cover


def makeClosure(cover, start):
    print "got to closure"
    closure = start
    old = []

    while closure != old:
        old = closure
        for fd in cover:
            if (fd[0] in closure) and (fd[1] not in closure):
                closure.add(fd[1])

    return closure


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


def convert3nf(inRows, inFDs, cursor):
    print "these are the FDs\n", inFDs
    # make the schema
    cover = minCover(inFDs)  # step 1
    # parts = partition(cover)  # step 2



