'''
Create List will create computer list
'''
def createComputerList(l1):
    for i in range(5):
        addComputer=str(input("Enter computer Name"))
        l1.append(addComputer)

    with open('ComputerNames.txt', 'w') as f:
        for item in l1:
            f.write("%s\n" % item)
'''
Delete function will delete computer List
'''
def DeleteComputerList(l2,deleteComputerName):
    l2.remove(deleteComputerName)
    with open('ComputerNames.txt', 'w') as f:
        for item in l2:
            f.write("%s\n" % item)


listComputer=[]
createComputerList(listComputer)
deleteComputerName=str(input("Enter computer Name to be deleted"))
DeleteComputerList(listComputer,deleteComputerName)
