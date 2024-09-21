# Program to create a to-do list and mark tasks as completed by removing them

todo_list = []

num_tasks = int(input("Enter the number of tasks in your to-do list: "))
for i in range(num_tasks):
    task = input(f"Enter task {i + 1}: ")
    todo_list.append(task)

print("\nCurrent To-Do List:")
for task in todo_list:
    print(task)

task_to_remove = input("\nEnter the task you want to mark as completed: ")
if task_to_remove in todo_list:
    todo_list.remove(task_to_remove)
    print(f"\n'{task_to_remove}' has been marked as completed.")
else:
    print(f"\n'{task_to_remove}' is not in the to-do list.")

print("\nUpdated To-Do List:")
for task in todo_list:
    print(task)
