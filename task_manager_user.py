#=====importing libraries===========
'''This is the section where you will import libraries'''

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and password from the file
    - Use a while loop to validate your user name and password
'''
User_file = open("users.txt", "r+")

user_registration = User_file.readlines()

login = False


while login == False:
    username = input("Enter your name : ")
    password = input("Enter your password : ")

    for line in user_registration:
        valid_username, valid_password = line.strip('\n').split(', ')
        if valid_username == username and valid_password == password:
            login = True
        else:
            print("Invalid details! Check your username and password")       

if username != "admin":

    # Present the menu to the user.
    menu = input(
                """Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit""")
    
if username == "admin":
    menu = input(
                """Please select one of the following option: 
    r - register user
    a - add task
    va - view all tasks
    vm - view my tasks
    s - display statistics of total number of task and users in txt
    e - exit\n""")
    if menu == "s":
        task_file = open("tasks.txt", "r")
        user_file = open("users.txt", "r")
        print("\nAll tasks below:")
        for line in task_file:
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
            """)
        task_file.close()
        user_file.close()

    if menu == 'r':
        if username != "admin":
            print("error you not admin")
        if username == "admin":
            user_file = open("users.txt", "a+")#I will need to append add this to user text
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            confirm = input("Please confirm password: ")

        for line in user_file:
            valid_password, valid_confirm = line.split(", ")
        if password == confirm:
            user_file.write(f"\n{username}, {password}")
            print("Password match confirmed password")
            
        if login == False:
            print("Incorect details! confirmed password does not match password")
        user_file.close()
        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''

    if menu == 'a':
        task_file = open("tasks.txt", "a+")
        task_name = input("Enter the username of the assigned task: ")
        title = input("Enter the title of the task: ")
        description = input("Enter the desription of the task: ")
        start_date = input("Enter the start date the task was assigned to user: ")
        end_date = input("Enter the end date the task was assigned to user: ")
        is_completed = input("Is the task completed: ")

        task_file.write(f"\n{task_name}, {title}, {description}, {start_date}, {end_date}, {is_completed}")
        task_file.close()
    
    '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt'''
    if menu == 'va':
        task_file = open("tasks.txt", "r")

        for line in task_file:
            task_name, title, description, start_date, end_date, is_completed = line.split(", ")

            print(f"""
            Username: {task_name}
            Title: {title}
            description = {description}
            Start date: {start_date}
            End date: {end_date}
            is_completed {is_completed}""")
        task_file.close()
    '''This code block will read the task from task.txt file and
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Print result in correct format.
            - It is much easier to read a file using a for loop.'''

    if menu == 'vm':
        task_file = open("tasks.txt", "r")

        for line in task_file:
            task_name, title, description, start_date, end_date, is_completed = line.split(", ")

            if username == task_name:
                print(f"""
                Username: {username}
                Title: {title}
                description = {description}
                Start date: {start_date}
                End date: {end_date}
                is_completed {is_completed}""")
        task_file.close()
    '''This code block will read the task from task.txt file.
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.'''

    if menu == 'e':
        print('Goodbye!!!')
        exit()

