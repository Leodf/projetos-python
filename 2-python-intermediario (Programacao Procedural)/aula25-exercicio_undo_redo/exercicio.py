"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefa
    opção de desfazer
    opção de refazer
"""
""" minha solução incompleta
lista = []
while True:
    print('#'*50)
    print('Programa de listagem de tarefas')
    print('para adicionar uma tarefa pressione [a]')
    print('para listar as tarefas pressione [l]')
    print('para desfazer um item pressione [d]')
    print('para refazer o item pressione [r]')
    valor = input('digite o comando desejado: ')
    if valor == 'a':
        lista.append(input('Adicione uma tarefa: '))
    elif valor == 'l':
        print(lista)
    elif valor == 'd':
        lista.pop()
        print(f'você desfez o item {lista[-1]}')
    elif valor == 'r':
        print(f'você refez o item {lista[-1]}')
    else:
        print('comando inválido, tente novamnte!!!!')
"""

def show_op(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()

def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a desfazer')
        return
    
    last_todo = todo_list.pop()
    redo_list.append(last_todo)

def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer')
        return
    
    last_redo = redo_list.pop()
    todo_list.append(last_redo)

def do_add(todo, todo_list):
    todo_list.append(todo)

if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite uma tarefa ou undo, redo, ls: ')

        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list, redo_list)
            continue
        elif todo == 'redo':
            do_redo(todo_list, redo_list)
            continue
        do_add(todo, todo_list)
        
        