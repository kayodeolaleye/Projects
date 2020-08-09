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
import os
import numpy as np

username_fn = "user.txt"
tasks_fn = "tasks.txt" 

# Note: store user name and passwords corresponding to a user in a tuple. 
# Read the content of users.txt into a list of tuple

 # declare an empty list to store username and password of all users

CURRENT_USER = None # set the username of the user that is currently logged-in to an empty string


def get_users():

    # this function takes as input a Text file containing all users login details 
    # the function reads the Text file and stores the data as a list of tuples containing the username and password for each users. 

    users_login_details = []
    with open(username_fn, "r") as f:
        for line in f:
            line = line.strip().split()
            users_login_details.append((line[0][:-1], line[1])) 

    return users_login_details

# MENU
def menu(current_user):

    if current_user == None:
        print("Please login to continue!")
        current_user = login()
        # CURRENT_USER = current_user
      
    if current_user == "admin":
        menu = input("Please select one of the following options: \n r - register user \n a - add task \n va - view all tasks \n vm - view my tasks \n gr - generate reports \n ds - display statistics \n e - exit \n")
    else:
        menu = input("Please select one of the following options: \n a - add task \n va - view all tasks \n vm - view my tasks \n e - exit \n")

    if menu == "r":
        reg_user()

    if menu == "a":
        add_task()

    if menu == "va":
        view_all()

    if menu == "vm":
        view_mine(current_user)

    if menu == "gr":
        generate_report(username_fn, tasks_fn)

    if menu == "ds":
        display_statistics("task_overview.txt", "user_overview.txt")

    if menu == "e":
        exit_check = input("Are you sure you want to log-out? (yes / no) ")
        if exit_check == "yes":
            current_user = None
            print("Successfully logged-out.")
            exit(0)

    print("\n")

# USER LOGIN 
def login(current_user=None):
    
    users_login_info = get_users()

    endless_loop = True
    while endless_loop:
        user_name = input("Username: ")
        password = getpass.getpass() 
        
        if (user_name, password) in users_login_info:  # Only users with correct login details can access the task manager
            current_user = user_name
            endless_loop = False
        else:
            print("Either your user name or password is incorrect. Try again.\n")

    print("\nWelcome {}!".format(current_user))
    print()

    return current_user

# USER REGISTRATION
def reg_user():

    users_login_details = get_users()

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
   

# TASK ASSIGNMENT
def add_task():

    task_details = []

    task_owner = input("Enter the username of the person the task is assigned to:  ")
    task_details.append(task_owner) # append the information to the list "task_details"

    task_title = input("Enter the title of the task: ") 
    task_details.append(task_title)

    task_description = input("Enter the description of the task: ")
    task_details.append(task_description)
   
    date_assigned = datetime.strftime(datetime.date(datetime.now()), "%d-%m-%Y")
    task_details.append(date_assigned)

    task_deadline = input("Enter the due date of the task (format => 10 Jul 2020): ")
    # task_deadline = format_date(task_deadline)
    task_details.append(task_deadline)

    is_task_completed = "No"
    task_details.append(is_task_completed)

    # write the data provided by the user to tasks.txt
    with open(tasks_fn, "r+") as f:
        old_tasks = f.read()
        f.seek(0)
        new_task = ", ".join(detail for detail in task_details)
        print("New task: ", new_task)
        f.write(old_tasks + "\n" + new_task)
    
def view_all():

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

