def binarySearch(alist, val):
    lowerbound = 0
    upperbound = len(alist) - 1
    middle = (lowerbound + upperbound) // 2
    found = False

    while(found == False and lowerbound <= upperbound):
        middle = (lowerbound + upperbound) // 2
        if(alist[middle] < val):
            lowerbound = middle + 1
        elif(alist[middle] > val):
            upperbound = middle - 1
        else:
            found = True
    if found == False:
        return -1
    else:
        return middle

def allPositions(alist, val):
    onepos = binarySearch(alist, val)
    listOfPositions = [onepos]
    pos = onepos + 1
    #get to the right of onepos
    while(alist[pos] == val):
        listOfPositions.append(pos)
        pos = pos + 1

    #get to the left
    pos = onepos - 1
    while(alist[pos] == val):
        listOfPositions.append(pos)
        pos -= 1

    return listOfPositions
