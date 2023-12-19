import os

def show_menu():
    print("\n===== To-Do List Menu =====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Exit")

def view_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\n===== To-Do List =====")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task(todo_list):
    task = input("\nEnter the task: ")
    todo_list.append(task)
    print(f'Task "{task}" added successfully.')

def mark_completed(todo_list):
    view_todo_list(todo_list)
    try:
        index = int(input("\nEnter the number of the task to mark as completed: ")) - 1
        if 0 <= index < len(todo_list):
            completed_task = todo_list.pop(index)
            print(f'Task "{completed_task}" marked as completed.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    todo_list = []

    while True:
        show_menu()

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            view_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            mark_completed(todo_list)
        elif choice == "4":
            print("\nExiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
