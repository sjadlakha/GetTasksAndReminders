# Simple Automated Reminder Program

This Program lets you add reminders for the next time you login.

### This program is specifically written for MacOS
It uses AppleScript to notify.

## Files and their functions:
  #### getReminders.py :
    The script helps in calling out the user to enter any reminders for the next session.
  #### notifier.py:
    The script uses AppleScript to create a desktop notification for each reminder on startup.
  #### SetReminders.sh:
    This file should be given execution permission as it commands to run the getReminders.py file in the terminal.
  #### startup.sh:
    To run the notifier.py script on startup we created a bash file that calls it runs on start up by enabling it to run on startup.
  #### db.txt:
    This text file stores the reminders everytime you enter them and its contents are cleared after you get notified.
 ##### Rest information regarding each function and file is present inside it.
 
### Flow :
    1. Run the SetReminders.sh file by double tapping it.
    2. Set reminders in terminal.
    3. Next time you start your mac, you will receive a notification for each reminder.
