class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "status": "Pending"})

    def list_tasks(self):
        return self.tasks

    def mark_task_completed(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["status"] = "Completed"
                return True
        return False

    def clear_tasks(self):
        self.tasks = []

    def search_task(self, task):
        return any(t["task"] == task for t in self.tasks)

    def update_task(self, old_task, new_task):
        for t in self.tasks:
            if t["task"] == old_task:
                t["task"] = new_task
                return True
        return False


if __name__ == "__main__":
    todo_list = ToDoList()
    
    # Example usage:
    todo_list.add_task("Buy milk")
    print(todo_list.list_tasks())  # [{'task': 'Buy milk', 'status': 'Pending'}]
    todo_list.mark_task_completed("Buy milk")
    print(todo_list.list_tasks())  # [{'task': 'Buy milk', 'status': 'Completed'}]
    todo_list.add_task("Pay bills")
    todo_list.update_task("Pay bills", "Pay electricity bills")
    print(todo_list.list_tasks())  # [{'task': 'Buy milk', 'status': 'Completed'}, {'task': 'Pay electricity bills', 'status': 'Pending'}]
    todo_list.clear_tasks()
    print(todo_list.list_tasks())  # []
