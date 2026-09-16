numlist = []

while True:
    print("\nTO-DO LIST:")

    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Exit\n")

    choice  = input("Please choose an option: ")

    if choice == "1":
        taskin = input("Enter a task: ").title()
        numlist.append(taskin)
        print("Task added!")

    if choice == "2":
        if not numlist:
            print("\nYou don't have a task yet, add one before removing a task.")
        else: 
            task_remove = int(input("Enter the number of the task you want to remove: ")) -1
            if 0 <= task_remove < len(numlist):
                removed_task = numlist.pop(task_remove)
            print("Task removed!")
    if choice == "3":
        if not numlist: 
            print("\nYou have no tasks yet!")

        for index, task in enumerate(numlist, start=1):
            print(f"{index}. {task}")

    if choice == "4":
        print("\nGoodbye!\n")
        break