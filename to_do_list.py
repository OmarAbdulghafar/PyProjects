tasks = []

def main():
    
    message = """1- add tasks to a list\n2- mark tasks as complete\n3- view tasks\n4- Quit """


    while True:
        print(message)
        choice = input("Enter your choice  ")
    
        if choice == "1":
            add_task()
        elif choice == "2":
         mark_task_complete()
        elif choice == "3":
            view_task()
        elif choice == "4":
         break
        else:
            print("_" * 20 + "\n")
            print("Invalid choice please Enter a number between 1 - 4")

def add_task():
    task = input("Enter task: ")
    task_info = { "Task": task, "Completed": False}
    tasks.append(task_info)
    print("Task added to a list successfuly")
    print("_" * 20)

    # print(tasks)

def mark_task_complete():
    incomplete_tasks = []
    for task in tasks:
        if task["Completed"] == False:
            incomplete_tasks.append(task)
    

    if incomplete_tasks:
        for i, task in enumerate(incomplete_tasks):
            print(f"{i+1}- {task['Task']} \n")
        print("_" * 20)
        task_num = int(input("choose the task to complete: \n"))

        incomplete_tasks[task_num -1]["Completed"] = True

        print("Task mark complete")
        print("_" * 20 + "\n")

    else:
        print("No task to mark as complete")
        print("_" * 20 + "\n")

def view_task():
    if not tasks:
        print("No tasks to view ")
    
    for i, task in enumerate(tasks):
        if task["Completed"]:
            status = " Done"
        else:
            status = "!"

        
        print(f"{i+ 1}. {task['Task']}  {status}")

    print("_" * 20)

main()

