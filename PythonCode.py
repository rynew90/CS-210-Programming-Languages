import re
import string
import os


def itemList():
    #print("Hello from python!")
    grocFile = open("GroceryList.txt", "r")
    totalList = dict()

    for line in grocFile:

        words = line.split()

        for word in words:
            if word in totalList:
                totalList[word] = totalList[word] + 1

            else:
                totalList[word] = 1

    for key in list(totalList.keys()):
        print(key, ":", totalList[key])

    grocFile.close()
        
def printItemNum(v):
    grocFile = open("GroceryList.txt", "r")
    item = grocFile.read()

    numTimes = item.count(v)
    print (v, ":", numTimes)

    grocFile.close()


def createHistogram():
    grocFile = open("GroceryList.txt", "r")
    totalList = dict()

    with open("frequency.dat", "w") as newFile:
        for line in grocFile:

            words = line.split()
        
            for word in words:

                if word in totalList:
                    totalList[word] = totalList[word] + "*"
                
                else:
                    totalList[word] = "*"

        for key in list(totalList.keys()):
            newFile.writelines(key + " " + totalList[key] + "\n")

    grocFile.close()
            

    
