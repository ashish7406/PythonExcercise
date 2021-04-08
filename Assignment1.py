def CreateFileWithName(filename):
    x= filename+" created the first file using python 3."
    with open(filename+'.txt', 'w+') as fh:
        fh.write(x)
        fh.close()

def UpdateFileName(filename):
    file1 = open(filename+'.txt', "a")
    text= "Now , {} is adding a new data to the existing file.".format(filename)
    # writing newline character
    file1.write("\n")
    file1.write(text)
'''
Viewing content of the file
'''
def ViewFileData(filename):
    with open(filename + '.txt', 'r+') as fh:
        for contenFile in fh:
            print(contenFile)

def CreatOrderFile(filename):
    listOrder=["1-56788-021 lenovo charger Raed Karim 01-03-2020","1-99923-022 HP battery John MacQueen 12-03-2020","1-23890-026 Sony HD Mary Donald 23-03-2020"]
    with open(filename+'.txt', 'w') as f:
        for item in listOrder:
            f.write("%s\n" % item)
def ViewOrderFile(filename):
    with open(filename+'.txt') as file:  # Use file to refer to the file object
        data = file.read()
        print(data)


CreateFileWithName("Ashish")
UpdateFileName("Ashish")
ViewFileData("Ashish")
CreatOrderFile("orders")
ViewOrderFile("orders")