class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f'Task "{description}" added successfully.')

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print(f'Task "{self.tasks[index].description}" marked as completed.')
        else:
            print('Invalid task index.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks available.')
        else:
            print('Tasks:')
            for i, task in enumerate(self.tasks):
                status = 'Completed' if task.completed else 'Pending'
                print(f'{i + 1}. {task.description} - {status}')

def main():
    task_manager = TaskManager()

    while True:
        print('\nTask Manager Menu:')
        print('1. Add Task')
        print('2. Mark Task as Completed')
        print('3. View Tasks')
        print('4. Exit')

        choice = input('Enter your choice (1-4): ')

        if choice == '1':
            description = input('Enter task description: ')
            task_manager.add_task(description)
        elif choice == '2':
            index = int(input('Enter task index to mark as completed: '))
            task_manager.mark_completed(index - 1)  # Adjust index to start from 1
        elif choice == '3':
            task_manager.view_tasks()
        elif choice == '4':
            print('Exiting Task Manager. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 4.')

if __name__ == '__main__':
    main()
