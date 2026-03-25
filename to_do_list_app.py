import json
from datetime import datetime
import os
def creating_task_user():
    global file_name
    now=datetime.now()
    task_list={
        'number':'',
        'topic':'',
        'description':'',
        'date':'',
        'STATUS':'NOT done'
    }
    user_input_task_topic=input('write your task TOPIC-')
    user_input_task_decription=input('write your task description\nwhat you should do-')
    task_list['topic']=user_input_task_topic
    task_list['description']=user_input_task_decription
    task_list['date']=now.strftime("%Y-%m-%d %H:%M:%S")
    if os.path.exists(file_name) and os.path.getsize(file_name)>0:
    return task_list
def create_task(file_name):
    task=creating_task_user()
    if os.path.exists(file_name) and os.path.getsize(file_name)>0:
        with open(file_name,'r') as f:
            data=read_file=json.load(f)
    else:
        data=[]
    data.append(task)
    with open(file_name,'w') as f:
        write_file=json.dumps(data,indent=2)
        f.write(write_file)
    print('Done!')
    print((json.dumps(data,indent=4)))
def delete_task(file_name):
    pass
def clear_list(file_name):
    with open(file_name,'w') as f:
        json.dump({},f)
        print('LIST IS CLEAR')
def see_list(file_name):
    print(json.dumps(file_name,indent=2))
file_name='tasks_list_data.json'
print('Hello its a todolist app at python')
print('Enter what you want to do\n 1.Create a new task \n 2.Delete a Task \n 3.See all tasks \n 4.Clear whole list ')
user_input=int(input())
if user_input==1:
    create_task(file_name)
elif user_input==2:
    delete_task()
elif user_input==3:
    see_list(file_name)
elif user_input==4:
    clear_list(file_name)
