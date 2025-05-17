# Control Flow

This tutorial covers basic control flow in `Python`.

# Logical Comparisons

Python provides several operators for comparing values:

- `==`: Equal to
- `!=`: Not equal to
- `>`: Greater than
- `<`: Less than
- `>=`: Greater than or equal to
- `<=`: Less than or equal to
- `is`: Identity (same object)
- `is not`: Negated identity
- `in`: Membership
- `not in`: Negated membership

These can be combined with logical operators:

- `and`: True if both conditions are true
- `or`: True if at least one condition is true
- `not`: Inverts a boolean value

```python
x = 5
y = 10

print(x == 5)        # True
print(x != y)        # True
print(x > 3)         # True
print(x >= y)        # False
print(x is y)        # False

names = ["Alice", "Bob", "Charlie"]
print("Alice" in names)      # True
print("Dave" not in names)   # True

print(x < 10 and y > 5)      # True
print(x > 10 or y > 5)       # True
print(not x == y)            # True
```

These comparisons can then be used to build logical statements. In the next few sections we will cover how to use these comparisons to build statements.

## `if` Statements

The `if` statement executes a block of code if a specified condition is true.

```python
age = 18

if age >= 18:
    print("You are an adult.")
    print("You can vote.")
```

The indented block under the `if` statement only executes when the condition is `True`.

## `elif` Statements

The `elif` (else if) statement allows you to check multiple conditions in sequence.

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

Python evaluates each condition in order and executes the block for the first condition that is `True`. Once a condition is met, the remaining conditions are skipped.

## `else` Statements

The `else` statement provides a block of code to execute when the `if` and all `elif` conditions are `False`.

```python
temperature = 15

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's a nice day.")
else:
    print("It's a bit cold.")
```

The `else` block executes only if all previous conditions are `False`.

# Loops

## `while` Loops

A `while` loop executes a block of code as long as a condition is `True`.

```python
count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1

# Output:
# Count: 1
# Count: 2
# Count: 3
# Count: 4
# Count: 5
```

Be careful to ensure that the condition will eventually become `False`, or you'll create an infinite loop.

```python
# Example of a controlled while loop with a sentinel value
user_input = ""
while user_input.lower() != "quit":
    user_input = input("Enter a command (type 'quit' to exit): ")
    print(f"You entered: {user_input}")
```

## `for` Loops

A `for` loop iterates over a sequence (like a list, tuple, dictionary, set, or string).

```python
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}s")

# Iterating over a string
for char in "Python":
    print(char)

# Iterating over a range
for i in range(5):  # 0 to 4
    print(i)

# Using range with start, stop, and step parameters
for i in range(2, 10, 2):  # 2, 4, 6, 8
    print(i)
```

The `range()` function generates a sequence of numbers:

- `range(stop)`: Numbers from 0 to stop-1
- `range(start, stop)`: Numbers from start to stop-1
- `range(start, stop, step)`: Numbers from start to stop-1, incrementing by step

### `break` Statements

The `break` statement exits a loop immediately, skipping any remaining iterations.

```python
# Find the first even number in a list
numbers = [1, 3, 5, 8, 9, 11]
for num in numbers:
    if num % 2 == 0:
        print(f"Found even number: {num}")
        break

# Exit a while loop when a condition is met
count = 1
while True:
    print(count)
    if count >= 5:
        break
    count += 1
```

### `continue` Statements

The `continue` statement skips the current iteration and moves to the next one.

```python
# Print only odd numbers
for num in range(1, 10):
    if num % 2 == 0:
        continue
    print(f"Odd number: {num}")

# Skip processing for empty strings
words = ["Hello", "", "World", "", "Python"]
for word in words:
    if word == "":
        continue
    print(f"Processing word: {word}")
```

### `else` Clauses in `for` Loops

A loop's `else` clause executes after the loop completes normally (without a `break`).

```python
# Check if all numbers are positive
numbers = [1, 3, 5, 7, 9]
for num in numbers:
    if num <= 0:
        print("Found a non-positive number")
        break
else:
    print("All numbers are positive")

# Search for a value
search_value = 42
data = [10, 25, 30, 15]
for item in data:
    if item == search_value:
        print(f"Found {search_value}!")
        break
else:
    print(f"{search_value} not found in the data")
```

The `else` clause is useful for implementing search algorithms and ensuring certain conditions are met for all items.

# More Features

## `pass` Statements

The `pass` statement is a no-operation placeholder. It's useful when you need a statement syntactically but don't want to execute any code.

```python
# Creating an empty function
def function_to_implement_later():
    pass

# Empty class
class EmptyClass:
    pass

# Placeholder in conditional statements
age = 20
if age < 18:
    pass  # Will implement age restriction later
else:
    print("Access granted")
```

`pass` is often used during development as a placeholder for code that will be implemented later.

## `match` Statements

The `match` statement (also known as pattern matching, which is available in Python 3.10+) provides a more powerful alternative to `if-elif-else` chains.

```python
def process_command(command):
    match command:
        case "start":
            return "Starting the system"
        case "stop":
            return "Stopping the system"
        case "restart":
            return "Restarting the system"
        case "status":
            return "System status: running"
        case _:  # Default case (like else)
            return f"Unknown command: {command}"

print(process_command("start"))    # Output: Starting the system
print(process_command("unknown"))  # Output: Unknown command: unknown
```

Pattern matching with destructuring:

```python
def process_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"Y-axis at y={y}"
        case (x, 0):
            return f"X-axis at x={x}"
        case (x, y) if x == y:
            return f"Diagonal at x=y={x}"
        case (x, y):
            return f"Point at x={x}, y={y}"

print(process_point((0, 0)))    # Output: Origin
print(process_point((0, 5)))    # Output: Y-axis at y=5
print(process_point((3, 3)))    # Output: Diagonal at x=y=3
print(process_point((2, 4)))    # Output: Point at x=2, y=4
```

Pattern matching with class instances:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

def describe_shape(shape):
    match shape:
        case Point(x=0, y=0):
            return "Point at origin"
        case Point(x=x, y=y):
            return f"Point at x={x}, y={y}"
        case Circle(center=Point(x=0, y=0), radius=r):
            return f"Circle at origin with radius {r}"
        case Circle(center=c, radius=r):
            return f"Circle at ({c.x}, {c.y}) with radius {r}"
        case _:
            return "Unknown shape"

print(describe_shape(Point(0, 0)))              # Output: Point at origin
print(describe_shape(Point(3, 4)))              # Output: Point at x=3, y=4
print(describe_shape(Circle(Point(0, 0), 5)))   # Output: Circle at origin with radius 5
```

The `match` statement is particularly useful for:

- Handling different message types in communication protocols
- Processing different data structures
- Implementing state machines
- Parsing and processing structured data
