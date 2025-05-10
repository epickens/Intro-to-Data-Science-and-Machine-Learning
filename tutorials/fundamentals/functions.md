# Python Functions

## Basics

```python
def func_name(arg1, arg2):
    """Docstring should have a short description.

    Additional explainations can be added in the body.

    Args:
        arg1(: type - if available) - description
        arg2(: type - if available) - description

    Returns:
        result(: type - if available) - description

    Example usage:

    func_name(1, 2)
    """
    result = arg1 + arg2

    return result
```

Basic functions take in arguments, have a docstring, a body, and then a return statement.

Using functions allows us to write code that is **organized and reuseable**.

## Function Parameters

### Default Parameters

```python
def greet(name, greeting="Hello"):
    """Greet someone with a customizable greeting."""
    return f"{greeting}, {name}!"

# Using default parameter
print(greet("Alice"))  # Output: Hello, Alice!

# Overriding default parameter
print(greet("Bob", "Hi"))  # Output: Hi, Bob!
```

Python allows us to specify "default parameters." These are values that will automatically be fed into the function if no value is provided. In the example above, `greeting` is giving the default value of "Hello."

### Positional vs. Keyword Arguments

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    return f"I have a {animal_type} named {pet_name}."

# Positional arguments (order matters)
print(describe_pet("dog", "Rex"))

# Keyword arguments (order doesn't matter)
print(describe_pet(pet_name="Whiskers", animal_type="cat"))
```

Python can take in both positional and keyword arguments. With positional arguments, order matters, but with keyword arguments it does not. This is because with keyword arguments Python does not need to infer which value is which.

### Variable Argument Counts (\*args and \*\*kwargs)

```python
# *args for variable positional arguments
def sum_all(*numbers):
    """Sum any number of values."""
    return sum(numbers)

print(sum_all(1, 2, 3, 4))  # Output: 10

# **kwargs for variable keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary with user information."""
    profile = {'first_name': first, 'last_name': last}
    profile.update(user_info)
    return profile

user = build_profile('Albert', 'Einstein',
                    field='physics',
                    location='Princeton')
print(user)
```

We can use `*args` and `**kwargs` to accept an unknown number of positional and keyword arguments respectively.

## Returns

```python
def get_formatted_name(first, last):
    """Return a formatted full name."""
    return f"{first.title()} {last.title()}"

def get_dimensions(length, width, height):
    """Return multiple values as a tuple."""
    area = length * width
    volume = length * width * height
    return area, volume

# Multiple return values
area, volume = get_dimensions(2, 3, 4)
print(f"Area: {area}, Volume: {volume}")
```

Python functions can return:

- Single values: `return x`
- Multiple values: `return x, y, z`
- Nothing: `return` will return `None` or we can omit the return statement all together to implicitly return `None`

## Scope and Lifetime

### Local Scope

```python
def demonstrate_scope():
    local_var = "I'm local"
    print(local_var)  # Works fine

demonstrate_scope()
# print(local_var)  # Would cause an error - local_var doesn't exist here
```

**Local scope** variables are defined, and only exist during function execution.

### Global Scope

```python
global_var = "I'm global"

def access_global():
    print(global_var)  # Can access global variables

def modify_global():
    global global_var  # Must declare global to modify
    global_var = "Modified global"
```

If we define a variable outside a function then it has **global scope**.

## Lambda Functions

```python
# Regular function
def square(x):
    return x**2

# Equivalent lambda function
square_lambda = lambda x: x**2

