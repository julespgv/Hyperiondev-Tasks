"""Some references are included in line.
Feedback from completing other Hyperiondev programming tasks / suggestions from 1:1 mentoring session 
(e.g. improving function get_input() by passing input type as an argument)

Finding semicolons in a string:
https://www.w3schools.com/python/ref_string_find.asp
Raising exceptions manually:
https://www.w3schools.com/python/python_try_except.asp
"""

#=====importing libraries=====
import os
from datetime import datetime, date
DATETIME_STRING_FORMAT = "%Y-%m-%d"

#=====functions=====
def call_function(function_name):
    '''Handle unforeseen errors for functions called by run_time() or main_menu()'''
    try:
        function_name()
    except:
        print (f"Error when running function: {str(function_name)}")

def get_percent(a, b):
    '''Either calculate a percentage successfully, or return 0'''
    try:
        result = eval(f"100*{a}/{b}")
        
        # If result is an integer return it without modification
        # Reference: https://docs.python.org/3/library/stdtypes.html#float.is_integer
        if (result).is_integer():
            return f"{result}%"
        
        # Float values should be formatted to 2 decimal places
        else:
            return f"{result:.2f}%"
    
    # All exceptions are handled (including ZeroDivisionError) as below, following mentor call discussion
    except:
        return "n/a"

def get_input(message="Please input a value (semicolons are prohibited): ", input_type=str,\
              error_message="Error! Please try again.", special_input=None):
    '''Return validated user input with error handling according to type specified as argument'''
    # Loop trying to take a valid input:
    while True:
        try:
            # For all normal inputs, return valid input of the requested type:
            valid_input = input_type(input(message))
            
            # For all date input requests
            if special_input == "date":
                # Attempt to put user's input into date format and return value
                valid_input = datetime.strptime(valid_input, DATETIME_STRING_FORMAT)
            
            # For all requests where semicolons are not permitted
            if special_input == "no_semicolon":
                                
                if not valid_input.find(";") == -1:
                    error_message
                    raise ValueError("Please re-enter text without semicolons.")
                    
            # If no exceptions raised return user's input
            return valid_input

        # On error display error message with guidance, then reloop
        except ValueError as error:
            print (f"{error}\nInput type expected is ({input_type}).")

        except:
            print (f"{error_message}\nInput type expected is ({input_type}).")
            continue

def check_files_exist(filenames_to_check):
    '''File names passed to the function (in a list) are created if non-existent'''
    for filename in filenames_to_check:
        
        # If missing, write the file with any defaults and notify user
        if not os.path.exists(filename) == True:

            # Open file to write with automatic closing
            with open(filename, "w") as default_file:
                print (f"File {filename} was missing and has now been created.")
                
                # user.txt requires initial credentials written into it:
                if filename == "user.txt":
                    default_file.write("admin;password")
                
                    # Display credentials to user for first admin login
                    print ("Please use the default admin login credentials below:\n\
                    \nDefault username is 'admin'\
                    \nDefault password is 'password'\n")
    return

def check_task_overdue(index):
    '''Returns "True" if this task is overdue, otherwise return "False"'''
    # Reference used, see https://stackoverflow.com/questions/1937622/convert-date-to-datetime-in-python
    # Assign to variable the time of 00:00 of the start of today and compare to due date.'''
    curr_date = datetime.combine(date.today(), datetime.min.time())
    this_due_date = task_list[index]["due_date"]
    
    if this_due_date < curr_date:
        return True
    
    else:
        return False

def load_users():
    '''Reads user.txt file, assign usernames/passwords to dictionary 'username_password'
    This is held in memory during program run time
    '''
    with open("user.txt", 'r') as user_file:
        # Split each line of the file into an element in a list
        user_data = user_file.read().split("\n")
    
    # Make dictionary available across the program, so can look up usernames.
    global username_password
    username_password = {}
    
    # Loop through loaded user_data and add contents of each element to the dictionary
    for user in user_data:
        username, password = user.split(';')
        username_password[username] = password
                
def load_tasks():
    '''Load tasks from tasks.txt file and assign to tasks_list, which is stored in memory'''    
    with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        # loop through each line in task data and remove non-blank lines:
        task_data = [t for t in task_data if t != ""]

    # Variable is used across the program, so declare as global:
    global task_list
    task_list = []
    
    # Loop through each line of the file
    for t_str in task_data:
        curr_t = {}
        # Split by semicolon and manually add each component to dictionary
        task_components = t_str.split(";")
        curr_t['username'] = task_components[0]
        curr_t['title'] = task_components[1]
        curr_t['description'] = task_components[2]
        curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['completed'] = True if task_components[5] == "Yes" else False
        
        # Add to task list stored in memory for editing in the program.
        task_list.append(curr_t)
    
