from behave import given, when, then

to_do_list = []

@given('the to-do list is empty')
def step_impl(context):
    context.to_do_list = []

@when('the user adds the task "{task}"')
def step_impl(context, task):
    context.to_do_list.append(task)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    assert task in context.to_do_list, f'Task "{task}" not found in the to-do list'

@given('the to-do list contains:')
def step_impl(context):
    context.to_do_list = [row['Task'] for row in context.table]

@when('the user lists all tasks')
def step_impl(context):
    context.result = context.to_do_list

@then('the output should contain:')
def step_impl(context):
    for row in context.table:
        assert row['Task'] in context.result

@when('the user marks the task "{task}" as completed')
def step_impl(context, task):
    for i, t in enumerate(context.to_do_list):
        if t == task:
            context.to_do_list[i] = f"{task} (Completed)"

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    assert f"{task} (Completed)" in context.to_do_list

@when('the user clears the to-do list')
def step_impl(context):
    context.to_do_list = []

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.to_do_list) == 0

@when('the user searches for the task "{task}"')
def step_impl(context, task):
    context.search_result = task in context.to_do_list

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    assert task in context.to_do_list

@when('the user updates the task "{old_task}" to "{new_task}"')
def step_impl(context, old_task, new_task):
    for i, t in enumerate(context.to_do_list):
        if t == old_task:
            context.to_do_list[i] = new_task

@then('the to-do list should contain "{new_task}"')
def step_impl(context, new_task):
    assert new_task in context.to_do_list
