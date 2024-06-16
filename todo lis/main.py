def display_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    tasks = []
    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            task = input("Enter a task: ")
            tasks.append(task)
            print("Task added.")
        elif choice == '2':
            display_tasks(tasks)
            task_num = int(input("Enter task number to remove: "))
            if 0 < task_num <= len(tasks):
                tasks.pop(task_num - 1)
                print("Task removed.")
            else:
                print("Invalid task number.")
        elif choice == '3':
            display_tasks(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
