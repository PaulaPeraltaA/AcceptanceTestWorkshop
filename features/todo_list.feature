Feature: To-Do List Management

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds the task "Buy milk"
    Then the to-do list should contain "Buy milk"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains:
      | Task         |
      | Buy milk     |
      | Pay bills    |
    When the user lists all tasks
    Then the output should contain:
      | Buy milk     |
      | Pay bills    |

  Scenario: Mark a task as completed
    Given the to-do list contains:
      | Task         | Status   |
      | Buy milk     | Pending  |
    When the user marks the task "Buy milk" as completed
    Then the to-do list should show task "Buy milk" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains:
      | Task         |
      | Buy milk     |
      | Pay bills    |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Search for a task in the list
    Given the to-do list contains:
      | Task         |
      | Buy milk     |
    When the user searches for the task "Buy milk"
    Then the to-do list should contain "Buy milk"

  Scenario: Update the description of a task
    Given the to-do list contains:
      | Task         |
      | Buy milk     |
    When the user updates the task "Buy milk" to "Buy milk and eggs"
    Then the to-do list should contain "Buy milk and eggs"
