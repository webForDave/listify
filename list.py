def main():
    menu()


def menu():
    while True:
        try:
            print('''
                Main menu
                1. Add a new task
                2. View all tasks
                3. Delete a task
                4. Exit
                ''')
            user_input = int(input('Choose an option by entering a number from the menu: ').strip())

            if user_input == 4:
                break
            elif user_input == 1:
                add_task()
            elif user_input == 2:
                view_tasks(all_tasks)
            elif user_input == 3:
                delete_task(all_tasks)
        except ValueError:
            break

    
all_tasks = []

def add_task():
    '''
    Prompts user for task details.

    returns task added to task_list
    '''
    while True:
        try:
            print('\n')
            task_title = input('Task title: ').strip()
            task_description = input('Task description (optional): ').strip()
            task_priority = input('Task priority: ').strip()

            if task_title == '':
                continue
            elif task_priority == '':
                continue
            else:
                break
        except EOFError:
            break
    
    all_tasks.append({'title': task_title, 'description': task_description, 'priority': task_priority})
    return all_tasks


def view_tasks(tasks):
    for task in tasks:
        for value in task.values():
            print(value)
        print()



def delete_task(tasks):
    del_index = int(input('What item do you want to delete? Enter item number: ').strip())
    del(tasks[del_index])
    return tasks




if __name__ == '__main__':
    main()