def write_users():
    '''Prepare and write list of userdata currently in memory to file'''
    with open("user.txt", "w") as out_file:
        user_data = []
        
        # Loop through username_password adding the delimited username and password to a list
        for k in username_password:
            user_data.append(f"{k};{username_password[k]}")
        
        # Join the delimited usernames/passwords and write to file on separate lines.
        out_file.write("\n".join(user_data))
        print("Updated users file")

def write_tasks():
    '''Prepare and write the list of tasks currently in memory to file'''
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        # Loop through contents of each task and add to a list
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                # Convert the date formats into the format used when writing to file: 
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                # Write to file 'Yes' if task is marked complete, or 'No' otherwise:
                "Yes" if t['completed'] else "No"
            ]
            # Join the contents together with semicolon separator
            task_list_to_write.append(";".join(str_attrs))
        # Finally, each task should be written to file on a separate line.
        task_file.write("\n".join(task_list_to_write))
    print("Tasks file updated.")

def task_details(index):
    '''Display the details of an indivdual task'''
    print(top_line)
    print (f"Task number:\t\t\t\t{index}")
    print (f"User assigned to:\t\t\t{task_list[index]['username']}")
    print (f"Title:\t\t\t\t\t{task_list[index]['title']}")
    print (f"Assigned date:\t\t\t\t{task_list[index]['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
    print (f"Due date:\t\t\t\t{task_list[index]['due_date'].strftime(DATETIME_STRING_FORMAT)}")
    # Account for completion status 'Yes' or 'No' 
    if task_list[index]['completed'] == True:
        print (f"Completed:\t\t\t\tYes")
    else:
        print (f"Completed:\t\t\t\tNo")
    print (f"Description:\n {task_list[index]['description']}")    
    print (separator_line)

def display_file_contents(filename):
    with open(filename, 'r') as file:
        # List to hold data parsed from file
        file_data = file.read()
    print (f"{file_data}\n")

def login():
    '''Loops user login prompt until user has logged in successfully'''
    logged_in = False
    while not logged_in:
        print("LOGIN")
         
        # Logged in user is a global variable for reference in other functions
        global curr_user
        curr_user = get_input("Username: ")
        curr_pass = get_input("Password: ")
        
        # Warn user of incorrect username/password
        if curr_user not in username_password.keys():
            print("User does not exist")
            continue
        
        elif username_password[curr_user] != curr_pass:
            print("Wrong password")
            continue
        
        else:
            print("Login Successful!")
            logged_in = True

def main_menu():
    '''Display menu, user enters input from options'''
    while True: 
        # Display the menu, take user input to call other functions.
        menu_options = (f'''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
ds - Display statistics
gr - Generate reports
e - Exit
: ''') 
        # Convert input to lower case to avoid errors.
        menu = get_input(menu_options, str).lower()

        # If user has made valid selection,
        # program will run the associated function:
        if menu == 'r':
            call_function(reg_user)

        elif menu == 'a':
            call_function(add_task)
        
        elif menu == 'va':
            call_function(view_all)
        
        elif menu == 'vm':
            call_function(view_mine)
    
        # Function can only be called by admin users.
        elif menu == 'ds':
            if curr_user == 'admin':
                call_function(display_statistics)
            
            else:
            # Display error message for non-admin:
                print("Permission denied: access limited to admin users")
        
        elif menu == 'gr':
            call_function(generate_reports)
     
        elif menu == 'e':
            print('Goodbye!!!')
            break
        
        # Error message for e.g. invalid input:
        else:
            print("Error: that is not a valid choice. Please try again.")

    # If chose exit, will break loop, then will exit program.
    return

def reg_user():
        '''Add a new user to the user.txt file'''        
        new_username = get_input("New Username: ", special_input = "no_semicolon").lower()
                
        # If this username already exists, display error and exit to main menu:
        if new_username in username_password:
            print ("Error: a user with this username exists! Returning to main menu.\n\
You can try again with a different username.")
            return
        
        # Request input and confirmation of password:
        new_password = get_input("New Password: ", special_input = "no_semicolon")
        confirm_password = get_input("Confirm Password: ")

        # Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            
            # If passwords are the same,
            # add them to the list of usernames and passwords in memory first:
            username_password[new_username] = new_password
            
            # Write to file using contents of username_password, then display message:
            write_users()
            print(f"Successfully added new user.\nUsername is \t{new_username},\nPassword is\t{confirm_password}.\n")
        
        else:
            print("Error: passwords do not match")

def add_task():
    '''Add a new task to task.txt file'''
    task_username = get_input("Name of person assigned to task: ")
    
    # Return error message if task assignee is not an existent username    
    if task_username not in username_password:
        
        print("User does not exist. Please enter a valid username")
        return
    
    task_title = get_input("Title of Task: ", special_input = "no_semicolon")
    task_description = get_input("Description of Task: ", special_input = "no_semicolon")
    
    # Get input from user for due date
    due_date_time = get_input("Due date of task (YYYY-MM-DD): ", str, \
"Invalid datetime format. Please use the format specified", special_input="date")

    # Then get the current date
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }
    
    # Add this new task to list of tasks, then write to file.
    task_list.append(new_task)
    write_tasks()
                