def view_mine(current_user):

    user_task_count = 0
    sub_headers = ["Assigned to:", "Task:", "Task description:", "Date assigned:", "Due date:", "Task Complete:"]
    # display all the tasks that have been assigned to the user that is currently logged-in 
    # make sure the tasks is displayed in a user-friendly, easy to read manner.
    with open(tasks_fn, "r") as f:
        print(f"TASKS FOR {current_user}".upper().center(40))

        all_tasks = []
        my_tasks = [] # an empty list to store tasks specific to the current user
        for line in f: 
            line = line.strip().split(",")
            user_task_count += 1
            task = line[1]
            assigned_to = line[0]
            date_assigned = line[3]
            task_complete = line[5]
            due_date = line[4]
            task_descrp = line[2]
            tasks = [str(user_task_count), task, assigned_to, date_assigned, task_complete, due_date, task_descrp] 
            all_tasks.append(tasks)
            if line[0] == current_user and len(line) > 0:
            
                print_user_f = "\n {} \n {} {} \n {} {} \n {} {} \n {} {} \n {} {} \n {} {} \n".format(
                "Task #" + str(user_task_count).ljust(20), sub_headers[1].ljust(20), task.ljust(20), sub_headers[0].ljust(20),assigned_to.ljust(20), 
                sub_headers[3].ljust(20), date_assigned.ljust(20), sub_headers[5].ljust(20), task_complete.ljust(20),
                sub_headers[4].ljust(20), due_date.ljust(20), sub_headers[2].ljust(20), task_descrp.ljust(20))
                print("-"*79)
                print(print_user_f)
                print("-"*79)
                my_tasks.append(tasks)

        if user_task_count == 0:
            print("You currently have no task assigned to you.") 
            print("\n")
            input("Press '-1' to go back to the main menu: ")
            menu(current_user)


        task_select = input("Would you like to select a specific task? \n press the task number on your keyboard e.g., '1' to select Task #1 \n press '-1' to go back to the main menu: ")
        if task_select == "-1":
            menu(current_user)
        else:
            task_to_select = all_tasks[int(task_select)-1] # use an integer cast of 'task_select' to choose a specific task from 'my_tasks'
            print_task_f = "\n {} \n {} {} \n {} {} \n {} {} \n {} {} \n {} {} \n {} {} \n".format(
                "Task #" + task_to_select[0].ljust(20), sub_headers[1].ljust(20), task_to_select[1].ljust(20), sub_headers[0].ljust(20),task_to_select[2].ljust(20), 
                sub_headers[3].ljust(20), task_to_select[3].ljust(20), sub_headers[5].ljust(20), task_to_select[4].ljust(20),
                sub_headers[4].ljust(20), task_to_select[5].ljust(20), sub_headers[2].ljust(20), task_to_select[6].ljust(20))
            print("-"*79)
            print(print_task_f)
            print("-"*79)

            action = input("To mark Task #{} as complete, press 'mt' on your keyboard \n To edit task, press 'et': ".format(task_select))

            if action == "mt":
               
                # update the task in tasks.txt so that the next time the file is read, it would indicate that the task has been completed
                # We will need to find a way to get the specific line for this task in the tasks.txt file.
                task_index, task_details = selected_task(tasks_fn, current_user, task_select)
                
                lines = _readlines(tasks_fn)
                if task_details[-1] == "No":
                    task_details[-1] = "Yes" # change the value of task complete ("No") to "Yes

                line_string = ", ".join(task_details) # convert list of string to string

                lines[task_index] = line_string + "\n" # update the specific task to the current information

                _writelines(tasks_fn, lines)
                print("\nTask successfully marked as completed")
              
            if action == "et":
                # TODO: Let the user change the username of the person to whom the task is assigned or change the due date of the task
                # Only be able to edit task if it has not been completed
                edit_options = input("Please select one of the following edit options: \n eto - edit task owner \n cdd - change due date: ")

                task_index, task_details = selected_task(tasks_fn, current_user, task_select)
                lines = _readlines(tasks_fn)
                task_complete_status = task_details[-1]
                
                if task_complete_status == "Yes":
                    print("! You cannot edit task because it has already been completed.")
                
                else:
                    if edit_options == "eto":
                        new_task_owner = input("Please enter the name of the new person the task is assigned: ").lower()
                        old_task_owner = task_details[0]
                        if old_task_owner == new_task_owner:
                            print("New task owner must be different from old task owner.")
                            menu(current_user)
                        task_details[0] = new_task_owner

                        line_string = ", ".join(task_details)

                        lines[task_index] = line_string + "\n"

                        _writelines(tasks_fn, lines)
            
                    
                    if edit_options == "cdd":
                        new_date = input("Enter the new due date of the task (e.g., 10 Jul 2020): ")
                        old_date = task_details[-2]
                        if old_date == new_date:
                            print("New due date must be different from old due date.")
                            menu(current_user)
                        task_details[-2] = new_date

                        line_string = ", ".join(task_details)

                        lines[task_index] = line_string + "\n"

                        _writelines(tasks_fn, lines)
           

def generate_report(users_fn, tasks_fn):
    # this function generates an overview of the Task Manager
    # it displays statistics extracted from the user.txt and the tasks.txt files
    
    generate_txt_files("task_overview.txt")
    generate_txt_files("user_overview.txt")

    task_overview(tasks_fn)
    user_overview(users_fn, tasks_fn)

