## IMPROVED CODE
def input_task():
    print('\nComandos: listar, desfazer, refazer')
    task = input('Digite uma tarefa ou comando: ')
    return task

def task_to_list(task, task_list):
    task_list.append(task)
    return task_list 

def show_tasks(task_list):
    print()
    for task in task_list:
        print(task)

def undo(task_list, undo_list):
    if len(task_list) > 0:
        removed_task = task_list.pop()
        undo_list.append(removed_task)  
    else:
        print('\nNada para desfazer')
    return task_list, undo_list
        
def redo(undo_list, task_list):
    if len(undo_list) > 0:
        removed_task = undo_list.pop()
        task_list.append(removed_task)  
    else:
        print('\nNada para refazer')
    return undo_list, task_list
        
def main():
    db_tasks = []
    db_undo = []

    while True:
        task = input_task()
    
        if task.lower() == 'listar':
            show_tasks(db_tasks)        
        elif task.lower() == 'desfazer':
            db_tasks, db_undo = undo(db_tasks, db_undo)
        elif task.lower() == 'refazer':
            db_undo, db_tasks = redo(db_undo, db_tasks)
        elif task.lower() == 'sair':
            break
        else:
            db_tasks = task_to_list(task, db_tasks)

if __name__ == '__main__':
    main()

# ## OLD WAY 

# def input_task():
#     print('\nComandos: listar, desfazer, refazer')
#     task = input('Digite uma tarefa ou comando: ')
#     return task

# def task_to_list(str, list=None):
#     if list == None:        
#         list = []
        
#     list.append(str)
#     return list 

# def show_tasks(list):
#     print()
#     for task in list:
#         print(task)

# def undo(list1,list2):
#     if len(list1) > 0:
#         remove = list1.pop()
#         list2.append(remove)  
#     else:
#         print('\nNada para desfazer')
        
# def redo(list_undo,list_task):
#     if len(list_undo) > 0:
#         remove = list_undo.pop()
#         list_task.append(remove)  
#     else:
#         print('\nNada para refazer')
        
# db_tasks = []
# db_undo = []

# while True:
#     task = input_task()
    
#     if task.lower() == 'listar':
#         show_tasks(db_tasks)        
#     elif task.lower() == 'desfazer':
#         undo(db_tasks,db_undo)
#     elif task.lower() == 'refazer':
#         undo(db_undo,db_tasks)
#     elif task.lower() == 'sair':
#         break
#     else:
#         task_to_list(task, db_tasks)
    
    
    

