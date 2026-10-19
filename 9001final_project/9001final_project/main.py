from task import Task
from planner import planner


def main():
    study_planner = planner()
    study_planner.load_tasks("tasks.txt")

    while True:
        print("\n===== Smart Exam Study Planner =====")
        print("1. Add a study task")
        print("2. View all tasks")
        print("3. Delete a task")
        print("4. Mark a task as completed")
        print("5. Show progress summary")
        print("6. Generate today's study plan")
        print("7. Update study progress")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            subject = input("Enter subject: ")
            description = input("Enter task description: ")

            try:
                estimated_time = int(input("Enter estimated time in minutes: "))
                progress = float(input("Enter current progress (0-100): "))
                difficulty = int(input("Enter difficulty level (1-5): "))

                if estimated_time <= 0:
                    print("Estimated time must be greater than 0.")
                elif progress < 0 or progress > 100:
                    print("Progress must be between 0 and 100.")
                elif difficulty < 1 or difficulty > 5:
                    print("Difficulty must be between 1 and 5.")
                else:
                    new_task = Task(
                        subject,
                        description,
                        estimated_time,
                        progress,
                        difficulty
                    )
                    study_planner.add_task(new_task)
                    print("Task added successfully.")

            except ValueError:
                print("Invalid input. Please enter numbers correctly.")

        elif choice == "2":
            study_planner.view_tasks()

        elif choice == "3":
            try:
                index = int(input("Enter task number to delete: "))
                study_planner.delete_task(index)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "4":
            try:
                index = int(input("Enter task number to mark as completed: "))
                study_planner.mark_task_completed(index)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "5":
            study_planner.show_progress_summary()

        elif choice == "6":
            try:
                available_time = int(input("Enter available study time in minutes: "))

                if available_time <= 0:
                    print("Available time must be greater than 0.")
                else:
                    study_planner.generate_study_plan(available_time)

            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "7":
            try:
                index = int(input("Enter task number to update: "))
                actual_time = int(input("Enter actual study time in minutes: "))

                if actual_time <= 0:
                    print("Actual time must be greater than 0.")
                else:
                    study_planner.update_task_progress(index, actual_time)

            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "8":
            study_planner.save_tasks("tasks.txt")
            print("Thank you for using Smart Exam Study Planner.")
            break

        else:
            print("Invalid choice. Please choose from 1 to 8.")


main()