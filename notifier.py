#!/usr/local/bin/python3.8

import os
import time

dbFile = "<path-to-db.txt>"


def notify(title, text):
    """ This function helps in generating desktop notifications using AppleScript. """
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


def GetData(DBFile):
    """ Retrieving data from the text file. """
    Data = []
    with open(DBFile, 'r') as file:
        for line in file:
            Data.append(line.strip())
    return Data


def main():
    """ Driver Function """
    reminders = GetData(dbFile)
    for _ in range(len(reminders)):
        notify("Reminder", reminders[_])
        time.sleep(2)


def clearDB():
    """ This function will empty the DataBase (text) file for next data to come in. """
    file = open(dbFile, 'w')
    file.close()


main()
clearDB()
