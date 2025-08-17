#Household Task Tracker
household_task = [] #list for household task

#to add a new task
def add_task():
    task_name = input("Enter a new task : ")
    household_task.append({"task" : task_name, "completed" : False})
    print("task added successfully!")


#to view task
def view_task():
    if not household_task:
        print("No tasks found.")
    else:
        print("\nYour Household Tasks:")
        for index, task in enumerate(household_task, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{index}. {task['task']} - {status}")

#Mark a task as completed
def completed_task():
    view_task()
    if not household_task:
        return #exit if no tasks to complete
    try:
        task_num = int(input("Enter the number of the task you completed: "))
        if 1 <= task_num <= len(household_task):
            household_task[task_num - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

#Menu to interact with the program
def show_menu():
    while True:
        print("\nMenu")
        print("1. Add task")
        print("2. View task")
        print("3. Complete task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            completed_task()
        elif choice == "4":
            print("Thank You for using the Task Management!")
            break
        else:
            print("Invalid choice. Please enter a number from 1-4")

#Start the Program
show_menu()


        

        




            

            


