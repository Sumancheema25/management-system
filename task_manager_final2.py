# ********* login *********


import datetime


# giving the date format
date_format = '%Y-%m-%d'
# Here we will read and write file in 'user.txt'
user_file = open("users.txt", "r+") 
login = False

while login == False:
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")
    
# check for valid username and password.
    for line in user_file:
        valid_user, valid_password = line.strip("\n").split(", ") # need to add strip first and then split (strip used to remove "\n" new line) As we saw that when admin register then a new line is printed which will result in incorrect details
        if user_name == valid_user and password == valid_password:
            login = True

    if login == False:
        print("Incorect details! Please enter a valid username and password")
    user_file.seek(0)

# ********* Menu for admin only *********

    if user_name == "admin":
        choice = input("""
        Please select one of the following options:
        r - register user
        s - display statistics of total number of task and users in txt
        e - exit
        """)
    if user_name != "admin":
        choice = input(
                """Select one of the following options:
                r - register a user
                a - add task
                va - view all tasks
                vm - view my tasks
                e - exit
                """)  
    
# ********* choice "r" for admin *********    
    if choice == "r":
        if user_name != "admin":
            print("error you are not admin.")
                    
        if user_name == "admin":
            user_file = open("users.txt", "a+")  #I will need to append add this to user text 
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            confirm = input("Please confirm password: ")
            if password == confirm:
                user_file.write(f"\n{username}, {password}")
                print("Password match confirmed password")
                
                if login == False:
                    print("Incorect details! confirmed password does not match password")
    user_file.close()

# ********* choice "s" for admin *********

# When user enter "s"
# if user choose "s" the following will take place indented under if for statement
# task_file and user_file will be opened and be read only "r"
# for line in task_file the following will be assigned below: task_name, title, description, start_date, end_date, is_completed and by split by a comma in 'taks.txt'
# the following will print out all task in the following order and format using (f.format).
# task_file.close() and user_file.close() is used to close and save files
    if choice == "s":
        if user_name != "admin":
            print("error you are not admin")
        if user_name == "admin":
            task_file = open("tasks.txt", "r")
            task_file = open("tasks.txt", "r")
            user_file = open("users.txt", "r")
            task_count = task_file.readlines()
            user_count = user_file.readlines()
            print(f"""
                Tasks: {len(task_count)}
                Users: {len(user_count)}
                """)
            '''for line in task_file:
                    task_name, title, description, start_date, end_date, is_completed = line.split(", ")
                    print(f"""
                    Username: {task_name}
                    Title: {title}
                    description = {description}
                    Start date: {start_date}
                    End date: {end_date}
                    is_completed {is_completed}""")
                print("\nAll users below:")
                for line in user_file:
                    user_name, password = line.split(", ")
                    print(f"""
                    Username: {user_name}
                    Password: {password}
                    """)'''
            task_file.close()
            user_file.close()

    if choice == "e":
        print("Goodbye")
        break

# ********* Menu for normal user (not admin) *********
while True:
    choice = input("""
        Please select one of the following options:
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit
        """)

# ********* choice "a" not admin *********

# if user select "a". task_file will open "task.txt".
# Asked of the user to be entered by the user below
# The username of the person to whom the task is assign.
# The title of the task.
# A description of the task.
# The date that the task was assigned to the user.
# The due date for the task.

    if choice == "a":

        if user_name != "admin":
            print("error you are not admin")
        if user_name == "admin":
            task_file = open("tasks.txt", "a+")
            task_name = input("Enter the username of the assigned task:\n ")
            title = input("Enter the title of the task:\n ")
            description = input("Enter the desription of the task:\n ")
            start_date = input("Enter the start date the task was assigned to user (yyyy-mm-dd):\n ")
            end_date = input("Enter the end date the task was assigned to user (yyyy-mm-dd):\n ")
            is_completed = input("Is the task completed: ")
            while True:
                try:
                    start_date = datetime.datetime.strptime(start_date, date_format)
                    end_date = datetime.datetime.strptime(end_date, date_format)
                    print(start_date, end_date)
                    break
                except ValueError:
                    print("Incorrect data format, should be yyyy-mm-dd")
                    start_date = input("Enter the start date the task was assigned to user (yyyy-mm-dd):\n ")
                    end_date = input("Enter the end date the task was assigned to user (yyyy-mm-dd):\n ")

            task_file.write(f"\n{task_name}, {title}, {description}, {start_date}, {end_date}, {is_completed}")
            task_file.close()

# ********* choice "va" not admin *********

# if user select "va". task_file will open "tasks.txt".
# for line in task_file the following will be assigned below: task_name, title, description, start_date, end_date, is_completed and by split by a comma in 'taks.txt'
# print into (f.format)
# task_file.close() is used to close and save files

    elif choice == "va":
        if user_name != "admin":
            task_file = open("tasks.txt", "r")
            for line in task_file:
                line_split = line.split(", ")
                print(f"""
                    Username: {line_split[0]}
                    Title: {line_split[1]}
                    description = {line_split[2]}
                    Start date: {line_split[3]}
                    End date: {line_split[4]}
                    is_completed {line_split[5]}""")
        if user_name == "admin": 
            task_file = open("tasks.txt", "r")  
            for line in task_file:
                line_split = line.split(", ")
                print(f"""
                    Username: {line_split[0]}
                    Title: {line_split[1]}
                    description = {line_split[2]}
                    Start date: {line_split[3]}
                    End date: {line_split[4]}
                    is_completed {line_split[5]}""")
        task_file.close()

# ********* choice "vm" not admin *********
# task_file.close() is used to close and save files

    elif choice == "vm":
        if user_name != "admin":
            task_file = open("tasks.txt", "r")
            for line in task_file:
                line_split = line.split(", ")
                if line_split[0] == user_name:
                    print(f"""
                        Username: {line_split[0]}
                        Title: {line_split[1]}
                        description = {line_split[2]}
                        Start date: {line_split[3]}
                        End date: {line_split[4]}
                        is_completed {line_split[5]}""")
        elif user_name == "admin":
            task_file = open("tasks.txt", "r")
            for line in task_file:
                line_split = line.split(", ")
                if line_split[0] == user_name:
                    print(f"""
                        Username: {line_split[0]}
                        Title: {line_split[1]}
                        description = {line_split[2]}
                        Start date: {line_split[3]}
                        End date: {line_split[4]}
                        is_completed {line_split[5]}""")
        task_file.close()

    elif choice == "e":
        print("Goodbye")
        break