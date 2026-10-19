class Task:
    def __init__(self, subject, description, estimated_time,progress, difficulty):

        self.subject = subject
        self.description = description
        self.estimated_time = estimated_time
        self.progress = progress
        self.difficulty = difficulty

        # 默认未完成
        self.completed = False

        # 如果进度已经100%，自动完成
        if self.progress >= 100:
            self.progress = 100
            self.completed = True

    # 计算 Need Score
    def calculate_need_score(self):
        score = 0.5 * (100 - self.progress) + \
                0.5 * (self.difficulty * 20)

        return round(score, 2)

    # 标记任务完成
    def mark_completed(self):
        self.progress = 100
        self.completed = True

    # 更新学习进度
    def update_progress(self, actual_time):

        added_progress = (
            actual_time / self.estimated_time
        ) * 100

        self.progress += added_progress

        # 防止超过100%
        if self.progress >= 100:
            self.progress = 100
            self.completed = True

    # 返回任务信息（用于 print）
    def display_task(self):

        status = "Completed"

        if not self.completed:
            status = "Incomplete"

        print(f"Subject: {self.subject}")
        print(f"Description: {self.description}")
        print(f"Estimated Time: {self.estimated_time} mins")
        print(f"Progress: {self.progress:.1f}%")
        print(f"Difficulty: {self.difficulty}")
        print(f"Need Score: {self.calculate_need_score()}")
        print(f"Status: {status}")

    # 转换为文件保存格式
    def to_file_string(self):

        return (
            f"{self.subject}|"
            f"{self.description}|"
            f"{self.estimated_time}|"
            f"{self.progress}|"
            f"{self.difficulty}|"
            f"{self.completed}"
        )
    
    def __str__(self):
        status = "Completed" if self.completed else "Incomplete"

        if self.completed == False:
            status = "Incomplete"

        return (
            f"{self.subject} - {self.description} | "
            f"Time: {self.estimated_time} mins | "
            f"Progress: {self.progress:.1f}% | "
            f"Difficulty: {self.difficulty} | "
            f"Need Score: {self.calculate_need_score()} | "
            f"Status: {status}"
        )