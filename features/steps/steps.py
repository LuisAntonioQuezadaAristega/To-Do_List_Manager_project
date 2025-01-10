from behave import *
import main
# Define a list to represent the to-do list
to_do_list = main.list()

# Step 1: Given a to-do list that is emptyy
@given('a to-do list that is empty')
def step_impl(context):
    # Set the to-do list as an empty list
    global to_do_list
    to_do_list = main.list()

# Step 2: When the user adds a task "Buy groceries"
@when('the user adds a task "{task}"')
def step_impl(context, task):
    # Add the task to the to-do list
    global to_do_list
    to_do_list.add_task(main.task(task, "desc", "Pending", "January 12"))

# Step 3: Then the to-do list should contain "Buy groceries"
@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    # Check if the task is in the to-do list
    assert main.task(task, "desc", "Pending", "January 12") in to_do_list.tasks, f'Task "{task}" not found in the to-do list'

@given('the to-do list contains tasks:')
def step_impl(context):
    global to_do_list
    to_do_list = main.list()
    to_do_list.add_task(main.task("Buy groceries", "desc", "Pending", "January 12"))
    to_do_list.add_task(main.task("Pay bills", "desc", "Pending", "January 12"))

@when('the user lists all tasks')
def step_impl(context):
    to_do_list.show_tasks()

@then('the output should contain:')
def step_impl(context):
    assert main.task("Buy groceries", "desc", "Pending", "January 12") in to_do_list.tasks, f'Task "Buy groceries" not found in the to-do list'
    assert main.task("Pay bills", "desc", "Pending", "January 12") in to_do_list.tasks, f'Task "Pay bills" not found in the to-do list'

@given('the to-do list contains task:')
def step_impl(context):
    global to_do_list
    to_do_list = main.list()
    to_do_list.add_task(main.task("Buy groceries", "desc", "Pending", "January 12"))

@when('the user marks task "Buy groceries" as completed')
def step_impl(context):
    to_do_list.task_complete("Buy groceries")

@then('the to-do list should show task "Buy groceries" as completed')
def step_impl(context):
    assert main.task("Buy groceries", "desc", "Complete", "January 12") in to_do_list.tasks, f'Task "Buy groceries" is incomplete'

@given('to-do list contains tasks:')
def step_impl(context):
    global to_do_list
    to_do_list = main.list()
    to_do_list.add_task(main.task("Buy groceries", "desc", "Pending", "January 12"))
    to_do_list.add_task(main.task("Pay bills", "desc", "Pending", "January 12"))

@when('the user clears the to-do list')
def step_impl(context):
    to_do_list.clear()

@then('the to-do list should be empty')
def step_impl(context):
    assert main.task("Buy groceries", "desc", "Pending", "January 12") not in to_do_list.tasks, f'to-do list is not empty'
    assert main.task("Pay bills", "desc", "Pending", "January 12") not in to_do_list.tasks, f'to-do list is not empty'

@given('to-do list contains task:')
def step_impl(context):
    global to_do_list
    to_do_list = main.list()
    to_do_list.add_task(main.task("Buy groceries", "desc", "Pending", "January 12"))

@when('the user count the unfinished tasks')
def step_impl(context):
    to_do_list.tasks_unfinished()

@then('the output should be:')
def step_impl(context):
    assert 1 == to_do_list.tasks_unfinished(), f'There is not 1 unfinished task'

@given('a empty to-do list')
def step_impl(context):
    global to_do_list
    to_do_list = main.list()

@when('the user look for the task "Buy groceries"')
def step_impl(context):
    to_do_list.get_task("Buy groceries")

@then('the output should be -1')
def step_impl(context):
    assert -1 == to_do_list.get_task("Buy groceries"), f'There is a task named "Buy groceries"'