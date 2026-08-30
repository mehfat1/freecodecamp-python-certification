Absolutely, Sera. For this one, I'd make the README specifically highlight **encapsulation and properties**, because that's the point of the exercise and the strongest part of your implementation.

Create:

```text
exercises/
└── oop/
    └── salary-tracker/
        ├── salary_tracker.py
        └── README.md
```

Then use this:

# Salary Tracker

A Python exercise from the freeCodeCamp Python curriculum focused on **encapsulation, properties, getters, and setters**.

## Overview

The Salary Tracker models employees with different career levels and corresponding base salaries.

The `Employee` class controls access to an employee's name, level, and salary through Python properties. Validation is performed whenever these attributes are created or modified.

The program also prevents invalid promotions and ensures that an employee's salary cannot fall below the minimum salary associated with their current level.

## Concepts Practiced

* Object-oriented programming
* Classes and objects
* Encapsulation
* Properties
* Getters using `@property`
* Setters using `@property.setter`
* Private-by-convention attributes using `_`
* Attribute validation
* Type checking
* Raising `TypeError`
* Raising `ValueError`
* Dictionary-based data storage
* Special methods: `__str__()` and `__repr__()`

## Employee Levels

The `Employee` class defines base salaries for four career levels:

| Level     | Base Salary |
| --------- | ----------- |
| Trainee   | $1,000      |
| Junior    | $2,000      |
| Mid-level | $3,000      |
| Senior    | $4,000      |

## Features

* Create employees with a name and career level
* Automatically assign a base salary according to the employee's level
* Validate employee names
* Validate career levels
* Validate salary values
* Prevent employees from being demoted
* Prevent selecting the same level twice
* Prevent salaries from falling below the minimum for the employee's level
* Automatically update salary when an employee is promoted

## Example

```python
charlie_brown = Employee('Charlie Brown', 'trainee')

print(charlie_brown)
print(f'Base salary: ${charlie_brown.salary}')

charlie_brown.level = 'junior'
```

### Example Output

```text
'name' updated to 'Charlie Brown'.
Salary updated to $1000.
'Charlie Brown' promoted to 'trainee'.
Charlie Brown: trainee
Base salary: $1000
Salary updated to $2000.
'Charlie Brown' promoted to 'junior'.
```

## Encapsulation

The exercise uses properties to control how employee attributes are accessed and modified.

For example, the `salary` property validates new salary values before allowing them to be stored:

```python
@property
def salary(self):
    return self._salary

@salary.setter
def salary(self, new_salary):
    ...
```

The underlying attributes use a single underscore, such as `_name`, `_level`, and `_salary`, indicating that they are intended for internal use within the class.

## Status

Completed as a progress exercise while working through the **Object-Oriented Programming** section of the freeCodeCamp Python curriculum.
