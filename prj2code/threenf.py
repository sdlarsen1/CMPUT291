# contains code for 3nf conversion
def minCover(inFDs):
    cover = []
    for dep in inFDs:  # step 1
        for i in range(len(dep[1])):  # split
            cover.append((dep[0], dep[1][i]))

    for i in range(len(cover)): # step 2
        for j in range(i+1, len(cover)):
            if cover[i][1] == cover[j][1]:
                if cover[i][0] in cover[j][0]:
                    cover.remove(cover[j])
                elif cover[j][0] in cover[i][0]:
                    cover.remove(cover[i])

    



def convert3nf(inRows, inFDs, cursor):
    minCover(inFds)