# Commonly used with functions like map, filter, and sort
numbers = [1, 5, 3, 9, 2]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 25, 9, 81, 4]
```

In python we can define anonymous **lambda** functions with the `lambda` keyword. These can be very useful when processing data.

## Functions as First-Class Objects

```python
def apply_operation(x, y, operation):
    """Apply a function to two numbers."""
    return operation(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print(apply_operation(5, 3, add))      # Output: 8
print(apply_operation(5, 3, multiply)) # Output: 15
```

In Python, functions are first-class objects, meaning that

- They can be assigned to variables
- Passed as arguments into other functions
- Returned from other functions

## Functional Python

### Higher-Order Functions and Callables

```python
from typing import Callable

def apply_twice(func: Callable[[int], int], value: int) -> int:
    """Apply a function twice to a value.

    Args:
        func: A function that takes an int and returns an int
        value: The initial value

    Returns:
        The result of applying the function twice
    """
    return func(func(value))

def add_five(x: int) -> int:
    return x + 5

result = apply_twice(add_five, 3)  # 3 -> 8 -> 13
print(result)  # Output: 13
```

**Higher-order functions** either take functions as arguments, return functions as results, or both. Python defines a special type for these: `Callable`.

### Function Factories

```python
def create_multiplier(factor: int) -> Callable[[int], int]:
    """Create a function that multiplies by a specific factor.

    Args:
        factor: The multiplication factor

    Returns:
        A function that multiplies its input by the factor
    """
    def multiplier(x: int) -> int:
        return x * factor

    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
```

We can build a "function factory" that creates other functions.

### Function Composition

```python
def compose(f: Callable, g: Callable) -> Callable:
    """Compose two functions: f(g(x)).

    Args:
        f: Outer function
        g: Inner function

    Returns:
        A function that applies g then f
    """
    return lambda x: f(g(x))

def add_ten(x: int) -> int:
    return x + 10

def square(x: int) -> int:
    return x * x

# Creates a function that first adds 10, then squares the result
square_after_adding_ten = compose(square, add_ten)

print(square_after_adding_ten(5))  # (5 + 10)² = 15² = 225
```

We can combine multiple functions into a new function.

### Built-in Function Tools

#### `map`: Apply a function to each item in an iterable

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# With a named function
def cube(x):
    return x**3

cubed = list(map(cube, numbers))
print(cubed)  # Output: [1, 8, 27, 64, 125]
```

#### `filter`: Filter items based on a predicate function

```python
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
```

#### `reduce`: Cumulatively apply a function to items

```python
from functools import reduce

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4]
product = reduce(multiply, numbers)  # 1*2*3*4 = 24
print(product)  # Output: 24
```

### Partial Functions

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

# Create a function that squares any number
square = partial(power, exponent=2)

# Create a function that cubes any number
cube = partial(power, exponent=3)

# Create a function that calculates powers of 2
powers_of_two = partial(power, base=2)

print(square(5))       # Output: 25
print(cube(3))         # Output: 27
print(powers_of_two(8))  # Output: 256
```

The `functools.partial` function allows you to create a new function with some arguments fixed.

### Decorators

```python
def timing_decorator(func):
    """A decorator that reports the execution time."""
    import time

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to run")
        return result

    return wrapper

@timing_decorator
def slow_function(delay):
    """A function that simulates a time-consuming task."""
    import time
    time.sleep(delay)
    return f"Finished after {delay} seconds"

print(slow_function(1.5))
```

Decorators are a powerful way to modify or enhance functions. In the example above, we define a timing decorator that we can easily use to time **any** function!

### List Comprehensions as Functional Tools

```python
# Map-like operation
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]

# Filter-like operation
even_numbers = [x for x in numbers if x % 2 == 0]

# Combined map and filter
even_squared = [x**2 for x in numbers if x % 2 == 0]

print(squared)      # Output: [1, 4, 9, 16, 25]
print(even_numbers) # Output: [2, 4]
print(even_squared) # Output: [4, 16]
```

List comprehensions provide a concise way to apply functional operations.

### Immutability and Pure Functions

```python
# Pure function
def add(a, b):
    return a + b

# Impure function (modifies external state)
total = 0
def add_to_total(value):
    global total
    total += value
    return total
```

Pure functions have no side effects and always return the same output for the same input. Impure functions effect the state of things outside the function.

```python
# Using tuples (immutable) instead of lists (mutable)
def add_item(collection, item):
    """Return a new collection with the item added."""
    return collection + (item,)

items = (1, 2, 3)
new_items = add_item(items, 4)  # Creates a new tuple
print(items)      # Output: (1, 2, 3) - original unchanged
print(new_items)  # Output: (1, 2, 3, 4)
```

Working with immutable data structures helps maintain function purity. When working with mutable data structures it's possible to change global variables by accident!
