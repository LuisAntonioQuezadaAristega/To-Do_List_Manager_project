class task:

    def __init__(self, name, description, state, end_day):
        self.name = name
        self.description = description
        self.state = state
        self.end_day = end_day

    def set_state(self, state):
        self.state = state


class list:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        for index in range(len(self.tasks)):
            print((self.tasks[index]).name)

    # Feature added
    def get_task(self, name):
        for index in range(len(self.tasks)):
            if (self.tasks[index]).name == name:
                return self.tasks[index]
        return -1

    def task_complete(self, name):
        task = self.get_task(name)
        if task == -1:
            print("Task don´t exist.")
            return -1
        print("State of task changed.")
        task.set_state("Complete")
        return 0

    # Feature added
    def tasks_unfinished(self):
        total = 0
        for index in range(len(self.tasks)):
            if (self.tasks[index]).state != "Complete":
                total += 1
        print("there are", total, "tasks unfinished")

    def clear(self):
        self.tasks.clear()


def main():

    to_do_list = list()

    task1 = task("name", "desc", "in progress", "January 12")

    to_do_list.add_task(task1)

    to_do_list.task_complete("name")

    to_do_list.tasks_unfinished()

    to_do_list.show_tasks()

    to_do_list.clear()

    to_do_list.show_tasks()

    to_do_list.task_complete("name")


if __name__ == "__main__":
    main()
