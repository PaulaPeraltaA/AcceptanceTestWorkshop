# todo_list.py
to_do_list = []

def add_task(task):
    to_do_list.append(task)

if __name__ == "__main__":
    add_task("Ejemplo de tarea")
    print(to_do_list)
