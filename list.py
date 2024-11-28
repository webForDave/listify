def main():
    return prompt()

tasks = []

def prompt():
    while True:
        try:
            print(
            """
            Welcome to PyTodo!
            Options:
            1. View tasks
            2. Add a new task
            3. Mark a task as complete
            4. Delete a task
            5. Exit
            """
            )
            prompt = int(input('Select an option: ').strip())
            if prompt == 5:
                return 'Exited!'
            elif prompt == 1:
                view_tasks(tasks)
            elif prompt == 2:
                add_new_task(tasks)
            elif prompt == 3:
                mark_complete(tasks)
            elif prompt == 4:
                delete_task(tasks)
        except ValueError:
            continue
        except KeyboardInterrupt:
            return 'Exited!'

def add_new_task(tasks):
    description = input('Enter the task description: ').strip()
    date = input('Enter the due date (optional, format YYYY-MM-DD): ').strip()

    tasks.append(f'{description} (Due: {date})')
    return 'Task added successfully!'


def view_tasks(tasks):
    if len(tasks) == 0:
        print('You do not have any task yet.')
    else:
        print('Here are your tasks: ')
        for index, task in enumerate(tasks, start=1):
            print(f'{index}.[] {task}')


def delete_task(tasks):
    id = int(input(('Which task would you like to delete? Enter the task number: ')))
    del tasks[id - 1]
    print('Task deleted successfully!')


def mark_complete(tasks):
    id = int(input('Which task would you like to mark as complete? Enter the task number:').strip())
    tasks[id - 1] = f'[X] {tasks[id - 1]}'


if __name__ == '__main__':
    print(main())