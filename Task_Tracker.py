import json
import time
import os


if os.path.exists('tasks.json'):
    with open('tasks.json', 'r') as file:
        all_task = json.load(file)
else:
    all_task = []
def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(all_task, file, indent=4)

def add_task():
    task = input('Please enter a task: ')
    state = int(input('Is it complete(1) / Due (2): /in progress (3): '))
    task_id = len(all_task) + 1
    if state == 1:
        state = 'Finished'
    elif state == 2:
        state = 'Due'
    elif state == 3:
        state = 'Progression'
    else:
        print('Enter a valid number')

    new_task = {
        'id':task_id,
        'task':task,
        'state':state
        }
    all_task.append(new_task)
    save_tasks()
    show_all()
    

def show_all():
    print('Here are all the tasks')
    print('=====================')
    print('')
    for x in all_task:
        
        print(f"ID: {x['id']}")
        print(f"Task: {x['task']}")
        print(f"State: {x['state']}")
        print('')
    if len(all_task) == 0:
        print('Theres no task left!')

def update_task():
    show_all()
    update = int(input('Please enter the id of your task: '))
    for x in all_task:
        if update == x['id']:
            x['task'] = input('Please enter a task: ')
            x['state'] = int(input('Is it complete(1) / Due (2): /in progress (3): '))
            if x['state'] == 1:
                x['state'] = 'Finished'
            elif x['state'] == 2:
                x['state'] = 'Due'
            elif x['state'] == 3:
                x['state'] = 'Progression'
            else:
                print('Enter a valid number')
            save_tasks()
            show_all()
def delet_task():
    show_all()
    remove = int(input('Enter id of task u want to remove: '))
    for x in all_task:
        del all_task[remove - 1]
    save_tasks()
    show_all()

def completed():
    print('Here are all the completed tasks')
    print('=====================')
    print('')
    for x in all_task:
        if x['state'] == 'Finished':
            print(x['task'])
def unfinished():
    print('Here are all the unfinished tasks')
    print('=====================')
    print('')
    for x in all_task:
        if x['state'] == 'Progression':
            print(x['task'])
def progress():
    print('Here are all the tasks inprogress')
    print('=====================')
    print('')
    for x in all_task:
        if x['state'] == 'Due':
            print(x['task'])
def mark(): 
    show_all()
    marked = int(input('Enter id of task to Mark'))
    for x in all_task:
        if marked == x['id']:
            x['state'] = int(input('Is it complete(1) /in progress (2): '))
            if x['state'] == 1:
                x['state'] = 'Finished'
            elif x['state'] == 2:
                x['state'] = 'Progression'
            else:
                print('Enter a valid number')
    save_tasks()
    show_all()


while True:
    menu = int(input('''
1.add task
2.update a task
3.delet a task
4.Mark task
5.list all task
6.list all completed task
7.list unfinished task
8.list all task in progress
9.exit

'''))
    
    
    if menu == 1:
        add_task()
        time.sleep(3)
    elif menu == 2:
        update_task()
        time.sleep(3)
    elif menu == 3:
        delet_task()
        time.sleep(3)
    elif menu == 4:
        mark()
        time.sleep(3)
    elif menu == 5:
        show_all()
        time.sleep(3)
    elif menu == 6:
        completed()
        time.sleep(3)
    elif menu == 7:
        unfinished()
        time.sleep(3)
    elif menu == 8:
        progress()
        time.sleep(3)
    else:
        break

    
