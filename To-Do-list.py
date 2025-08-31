# Using lists, dictionaries, loops, conditionals
def show_tasks(tasks_list):
    tasks_dict = {}
    for j in range(0, len(tasks_list), 1):
        task_key = "Task " + str(j + 1)
        tasks_dict.update({task_key: tasks_list[j]})
    print(tasks_dict)


print("\t👉 YOUR TO-DO LIST APP ✨")
tasks_for_month = []
tasks_for_week = []
tasks_for_today = []

user_choice = str(input("Do you want to create tasks for a whole month, week, or a single day? Enter 'day' or 'month' or 'week': "))

if user_choice == "month":
    print("Enter your day-by-day tasks as Day 1, Day 2 ... Day 30")
    for i in range(0, 30):
        task = str(input(f"Enter the task for Day {i + 1}: "))
        tasks_for_month.append(task)
        print("Your task has been added to the task list.")
    
    print("Your task list is full.")
    ask = str(input("Do you want to see your task list? (yes or no): "))
    if ask == "yes":
        show_tasks(tasks_for_month)
        action = str(input("Do you want to edit (type 'edit') or delete a specific task (type 'delete')? "))
        if action == "delete":
            idx = int(input("Which task number do you want to delete? (1, 2, 3...): "))
            tasks_for_month.pop(idx - 1) 
        if action == "edit":
            idx = int(input("Which task number do you want to edit? (1, 2, 3...): "))
            new_task = str(input("Enter the new task: "))
            tasks_for_month.insert(idx - 1, new_task)
        print("Here is your updated task list:")
        show_tasks(tasks_for_month)
    else:
        print("Okay, best of luck with your tasks!")

elif user_choice == "week":
    print("Enter your day-by-day tasks as Day 1, Day 2 ... Day 7")
    for i in range(0, 7):
        task = str(input(f"Enter the task for Day {i + 1}: "))
        tasks_for_week.append(task)
        print("Your task has been added to the task list.")
    
    print("Your task list is full.")
    ask = str(input("Do you want to see your task list? (yes or no): "))
    if ask == "yes":
        show_tasks(tasks_for_week)
        action = str(input("Do you want to edit (type 'edit') or delete a specific task (type 'delete')? "))
        if action == "delete":
            idx = int(input("Which task number do you want to delete? (1, 2, 3...): "))
            tasks_for_week.pop(idx - 1)
        if action == "edit":
            idx = int(input("Which task number do you want to edit? (1, 2, 3...): "))
            new_task = str(input("Enter the new task: "))
            tasks_for_week.insert(idx - 1, new_task)
        print("Here is your updated task list:")
        show_tasks(tasks_for_week)
    else:
        print("Okay, best of luck with your tasks!")

elif user_choice == "day":
    print("Do you want to create tasks per hour (type 'perhour') "
          "or do you want to set a specific number of tasks for the day (type 'tasknumber')?")
    
    user_choice2 = str(input("Enter your choice: "))
    if user_choice2 == "perhour":
        sleep_hours = int(input("How many hours do you sleep (including extra activities that don't need to be added)? "))
        remaining_hours = 24 - sleep_hours
        print(f"Enter {remaining_hours} tasks for the day, in sequence:")
        for i in range(0, remaining_hours, 1):
            task = str(input(f"Enter task {i + 1}: "))
            tasks_for_today.append(task)
    
    if user_choice2 == "tasknumber":
        print("Okay, so you want to specify the number of tasks.")
        task_count = int(input("Enter the number of tasks: "))
        sleep_hours = int(input("How many hours do you sleep (including extra activities that don't need to be added)? "))
        remaining_hours = 24 - sleep_hours
        per_hour = int(remaining_hours / task_count)
        print(f"We have set your tasks with a gap of {per_hour} hour(s).")
        for i in range(0, task_count):
            task = str(input(f"Enter task {i + 1}: "))
            tasks_for_today.append(task)
    
    see_list = str(input("Do you want to see your task list? (yes or no): "))
    if see_list == "yes":
        show_tasks(tasks_for_today)
        action = str(input("Do you want to edit (type 'edit') or delete a specific task (type 'delete')? "))
        if action == "delete":
            idx = int(input("Which task number do you want to delete? (1, 2, 3...): "))
            tasks_for_today.pop(idx - 1)
        if action == "edit":
            idx = int(input("Which task number do you want to edit? (1, 2, 3...): "))
            new_task = str(input("Enter the new task: "))
            tasks_for_today.insert(idx - 1, new_task)
        print("Here is your updated task list:")
        show_tasks(tasks_for_today)
    else:
        print("Alright, best of luck with your tasks!")

else:
    print("Please enter valid information.")