def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. readable) 
    '''
    # Displays message if no existent tasks. 
    if (task_list == []) or (task_list is None):
        print ("No tasks have been created.")
    else:
        # Will loop through all tasks loaded, displaying each
        print ("All tasks are listed below:") 
        for index, t in enumerate(task_list):
            task_details(index)

def view_mine():
    '''Display and provide updates to a logged-in user's tasks (all tasks if admin user)'''
    # Check if no tasks loaded from tasks.txt:
    if (len(task_list) == 0):
        print (f"No tasks assigned.")
    
    # If tasks exist, loop as below:
    else:
        print (f"Tasks assigned to {curr_user}")
        while True:
            # Create list of tasks visible/editable by this user, which updates if user reassigns or modifies tasks.
            visible_tasks = []
            # Looping through all tasks display those assigned to logged-in user:
            for index, t in enumerate(task_list):

                # Admin can view/edit all tasks:
                if curr_user == "admin":
                    visible_tasks.append(index)
                    task_details(index)

                # Non-admin users can view / edit their own tasks only:
                elif curr_user == t['username']:
                    visible_tasks.append(index)
                    task_details(index)
        
            if (visible_tasks == []) or (visible_tasks is None):
                print ("No tasks created for this user.")
            else:
                print (f"You can view the following task numbers: {visible_tasks}")
            # Input command:
            selected_task = get_input("Enter a Task number to update/edit that task,\n\
or enter '-1' to exit to main menu\n: ", int, "You can enter a number only")
            
            # Exit loop if '-1' entered:
            if (selected_task == -1):
                print("Returning to main menu")
                break
            
            if not selected_task in visible_tasks:
                print ("Task not editable by logged in user")
            
            else:
                try:
                    # Allows user to edit task, mark complete.
                    drill_down(selected_task)                
                
                except:
                    print(f"\nError! Enter the Task number (integer), or '-1' to go back.")
                    continue
            
def drill_down(index):
    '''User can select to mark a task complete or edit it'''
    while True:
        # Display all details of this task: 
        task_details(index)        

        # Prevent editing if task has been marked complete:
        if (task_list[index]['completed'] == True) :
            print("This task has already been completed. No editing is possible.")
        
        # User input to either edit task or mark complete:
        option = get_input(f"Enter one of the below options:\n\t'mc' to Mark complete\n\t'e' to edit,\
\n\t'-1' to go back.\n:", str, "Error! Please enter 'mc' or 'edit'")

        # Exit function if command given
        if option == "-1":
            print("Exiting edit mode.")
            return
        
        # If task is not completed,
        elif (task_list[index]['completed'] == False):
            
            # Mark task complete and write to file: 
            if option == "mc":
                task_list[index]['completed'] = True
                write_tasks() 
                print ("Marked complete. File saved.")
            
            # Or call function to edit task.
            elif option == "e":
                edit_task(index)
        
        else:
            print("Error. Please enter a different command.")
        
        return

def edit_task(index):
    '''User can change due date / assign task to another existent user. Automatically saves after edit'''
    while True:
        choice = get_input("Enter 'date' to change due date.\nOr enter 'assign' to change the assigned user.\n\
or enter '-1' to exit\n: ")
        
        if (choice == "-1"):
            return
        
        # User changes the due date:
        elif (choice == "date"):
            new_due_date = get_input("Please enter the new due date in YYYY-MM-DD format: ", str,\
"Invalid datetime format. Please use the format specified", special_input="date")
            task_list[index]['due_date'] = new_due_date
            write_tasks()
            print ("Tasks file saved.")
        
        # User enters the name of a different existent user:
        elif choice == "assign":
            assign_user = get_input("Assign task to which user? ")
        
            if (assign_user in username_password.keys()):
                task_list[index]['username'] = assign_user
                write_users()
                print (f"Assigned to '{assign_user}'. File saved.\n")
                return
            
            else:
                print ("User does not exist.")

        else:
            print ("Error. Please select a valid option.")

        return

def display_statistics():
    ''' Displays users and tasks statistics, which are loaded from files'''
    display_file_contents("task_overview.txt")
    display_file_contents("user_overview.txt")
    
