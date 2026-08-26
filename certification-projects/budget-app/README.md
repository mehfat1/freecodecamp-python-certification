# Budget App

A Python project completed as part of the **freeCodeCamp Python curriculum**.

## Overview

The Budget App is a Python program for managing money across different budget categories.

It allows users to deposit and withdraw funds, check balances, transfer money between categories, maintain transaction ledgers, and generate a visual spending chart showing the percentage of spending by category.

## Concepts Practiced

* Object-oriented programming (OOP)
* Classes and objects
* Constructors and instance attributes
* Methods
* Lists and dictionaries
* Loops and conditional logic
* String manipulation and formatting
* Data processing
* Function design
* Boolean return values
* Balance and transaction management
* Working with positive and negative values
* Generating formatted text output

## Main Components

### `Category`

The `Category` class represents an individual budget category and maintains its transaction ledger.

It provides methods to:

* Deposit money
* Withdraw money
* Check available funds
* Calculate the current balance
* Transfer money between categories
* Display the category ledger

### `create_spend_chart()`

The `create_spend_chart()` function calculates the percentage of total spending represented by each category and generates a vertical text-based chart.

## Features

* Create separate budget categories
* Record deposits
* Record withdrawals
* Track category balances
* Prevent withdrawals when sufficient funds are unavailable
* Transfer funds between categories
* Record transaction descriptions
* Maintain a transaction ledger
* Generate a spending percentage chart

## Example

The following test creates a main budget and transfers money into three spending categories:

```python
budget = Category('Budget')
food = Category('Food')
clothing = Category('Clothing')
auto = Category('Auto')

budget.deposit(1000, 'initial deposit')

budget.transfer(100, food)
budget.transfer(100, clothing)
budget.transfer(100, auto)

food.withdraw(60, 'groceries')
clothing.withdraw(20, 'clothes')
auto.withdraw(10, 'fuel')

print(create_spend_chart([food, clothing, auto]))
```

### Spending Distribution

The resulting spending is:

| Category | Amount Spent | Percentage |
| -------- | ------------ | ---------- |
| Food     | 60           | 60%        |
| Clothing | 20           | 20%        |
| Auto     | 10           | 10%        |

### Program Output

```text
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    -----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h  o  
        i     
        n     
        g     
```

The chart shows the percentage of total spending represented by each category. Food accounts for 60% of spending, Clothing for 20%, and Auto for 10%.

## Project Structure

```text
budget-app/
├── budget_app.py
└── README.md
```

## Certification Status

**Completed**

This project was completed as part of the freeCodeCamp Python curriculum.

## Technologies

* Python 3
* Python standard library
* Built-in Python data structures
