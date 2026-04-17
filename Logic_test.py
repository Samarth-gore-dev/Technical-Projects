# Internship Portfolio: Task Management Logic
# This script demonstrates list handling, loops, and conditional logic.

def show_tasks(task_list):
    print("\n--- Current Internship Tasks ---")
    if not task_list:
        print("No tasks assigned yet.")
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task}")

def main():
    # Initial list of tasks
    tasks = ["Update Portfolio", "Complete Python Logic", "Apply for Internships"]
    
    # Adding a new task dynamically
    new_task = "Prepare for Vexocore Interview"
    tasks.append(new_task)
    
    show_tasks(tasks)
    
    # Logic to check for a specific priority task
    priority = "Apply for Internships"
    if priority in tasks:
        print(f"\nPriority Alert: '{priority}' is on your list!")
    
    print("\nStatus: Logic executed successfully.")

if __name__ == "__main__":
    main()
