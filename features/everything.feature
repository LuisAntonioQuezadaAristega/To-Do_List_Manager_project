# language: en

Feature: Task and List functions

    Scenario: Add a task to the to-do list
        Given a to-do list that is empty
        When the user adds a task "Buy groceries"
        Then the to-do list should contain "Buy groceries"

    Scenario: List all tasks in the to-do list
        Given the to-do list contains tasks:
        | Buy groceries |
        | Pay bills |
        When the user lists all tasks
        Then the output should contain:
        - Buy groceries
        - Pay bills

    Scenario: Mark a task as completed
        Given the to-do list contains task:
        | Task | Status |
        | Buy groceries | Pending |
        When the user marks task "Buy groceries" as completed
        Then the to-do list should show task "Buy groceries" as completed

    Scenario: Clear the entire to-do list
        Given to-do list contains tasks:
        | Task |
        | Buy groceries |
        | Pay bills |
        When the user clears the to-do list
        Then the to-do list should be empty
    
    Scenario: Show the number of unfinished tasks
        Given to-do list contains task:
        | Task | Status |
        | Buy groceries | Pending |
        When the user count the unfinished tasks
        Then the output should be:
        - there are 1 task unfinished

    Scenario: Find a task in the to-do list
        Given a empty to-do list
        When the user look for the task "Buy groceries"
        Then the output should be -1