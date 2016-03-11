#!/usr/bin/python

def answer(minions):
    #for each minion, determine their prob/minute
    returnList = []; probList = []
    for minion in enumerate(minions):
        probList.append([(minion[1][0]+0.0)/((minion[1][1]+0.0)/(minion[1][2]+0.0)),minion[0]])
    probList.sort()
    for i in probList:
        returnList.append(i[1])
    return returnList

print answer([[390, 185, 624],[686, 351, 947],[276, 1023, 1024],[199,148,250]])
