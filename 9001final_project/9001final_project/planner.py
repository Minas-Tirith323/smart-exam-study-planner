from task import Task

class planner:
    def __init__ (self):
        self.tasks = []

    def add_task(self,task):
        self.tasks.append(task)

    def delete_task(self,index):
        if index <=0 or index > len(self.tasks):
            print("Invalid input.")
        else:
            removed_task = self.tasks.pop(index - 1)
            print(f'Remove task:{removed_task}')

    def view_tasks(self):
        if len(self.tasks) <= 0:
            print("No task found.")
        else: 
            for i in range(len(self.tasks)):
                print(f'{i+1}.{self.tasks[i]}')

    def generate_study_plan(self,available_time):
        incomplete_tasks = []
        for task in self.tasks:
            if task.completed == False: 
                incomplete_tasks.append(task)
        
        incomplete_tasks.sort(
        key=lambda task: task.calculate_need_score(),reverse=True
        )

        total_time = 0
        study_plan = []

        for task in incomplete_tasks:
            if total_time + task.estimated_time <= available_time:
                study_plan.append(task)
                total_time += task.estimated_time
        
        if len(study_plan) == 0:
            print('No study task. Enjoy your time!')
        else:
            print("Today's study plan: ")
            for i in range(len(study_plan)):
                print(i + 1, study_plan[i])

        print("Total planned time:", total_time, "mins")

    def mark_task_completed(self, index):
        if index < 1 or index > len(self.tasks):
            print("Invalid task number.")
        else:
            self.tasks[index - 1].mark_completed()
        print("Task marked as completed.")

    def show_progress_summary(self):
        total_tasks = len(self.tasks)
        completed_tasks = 0
        remaining_time = 0

        for task in self.tasks:
            if task.completed == True:
                completed_tasks += 1
            else:
                remaining_time += task.estimated_time

        incomplete_tasks = total_tasks - completed_tasks

        if total_tasks == 0:
            completion_rate = 0
        else:
            completion_rate = (completed_tasks / total_tasks) * 100

        print("===== Progress Summary =====")
        print("Total tasks:", total_tasks)
        print("Completed tasks:", completed_tasks)
        print("Incomplete tasks:", incomplete_tasks)
        print("Completion rate:",round(completion_rate, 1),"%")

        print("Remaining study time:",remaining_time,"mins")

    def update_task_progress(self, index, actual_time):
        if index < 1 or index > len(self.tasks):
            print("Invalid task number.")
        else:
            self.tasks[index - 1].update_progress(actual_time)

        print("Task progress updated.")

    def save_tasks(self, filename):
        file = open(filename, "w")

        for task in self.tasks:
            file.write(task.to_file_string() + "\n")

        file.close()
        print("Tasks saved successfully.")

    def load_tasks(self, filename):
        try:
            file = open(filename, "r")

            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split("|")

                subject = parts[0]
                description = parts[1]
                estimated_time = int(parts[2])
                progress = float(parts[3])
                difficulty = int(parts[4])
                completed = parts[5] == "True"

                task = Task(
                    subject,
                    description,
                    estimated_time,
                    progress,
                    difficulty
                )

                task.completed = completed

                self.tasks.append(task)

            file.close()
            print("Tasks loaded successfully.")

        except FileNotFoundError:
            print("No saved task file found. Starting with an empty planner.")





