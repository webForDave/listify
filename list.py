def main():
    if prompt() == 2:
        return add_task()

tasks = []

def prompt():

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

    while True:
        try:
            return int(input('Select an option: '))
        except ValueError:
            continue
        except KeyboardInterrupt:
            break



def add_task():
    description = input('Enter the task description: ').strip()
    date = input('Enter the due date (optional, format YYYY-MM-DD): ')
    tasks.append(f'{description} (Due: {date})')

    print('\nTask added successfully!')
    return 'Run program for list of options.'


if __name__ == '__main__':
    print(main())