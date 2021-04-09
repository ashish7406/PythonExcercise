# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Author Name:- ASHISH SHARMA (500188494)
#               KARTHIK THALLAM(500188370)

# This program performs the following  operations
# 1.	Create a file with your name and write to it this line:
# [Your name] created the first file using python 3.
# 2.	Open the previous file in question 1, and add to it this line:
# Now , [your name] is adding a new data to the existing file.
# 3.	Read the data in the file you have created in questions 1, 2 and print it out.
# 4.	Create a new file and call it scores. Write to it a few scores from the user, then print them in list format.
# 5.	Create a new file and call it “ orders”. Write to it three lines each contains information about an order like this:
# 1-56788-021 lenovo charger Raed Karim 01-03-2020
# 1-99923-022 HP battery John MacQueen 12-03-2020
# 1-23890-026 Sony HD Mary Donald 23-03-2020
# 6.	Use with keyword to iterate through the lines in question 5 and print them out.
# Do your own SEARCH for this – using with
# 7.	Go to any online-shopping website and pick any reviews from customers. Copy them into a notepad to create a text file of a few lines ( e.g. 10 lines).
# Now, create a program that split each line into a list of words. In each list, I want you to remove any of the following words (stop words) like “the” “a” “is” “are” “she”, etc, and then return the new lists.
# 8.	The output of the program should look similar to the output of a sample run shown below.


import os
import json

# Take current working directory and used in future to create files there.
path = os.path.abspath(os.getcwd()) + "//"



def write_userfile(filename):
    x= filename+" created the first file using python 3."
    with open(path+filename+'.txt', 'w+') as fh:
        fh.write(x)
        fh.close()

def update_userfileName(filename):
    file1 = open(path+filename+'.txt', "a")
    text= "Now , {} is adding a new data to the existing file.".format(filename)
    # writing newline character
    file1.write("\n")
    file1.write(text)
'''
Viewing content of the file
'''
def view_file_data(filename):
    #opening file using with keyword
    with open(path+filename + '.txt', 'r+') as fh:
        for contenFile in fh:
            print(contenFile)

def create_score_file(fileaname):
    listScore=[]
    score = int(input("How many scores do you want to enter?"))
    for i in range(score):
        score=int(input("Enter the score "+str(i+1)+" :"))
        listScore.append(score)
    print(listScore)
# It will create score file and write list content into score file.
    with open(path+fileaname + '.txt', 'w+') as scorefile:
        for line in listScore:
            scorefile.write(str(line))
            scorefile.write("\n")



def creat_order_File(filename):
    listOrder=["1-56788-021 lenovo charger Raed Karim 01-03-2020","1-99923-022 HP battery John MacQueen 12-03-2020","1-23890-026 Sony HD Mary Donald 23-03-2020"]
    with open(path+filename+'.txt', 'w') as f:
        for item in listOrder:
            f.write("%s\n" % item)


def view_order_file(filename):
    with open(filename+'.txt') as file:  # Use file to refer to the file object
        data = file.read()
        print(data)

def review_file():
    updatedreview_list = []
    stop_words = ['a', 'the', 'is', 'are', 'she']
    new_path = path + "review.txt"
    with open(new_path, "r") as file6:
        for line in file6:
            for word in line.split():
                if word not in stop_words:
                    updatedreview_list.append(word)
        print(updatedreview_list)
    file6.close()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user_name = str(input("Please enter your name: "))
    #Create file With your  Name
    write_userfile(user_name)
    #Update the content in the file
    update_userfileName(user_name)
    #View the content from the same file
    view_file_data(user_name)
    #Create Score file and print content of the list
    create_score_file("scores")
    #Create a file orders and write contents into file
    creat_order_File("orders")
    #View Orders
    view_order_file("orders")
    #Extract review file and print the contents
    review_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
