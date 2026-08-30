# Polygon Area Calculator

A Python project completed as part of the **freeCodeCamp Python curriculum**.

## Overview

The Polygon Area Calculator uses object-oriented programming to represent rectangles and squares and perform calculations based on their dimensions.

The project defines a `Rectangle` class containing common shape operations and a `Square` subclass that inherits from `Rectangle` while modifying its behaviour to maintain equal width and height.

## Concepts Practiced

* Object-oriented programming
* Classes and objects
* Inheritance
* Method overriding
* Polymorphism
* Instance attributes
* Constructors
* Instance methods
* Special methods such as `__str__()`
* Loops
* Conditional logic
* Integer division
* Mathematical calculations
* Using Python's `math` module
* Type hints

## Classes

### `Rectangle`

Represents a rectangle using its width and height.

It provides methods to:

* Change the width and height
* Calculate the area
* Calculate the perimeter
* Calculate the diagonal
* Generate a text representation of the shape
* Determine how many instances of another shape can fit inside it

### `Square`

`Square` inherits from `Rectangle`.

It modifies the behaviour of the width and height setters so that changing either dimension keeps both dimensions equal.

It also provides a `set_side()` method for changing both dimensions simultaneously.

## Features

* Calculate the area of a rectangle or square
* Calculate the perimeter
* Calculate the diagonal
* Generate an ASCII representation of a shape
* Prevent oversized shapes from being displayed as pictures
* Modify shape dimensions
* Determine how many smaller shapes can fit inside a larger shape
* Represent rectangles and squares as readable strings

## Example

```python
rect = Rectangle(10, 5)

print(rect.get_area())

rect.set_height(3)

print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)

print(sq.get_area())

sq.set_side(4)

print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)

print(rect.get_amount_inside(sq))
```

### Example Output

```text
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```

## Inheritance

`Square` inherits from `Rectangle`:

```python
class Square(Rectangle):
    ...
```

This allows `Square` to reuse methods such as `get_area()`, `get_perimeter()`, `get_diagonal()`, and `get_picture()` while overriding methods whose behaviour must be different for a square.

For example, changing the width of a square also changes its height:

```python
def set_width(self, width):
    self.width = width
    self.height = width
```

## Status

**Completed**

This Polygon Area Calculator was completed as part of the freeCodeCamp Python curriculum.
