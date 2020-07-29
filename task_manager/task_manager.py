"""This Python program is a task management system for a small business.
The user of this program can perform any of the following actions depending on their access level:
    - register user
    - add task
    - view all tasks
    - view my tasks
Only the admins can register new users.    

"""

# imports
import getpass 
from datetime import datetime

username_fn = "user.txt"
tasks_fn = "tasks.txt" 

# Note: store user name and passwords corresponding to a user in a tuple. 
# Read the content of users.txt into a list of tuple

users_login_details = [] # declare an empty list to store username and password of all users

current_user = "" # set the username of the user that is currently logged-in to an empty string
endless_loop = True # boolean value for the while loop that continuously ask user to login until they type the correct login details

with open(username_fn, "r") as f:
    for line in f:
        line = line.strip().split()
        users_login_details.append((line[0][:-1], line[1])) # this is a list of tuples to store username and password. line[0] and line[1] corresponds to the username and password for each user

# USER LOGIN 
current_user = ""
endless_loop = True
while endless_loop:
    user_name = input("Username: ")
    password = getpass.getpass() 
    
    if (user_name, password) in users_login_details:  # Only users with correct login details can access the task manager
        current_user = user_name
        endless_loop = False
    else:
        print("Either your user name or password is incorrect. Try again.\n")

print("\nWelcome {}!".format(user_name))
print()

# Once a user has successfully logged in, display a menu based on user's privilege

if current_user == "admin":
    menu = input("Please select one of the following options: \n r - register user \n a - add task \n va - view all tasks \n vm - view my tasks \n e - exit \n")
else:
    menu = input("Please select one of the following options: \n a - add task \n va - view all tasks \n vm - view my tasks \n e - exit \n")

# USER REGISTRATION
if menu == "r":

    usernameIsTaken = True

    while usernameIsTaken:

        username = input("Username: ")
        if username not in list(list(zip(*users_login_details))[0]): # make sure username does not already exist before asking for password. list(list(zip(*users_login_details))[0])) gives list of all the usernames
            password = getpass.getpass() 
            if password == getpass.getpass("Confirm password: "): # check if password and confirm password matches           
                # append the new username and password to the user.txt file.
                with open(username_fn, "r+") as f:
                    old_users = f.read()
                    f.seek(0)
                    f.write(old_users + "\n" + username + "," + " " + password) # write new username and password to file
                usernameIsTaken = False
                print("User registration successful!")
            else:
                print("Password mismatched. Please confirm your password")
        else:
            print("This username has already been taken by another user. Please choose a new username.")

# TASK ASSIGMENT
task_details = []
if menu == "a":

    task_owner = input("Enter the username of the person the task is assigned to:  ")
    task_details.append(task_owner) # append the information to the list "task_details"

    task_title = input("Enter the title of the task: ") 
    task_details.append(task_title)

    task_description = input("Enter the description of the task: ")
    task_details.append(task_description)
   
    date_assigned = str(datetime.date(datetime.now())) # TODO: change the date format to "10 Jul 2020
    task_details.append(date_assigned)

    task_deadline = input("Enter the due date of the task (e.g., 10 Jul 2020): ")
    task_details.append(task_deadline)

    is_task_completed = "No"
    task_details.append(is_task_completed)

    # write the data provided by the user to tasks.txt
    with open(tasks_fn, "r+") as f:
        old_tasks = f.read()
        f.seek(0)
        new_task = ", ".join(detail[1] for detail in task_details)
        f.write(old_tasks + "\n" + new_task)

if menu == "va":
    sub_headers = ["Assigned to:", "Task:", "Task description:", "Date assigned:", "Due date:", "Task Complete:"]
    # display the information for each task on the screen in an easy to read format
    with open(tasks_fn, "r") as f:
        print("ALL TASKS".center(40))
        for line in f: 
            line = line.strip().split(",")
            print_user_f = "\n {} {} \n {} {} \n {} {} \n {} {} \n {} {} \n {} {} \n".format(
            sub_headers[1].ljust(20), line[1].ljust(20), sub_headers[0].ljust(20),line[0].ljust(20), 
            sub_headers[3].ljust(20), line[3].ljust(20), sub_headers[5].ljust(20), line[5].ljust(20),
            sub_headers[4].ljust(20), line[4].ljust(20), sub_headers[2].ljust(20), line[2].ljust(20))
            
            print("-"*79)
            print(print_user_f)
            print("-"*79)
            
if menu == "vm":
    user_task_count = 0
    sub_headers = ["Assigned to:", "Task:", "Task description:", "Date assigned:", "Due date:", "Task Complete:"]
    # display all the tasks that have been assigned to the user that is currently logged-in 
    # make sure the tasks is displayed in a user-friendly, easy to read manner.
    with open(tasks_fn, "r") as f:
        print(f"TASKS FOR {current_user}".upper().center(40))
        for line in f: 
            line = line.strip().split(",")
            if line[0] == current_user and len(line) > 0:
                user_task_count += 1
                print_user_f = "\n {} {} \n {} {} \n {} {} \n {} {} \n {} {} \n {} {} \n".format(
                sub_headers[1].ljust(20), line[1].ljust(20), sub_headers[0].ljust(20),line[0].ljust(20), 
                sub_headers[3].ljust(20), line[3].ljust(20), sub_headers[5].ljust(20), line[5].ljust(20),
                sub_headers[4].ljust(20), line[4].ljust(20), sub_headers[2].ljust(20), line[2].ljust(20))
                print("-"*79)
                print(print_user_f)
                print("-"*79)
   
        if user_task_count == 0:
            print("You currently have no task assigned to you.")        

if menu == "e":
    exit_check = input("Are you sure you want to log-out? (yes / no) ")
    if exit_check == "yes":
        current_user = ""
        print("Successfully logged-out.")
        exit(0)
print("\n")
if current_user == "admin":
    new_feature = input("*New beta feature: an option that allows you display statistics is now available.\n Would you like to try it out? (yes / no) ").lower()

    if new_feature == "yes":

        user_count = 0
        task_count = 0
        with open(username_fn, "r") as f:
            for user in f:
                if len(user) > 0:
                    user_count += 1

        with open(tasks_fn, "r") as f:
            for task in f:
                if len(task) > 0:
                    task_count += 1
        print(f"Total number of users: {user_count} \n Total number of tasks: {task_count}")
    else:
        exit(0)
print("\n")
print("Run the script again to perform another task.")
    
