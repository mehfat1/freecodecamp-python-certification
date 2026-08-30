# Discount Calculator

A Python exercise from the freeCodeCamp Python curriculum focused on **abstraction, inheritance, and polymorphism**.

## Overview

The Discount Calculator uses different discount strategies to determine the best available price for a product.

An abstract `DiscountStrategy` class defines the common interface for discount strategies, while different subclasses implement their own rules for determining whether a discount applies and how it is calculated.

The `DiscountEngine` evaluates all applicable strategies and selects the lowest resulting price.

## Concepts Practiced

* Object-oriented programming
* Abstract base classes
* Abstraction
* Inheritance
* Polymorphism
* Method overriding
* `ABC` and `@abstractmethod`
* Type hints
* Lists and list comprehensions
* Conditional logic
* Strategy-based program design
* Working with floating-point values

## Classes

### `Product`

Represents a product with a name and price.

### `DiscountStrategy`

An abstract base class that defines the interface that all discount strategies must implement.

It contains two abstract methods:

* `is_applicable()`
* `apply_discount()`

### `PercentageDiscount`

Applies a percentage-based discount when the strategy is applicable.

### `FixedAmountDiscount`

Subtracts a fixed amount from the product price when the discount conditions are met.

### `PremiumUserDiscount`

Provides a special discount for users with the `Premium` tier.

### `DiscountEngine`

Evaluates the available discount strategies and determines the lowest possible price.

## Features

* Support multiple discount strategies
* Determine whether each strategy is applicable
* Calculate discounted prices
* Support premium-user discounts
* Compare multiple possible prices
* Automatically select the best available price
* Use an abstract interface for different discount strategies

## Example

```python
product = Product('Wireless Mouse', 50.0)
user_tier = 'Premium'

strategies = [
    PercentageDiscount(10),
    FixedAmountDiscount(5),
    PremiumUserDiscount()
]

engine = DiscountEngine(strategies)
best_price = engine.calculate_best_price(product, user_tier)

print(f'Best price for {product.name} for {user_tier} user: ${best_price:.2f}')
```

### Example Output

```text
Best price for Wireless Mouse for Premium user: $40.00
```

The available discounts produce:

* Original price: `$50.00`
* 10% discount: `$45.00`
* Fixed $5 discount: `$45.00`
* Premium discount: `$40.00`

The `DiscountEngine` selects `$40.00` as the best available price.

## Abstraction and Polymorphism

`DiscountStrategy` defines a common interface without specifying how each discount should be calculated.

Each subclass provides its own implementation of the abstract methods:

```python
class DiscountStrategy(ABC):
    @abstractmethod
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        pass

    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        pass
```

This allows `DiscountEngine` to work with different discount strategies without needing to know their individual implementations.

## Status

Completed as a progress exercise while working through the **Object-Oriented Programming** section of the freeCodeCamp Python curriculum.