def display_statistics(task_overview_fn, user_overview_fn):

    # print User overview 
    user_data = []
    with open(user_overview_fn, "r") as f:
        for line in f:
            line = line.strip().split(": ")
            user_data.append((line[0], line[1]))

    total_users = user_data[0][1] # total number of registered users
    total_tasks = user_data[1][1] # total number of tracked tasks
    user_specific_data = user_data[2:]
    user_overview_lines = ["\nTotal number of users: " + total_users + "\n" + "Total number of tracked tasks: " + total_tasks + "\n"] 
    for username, d in user_specific_data:
        d = d.split(", ")
        print_l = username.ljust(30) + "\n" + "\n" + \
                    "Total number of task assigned: " + d[0] + "\n" + \
                    "Percentage of the total tasks assigned: " + d[1] + "%" + "\n" + \
                    "Percentage of completed assigned tasks: " + d[2] + "%" + "\n" + \
                    "Percentage of uncompleted assigned tasks: " + d[3] + "%" + "\n" + \
                    "Percentage of overdue uncompleted tasks: " + d[4] + "%" + "\n"
        user_overview_lines.append(print_l)
    print("User Overview: ".center(30))
    print("-"*79)
    for user_stat in user_overview_lines:
        print(user_stat)
    print("-"*79)

    # print task overview.

    task_data = []
    with open(task_overview_fn, "r") as f:
        for line in f:
            line = line.strip().split(": ")
            task_data.append(line[1])


    print_l = "\nTotal number of tracked tasks: " + task_data[0] + "\n" + \
                "Total number of completed tasks: " + task_data[1] + "\n" + \
                "Total number of uncompleted tasks: " + task_data[2] + "\n" + \
                "Total number of overdue uncompleted tasks: " + task_data[3] + "\n" + \
                "Percentage of uncompleted tasks: " + task_data[4] + "%" + "\n" + \
                "Percentage of overdue uncompleted tasks: " + task_data[1] + "%" + "\n"

    print("\nTask Overview: ".center(30))
    print("-"*79)
    print(print_l)
    print("-"*79)

                
# TODO: Define a function for printing user-friendly stuff

# UTILS functions

def task_overview(tasks_fn):
    # this function generates statistics from the tasks file
    total_num_of_tasks = 0
    completed_count = 0
    uncompleted_count = 0
    task_overdue_count = 0

    with open(tasks_fn, "r") as f:
        for line in f:
            total_num_of_tasks += 1 
            line = line.strip().split(", ")
            due_date_str = line[4]
            due_date_str = format_date(due_date_str)
            due_date = datetime.strptime(due_date_str, '%d-%m-%Y') # convert string to date
            date_now = datetime.now() # get the current date
    
            if line[-1] != "No":
                completed_count += 1
            else:
                uncompleted_count += 1
                if due_date < date_now:
                    task_overdue_count += 1


    percent_incomplete = (uncompleted_count / total_num_of_tasks) * 100.0

    # percentage of tasks over-due
    percent_overdue = (task_overdue_count / total_num_of_tasks) * 100.0

    lines = "Tasks total: " + str(total_num_of_tasks) + "\n" +  "Completed Tasks total: " +  \
        str(completed_count) + "\n" + "Uncompleted Tasks total: " + str(uncompleted_count) + \
        "\n" + "Overdue Tasks total: " +  str(task_overdue_count) + "\n" + "Percentage Tasks Incomplete: " + \
            str(percent_incomplete) + "\n" + "Percentage Tasks Overdue: " + str(percent_overdue)

    _writelines("task_overview.txt", lines)

    print("Task Overview generated successfully!")


