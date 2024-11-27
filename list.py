def main():
    print(prompt())


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


if __name__ == '__main__':
    print(main())