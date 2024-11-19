# To-Do List

tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter a task: ")
        tasks.append(task)
    elif choice == '2':
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    elif choice == '3':
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
        else:
            print("Invalid task number.")
    elif choice == '4':
        break
    else:
        print("Invalid choice.")