def user_overview(users_fn, tasks_fn):
    # this function generates statistics from the users.txt file
    user_task_stats = {} # this dictionary stores all users individual statistics in a list with the user as the key 
    user_dict = {}
    total_num_of_tasks = 0
    total_num_users = 0
    lines = []

    with open(users_fn, "r") as f:
        for line in f:
            total_num_users += 1

    lines.append("Total number of users: " + str(total_num_users) + "\n")
    

    with open(tasks_fn, "r") as f:
        for line in f:
            total_num_of_tasks += 1  # total number of tasks that have been generated and tracked using the task_manager.py
            line = line.strip().split(", ")

            # create a dictionary where the keys are distinct user names (line[0]) and the values are line[1:]
            key = line[0]
            if key not in user_dict:
                user_dict[key] = []
            user_dict[key].append(line[1:])

    lines.append("Total number of tasks: " + str(total_num_of_tasks) + "\n")

    for user in user_dict:
        print(user)
        user_total_task = len(user_dict[user])
        if user not in user_task_stats:
            user_task_stats[user] = []
        user_task_stats[user].append(user_total_task) # append total number of tasks assigned to that user
  
        percent_task_assigned = np.round(((user_total_task / total_num_of_tasks) * 100.0), 2) # percentage of the total number of tasks assigned to that user
        user_task_stats[user].append(percent_task_assigned)
        completed_count = 0
        uncompleted_count = 0
        task_overdue_count = 0
        for task in user_dict[user]:
            due_date_str = task[3]
            due_date_str = format_date(due_date_str)
            due_date = datetime.strptime(due_date_str, '%d-%m-%Y') # convert string to date
            date_now = datetime.now() # get the current date
            
            if task[-1] != "No":
                completed_count += 1 
            else:
                uncompleted_count += 1
                if due_date < date_now:
                    task_overdue_count += 1
        percent_task_completed = (completed_count / user_total_task) * 100.0
        percent_task_incomplete = (uncompleted_count / user_total_task) * 100.0
        percent_task_overdue = (task_overdue_count / user_total_task) * 100.0
        user_task_stats[user].append(percent_task_completed) # percentage of completed task per user 
        user_task_stats[user].append(percent_task_incomplete) # percentage incomplete task
        user_task_stats[user].append(percent_task_overdue) # percentage overdue task

    # Write statistics to user_overview.txt
    
    for user in user_task_stats:
        # print(user)
        lines.append(user + ": " + ", ".join(list(map(str, user_task_stats[user]))) + "\n")

    _writelines("user_overview.txt", lines)

     print("User Overview generated successfully!")


def generate_txt_files(file_name):

    if not os.path.exists(file_name):
        open(file_name, 'w').close()
              
def selected_task(task_fn, current_user, task_select):

    # This reads the file line by line to retrieve the line number and the tasks we want to mark as completed based on task_select 
    # (keyboard input from the user)
    
    line_count = 0 # counter for each lines in tasks.txt
    task_index = 0 # this is use to store the line number of the specific task we want to mark as completed in tasks.txt
    task_details = None # this will store the strings in the line we want to mark as completed as a list of words.

    # This function takes the task file name as input,
    # and returns a list of words for the specified task identified by its line number in a list of tasks belonging to the current user
    with open(tasks_fn, "r") as f:
        for line in f:
            line_count += 1 
            line = line.strip().split(", ")              
            if line[0] == current_user and len(line) > 0 and int(task_select) == line_count: # check that only tasks belonging to the current user and the task number specified are edited 
                task_index = line_count - 1
                task_details = [i for i in line] # copy every item in line to another list
    return task_index, task_details

def _readlines(file_name):
    # this is an extension of the built-in Python's readlines() function
    with open(file_name, 'r') as f:
        lines = f.readlines() # store every lines in tasks.txt as a list
        return lines

def _writelines(file_name, lines):
    # this is an extension of the built-in Python's writelines() function
    # the function takes the file name to write and a list of strings as input and writes the strings to the file
    with open(file_name, 'w') as f:
        f.writelines(lines)

def format_date(date_str):
    # this function converts a date object to string
    # date_str (str) in "DD MM YYYY" format
    # output: str in DD Nov YYYY

    if "-" not in date_str:
        date_str = date_str.split(" ") # split date into day, month, and year and store as a list
    
    dd = date_str[0]
    mm = date_str[1]
    yyyy = date_str[2]
    new_format = ""
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    # loop through months and choose a month (three-lettered word) corresponding to mm
    for i, m in enumerate(months):
        if m.lower() == mm.lower():
            new_format = "{}-{}-{}".format(int(dd), i+1, int(yyyy))
            # print("new format: ", new_format)

    return new_format



print("\n")
print("Run the script again to perform another task.")
    

def main():
    
    # Once a user has successfully logged in, display a menu based on user's privilege

    menu(CURRENT_USER)



if __name__=="__main__":
    main()
