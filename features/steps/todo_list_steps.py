from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list is empty')
def step_impl(context):
    context.todo_list = ToDoList()

@when('the user adds the task "{task}"')
def step_impl(context, task):
    context.todo_list.add_task(task)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    assert any(t["task"] == task for t in context.todo_list.list_tasks()), f'Task "{task}" not found in the to-do list'

@given('the to-do list contains:')
def step_impl(context):
    context.todo_list = ToDoList()
    for row in context.table:
        context.todo_list.add_task(row['Task'])

@when('the user lists all tasks')
def step_impl(context):
    context.result = context.todo_list.list_tasks()

@then('the output should contain:')
def step_impl(context):
    tasks = [row['Task'] for row in context.table]
    for task in tasks:
        assert any(t["task"] == task for t in context.result)

@when('the user marks the task "{task}" as completed')
def step_impl(context, task):
    context.todo_list.mark_task_completed(task)

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    assert any(t["task"] == task and t["status"] == "Completed" for t in context.todo_list.list_tasks())

@when('the user clears the to-do list')
def step_impl(context):
    context.todo_list.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo_list.list_tasks()) == 0

@when('the user searches for the task "{task}"')
def step_impl(context, task):
    context.search_result = context.todo_list.search_task(task)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    assert context.search_result

@when('the user updates the task "{old_task}" to "{new_task}"')
def step_impl(context, old_task, new_task):
    context.todo_list.update_task(old_task, new_task)

@then('the to-do list should contain "{new_task}"')
def step_impl(context, new_task):
    assert any(t["task"] == new_task for t in context.todo_list.list_tasks())
