"""
Week 3 Task: Pseudo-Coding Project
Project: Simple To-Do List Manager

Purpose:
A beginner-friendly command-line program that lets users add, view,
complete, and remove tasks. The program demonstrates how pseudocode
can be translated into working Python code.

Run:
    python todo_list.py
"""

def display_menu():
    """Show the actions available to the user."""
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark a task as complete")
    print("4. Remove a task")
    print("5. Exit")


def view_tasks(tasks):
    """Display all tasks, including their completion status."""
    if not tasks:
        print("\nYour to-do list is empty.")
        return

    print("\nYour tasks:")
    for number, task in enumerate(tasks, start=1):
        status = "Complete" if task["completed"] else "Pending"
        print(f"{number}. [{status}] {task['title']}")


def add_task(tasks):
    """Ask for a task title and add it if the input is not blank."""
    title = input("Enter the task: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    tasks.append({"title": title, "completed": False})
    print(f"Task added: {title}")


def mark_task_complete(tasks):
    """Mark a selected task as completed."""
    if not tasks:
        print("There are no tasks to complete.")
        return

    view_tasks(tasks)
    choice = input("Enter the task number to mark complete: ").strip()

    if not choice.isdigit():
        print("Please enter a valid whole-number task number.")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(tasks):
        print("That task number does not exist.")
        return

    tasks[index]["completed"] = True
    print(f"Marked as complete: {tasks[index]['title']}")


def remove_task(tasks):
    """Remove a selected task from the list."""
    if not tasks:
        print("There are no tasks to remove.")
        return

    view_tasks(tasks)
    choice = input("Enter the task number to remove: ").strip()

    if not choice.isdigit():
        print("Please enter a valid whole-number task number.")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(tasks):
        print("That task number does not exist.")
        return

    removed = tasks.pop(index)
    print(f"Removed task: {removed['title']}")


def main():
    """Control the application until the user chooses to exit."""
    tasks = []

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Thank you for using the To-Do List Manager.")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