def generate_task_overview():
    '''Prepare and write data to task_overview.txt'''
    print ("\nGenerating information for Task Overview.")    
    completed_tasks = 0
    overdue_tasks = 0
    
    # Loop through every task and count completed/incomplete and overdue tasks for this user:
    for index, task in enumerate (task_list):        
        
        if task_list[index]['completed'] == True:
            completed_tasks +=1
        
        elif check_task_overdue(index) == True:
            overdue_tasks += 1
    
    curr_time = datetime.now()
    task_total = len(task_list)
    incomplete_tasks = (task_total - completed_tasks)
    percent_incomplete_tasks = get_percent(incomplete_tasks, task_total)
    percent_overdue_tasks = get_percent(overdue_tasks, task_total)

    task_overview_data = f"\
{separator_line}\n\
Task overview generated by {curr_user} at {datetime.now()}\n\
{separator_line}\n\
Total number of tasks:                   {task_total}\n\
Total completed tasks:                   {completed_tasks}\n\
Number of incomplete tasks:              {incomplete_tasks}\n\
Number of overdue & incomplete tasks:    {overdue_tasks}\n\
Percentage of tasks that are overdue:    {percent_overdue_tasks}\n\
Percentage of tasks that are incomplete: {percent_incomplete_tasks}\n\
{separator_line}"
 
    # Open the file to write.
    with open("task_overview.txt", "w") as out_file:
        # Write the larger list of all task information to file: 
        out_file.write(task_overview_data)
        print("Wrote to task_overview.txt file")

def generate_user_overview():
    '''Prepares and writes data to user_overview.txt'''
    print ("\nGenerating information for User Overview")
    
    # Prepare variables for top section of file: 
    user_overview_data = []
    num_users = len(username_password)
    num_tasks = len(task_list)
    # curr_time = datetime.now()

    user_overview_header = f"\
{separator_line}\n\
User overview generated by {curr_user} at {datetime.now()}\n\
Total number of users registered:        {num_users}\n\
Total number of tasks generated:         {num_tasks}\n\
{separator_line}"
    user_overview_data.append(user_overview_header)

    # Loop through each user in users.txt:
    for user in username_password:
    
        # Set variables back to 0 before counting for this user
        user_tasks = 0
        user_incomplete_tasks = 0
        user_incomplete_overdue = 0
        user_complete_tasks = 0

        # Loop through all tasks and identify which are this user's
        for index, task in enumerate(task_list):
            
            # When a task is assigned to this user 
            if user == task_list[index]['username']:
                # Add 1 to user_tasks: 
                user_tasks += 1
                
                # Update variables according to task's completion status:
                if task_list[index]['completed'] == True:
                    user_complete_tasks += 1
            
                elif task_list[index]['completed'] == False:
                    user_incomplete_tasks += 1
                    
                    if check_task_overdue(index) == True:
                        user_incomplete_overdue += 1  

        user_percent_assigned = get_percent(user_tasks, len(task_list))            
        user_percent_complete = get_percent(user_complete_tasks, user_tasks)
        user_percent_incomplete = get_percent(user_incomplete_tasks, user_tasks)
        user_percent_incomplete_overdue = get_percent(user_incomplete_overdue, user_tasks)

        # Concatenate user statistics and append to list
        user_overview_string = (f"\
Username:                                 {user}\n\
Number of tasks assigned:                 {user_tasks}\n\
Percentage of total tasks assigned:       {user_percent_assigned}\n\
Percentage of assigned tasks complete:    {user_percent_complete}\n\
Percentage of incomplete assigned tasks:  {user_percent_incomplete}\n\
Percentage of incomplete, overdue tasks:  {user_percent_incomplete_overdue}")
        
        # Add the above string to the larger list
        user_overview_data.append(user_overview_string)
        user_overview_data.append(separator_line)
    # Open the file to write.
    with open("user_overview.txt", "w") as out_file:
        # Write the larger list of all users' information to file: 
        out_file.write("\n".join(user_overview_data))
        print("Wrote to users_overview.txt file")

def generate_reports():
    '''Call functions to generate task_overview.txt and user_overview.txt'''
    # Generate and write to task overview.txt 
    generate_task_overview() 
    # Generate data for user_overview.txt
    generate_user_overview()

def startup():
    # Confirm files required exist and generate them if not:
    files_to_check = ('user_overview.txt', 'task_overview.txt', 'tasks.txt', 'user.txt')
    check_files_exist(files_to_check)
    # Load tasks and usernames/passwords from files into memory
    load_tasks()
    load_users()

    # Variables used to create top / bottom / border lines when displaying information.
    global top_line, bottom_line, separator_line
    top_line = "\n----------------------------------------------------------------------"
    bottom_line = "----------------------------------------------------------------------\n"
    separator_line = "----------------------------------------------------------------------"

def run_time():
    '''Load tasks and user from file into memory, complete user login, 
    then loop menu selection until exit
    '''
    # Complete login and loop main menu until user exits.
    call_function(login)
    call_function(main_menu)

#=====run program=====
call_function(startup)
call_function(run_time)