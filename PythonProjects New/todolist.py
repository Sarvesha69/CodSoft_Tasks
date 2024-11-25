# Simple To-Do List Program

tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Your Tasks")
    print("2. Add a new Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter the task: ")
    tasks.append(task)
    print(f"Added: '{task}' to your to-do list!")

def remove_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed: '{removed}' from your to-do list!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye! Happy tasking! 📝")
            break
        else:
            print("Invalid choice! Please pick a number between 1 and 4.")

if __name__ == "__main__":
    main()
