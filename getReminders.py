#!/usr/local/bin/python3

import sys
import datetime


def GetReminders():
    """This function will ask the user to enter all the tasks and reminders that the user wants to be notified about as soon as he logs in the next time."""
    response1 = input(
        "Got any tasks or reminders for the next session? \n(y/n)").lower()

    if response1 == 'n':
        print("Have a nice time developing!")
        return None
    elif response1 == 'y':
        print("^"*50)
        print("Enter your tasks and reminders below:")
        more = True
        Data = []
        while(more):
            print("#"*10)
            data = input("<:> ")
            Data.append(data.strip())
            response2 = input("Want to add more to your list? \n(y/n)").lower()
            more = True if response2 == 'y' else False

        print("%"*100)
        print("Thanks, Have a nice day")

        return Data


def WriteDatatoFile(Data):
    """This function will write all the tasks to a text file."""
    if Data != None:
        # Enter the complete path for db.txt file
        with open('<path-to-db.txt>', 'a') as dataBaseFile:
            for line in Data:
                dataBaseFile.write(line+'\n')


WriteDatatoFile(GetReminders())
