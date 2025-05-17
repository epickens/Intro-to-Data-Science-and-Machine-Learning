# Python Classes

Among the many programming paradigms support by `Python`, one of the most important is "object oriented programming" (OOP). OOP centers around the idea of using "classes" to define and create objects that can be used throughout your programs. It provides a clean way to handle complex problems, and while it isn't the only way to program in `Python`, it is popular with many developers.

In this tutorial we will cover some important aspects of classes in `Python` and how to use them.

# The Basics

## Basic Class Structure

A class in Python is defined using the `class` keyword, followed by the class name and a colon. By convention, class names use CamelCase (starting with a capital letter).

```python
class Person:
    """A simple class representing a person."""

    # Class body goes here
    pass
```

Classes act as blueprints for creating objects (instances). Each instance can have attributes (data) and methods (functions that operate on the data).

````python
# Creating an instance of the Person class
person1 = Person()
person2 = Person()

# These are two different objects
print(person1 is person2)  # Output: False

## Constructors

The constructor is a special method called ```__init__``` that is automatically executed when a new instance of a class is created. It's used to initialize the object's attributes.

```python
class Person:
    """A class representing a person with a name and age."""

    def __init__(self, name, age):
        """Initialize a new Person object.

        Args:
            name (str): The person's name
            age (int): The person's age
        """
        self.name = name
        self.age = age

# Creating instances with initial values
alice = Person("Alice", 30)
bob = Person("Bob", 25)

print(alice.name, alice.age)  # Output: Alice 30
print(bob.name, bob.age)      # Output: Bob 25
````

The constructor allows you to set up each new instance with its own unique state.

## The `self` Parameter and Instance Methods

The `self` parameter refers to the instance of the class and is used to access variables and methods that belong to the instance. It's always the first parameter in instance methods.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        """Return a greeting message."""
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def have_birthday(self):
        """Increment the person's age by 1."""
        self.age += 1
        return f"{self.name} is now {self.age} years old."

# Using instance methods
alice = Person("Alice", 30)
print(alice.greet())         # Output: Hello, my name is Alice and I am 30 years old.
print(alice.have_birthday()) # Output: Alice is now 31 years old.
```

Instance methods can access and modify the instance's attributes using `self`. When you call an instance method, Python automatically passes the instance as the first argument.

## Class Attributes and Methods

Class attributes belong to the class itself rather than to instances. They're shared among all instances of the class.

```python
class Person:
    # Class attribute
    species = "Homo sapiens"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def describe(self):
        return f"{self.name} is {self.age} years old."

    # Class method
    @classmethod
    def get_species(cls):
        return f"All people are {cls.species}"

    # Static method (doesn't use cls or self)
    @staticmethod
    def is_adult(age):
        return age >= 18

# Accessing class attributes and methods
print(Person.species)           # Output: Homo sapiens
print(Person.get_species())     # Output: All people are Homo sapiens
print(Person.is_adult(20))      # Output: True

# Instances can also access class attributes
alice = Person("Alice", 30)
print(alice.species)            # Output: Homo sapiens
print(alice.get_species())      # Output: All people are Homo sapiens
```

Class methods use the `@classmethod` decorator and take a `cls` parameter (reference to the class). Static methods use the `@staticmethod` decorator and don't automatically receive any special first parameter.

## Inheritance

Inheritance allows a class to inherit attributes and methods from another class. The new class (subclass) can override or extend the functionality of the parent class (superclass).

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating instances of subclasses
dog = Dog("Rex")
cat = Cat("Whiskers")

print(dog.name)    # Output: Rex (inherited from Animal)
print(dog.speak()) # Output: Woof! (overridden in Dog)
print(cat.speak()) # Output: Meow! (overridden in Cat)
```

You can extend parent class methods using `super()`:

````python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name}."

class Student(Person):
    def __init__(self, name, age, student_id):
        # Call the parent class's __init__ method
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        # Extend the parent's introduce method
        basic_intro = super().introduce()
        return f"{basic_intro} I'm a student with ID {self.student_id}."

student = Student("Alice", 20, "A12345")
print(student.introduce())  # Output: Hi, I'm Alice. I'm a student with ID A12345.

### Composition vs Inheritance

While inheritance represents an "is-a" relationship, composition represents a "has-a" relationship. Composition often provides more flexibility and is generally preferred when possible.

```python
# Inheritance approach (is-a relationship)
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        return f"Moving at {self.speed} mph"

class Car(Vehicle):
    def honk(self):
        return "Beep beep!"

# Composition approach (has-a relationship)
class Engine:
    def start(self):
        return "Engine started"

    def stop(self):
        return "Engine stopped"

class Car:
    def __init__(self, speed):
        self.speed = speed
        self.engine = Engine()  # Car has-an Engine

    def start(self):
        return self.engine.start()

    def move(self):
        return f"Moving at {self.speed} mph"
````

Composition is often more flexible because:

- It allows changing behavior at runtime
- It avoids the complexities of deep inheritance hierarchies
- It makes code more modular and easier to test

## Magic Methods

Magic methods (also called dunder methods for "double underscore") allow you to define how your objects behave with built-in Python operations.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # String representation for developers
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    # String representation for users
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Addition: v1 + v2
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Subtraction: v1 - v2
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # Multiplication: v1 * scalar
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # Length: len(v)
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

    # Equality: v1 == v2
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Using the magic methods
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)            # Output: (3, 4)
print(repr(v1))      # Output: Vector(3, 4)
print(v1 + v2)       # Output: (4, 6)
print(v1 - v2)       # Output: (2, 2)
print(v1 * 2)        # Output: (6, 8)
print(len(v1))       # Output: 5
print(v1 == Vector(3, 4))  # Output: True
```

Common magic methods include:

- `__init__`: Constructor
- `__str__` and `__repr__`: String representations
- `__add__`, `__sub__`, `__mul__`: Arithmetic operations
- `__eq__`, `__lt__`, `__gt__`: Comparison operations
- `__len__`, `__getitem__`, `__setitem__`: Container behavior
- `__enter__` and `__exit__`: Context manager protocol

## Data Classes

Data classes simplify the creation of classes that primarily store data. They automatically generate special methods like `__init__`, `__repr__`, and `__eq__`.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0  # Default value

    def distance_from_origin(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

# Creating instances
p1 = Point(1.0, 2.0)
p2 = Point(3.0, 4.0, 5.0)

print(p1)  # Output: Point(x=1.0, y=2.0, z=0.0)
print(p2)  # Output: Point(x=3.0, y=4.0, z=5.0)
print(p1.distance_from_origin())  # Output: 2.23606...
print(p1 == Point(1.0, 2.0))      # Output: True
```

You can customize data classes with additional parameters:

```python
from dataclasses import dataclass, field

@dataclass(frozen=True)  # Makes instances immutable
class Person:
    name: str
    age: int
    email: str = field(default="", repr=False)  # Not shown in repr
    friends: list = field(default_factory=list)  # Default empty list

    def is_adult(self):
        return self.age >= 18

person = Person("Alice", 30)
print(person)  # Output: Person(name='Alice', age=30)
```

### Why Data Classes are Useful in ML and DS

Data classes are particularly useful in machine learning and data science for several reasons:

1. **Clean representation of data structures**:

```python
@dataclass
class DatasetConfig:
    name: str
    batch_size: int = 32
    shuffle: bool = True
    num_workers: int = 4

config = DatasetConfig("MNIST")
```

2. **Immutable configurations**:

```python
@dataclass(frozen=True)
class ModelParameters:
    learning_rate: float
    hidden_size: int
    dropout_rate: float

params = ModelParameters(0.001, 256, 0.2)
```

3. **Type hints for better IDE support and documentation**:

```python
@dataclass
class TrainingMetrics:
    epoch: int
    train_loss: float
    val_loss: float
    accuracy: float

    def is_improved(self, previous: 'TrainingMetrics') -> bool:
        return self.val_loss < previous.val_loss
```

4. **Simplified serialization/deserialization**:

```python
import json
from dataclasses import asdict

@dataclass
class ExperimentConfig:
    model_name: str
    dataset: str
    epochs: int

config = ExperimentConfig("ResNet", "ImageNet", 100)
config_dict = asdict(config)  # Convert to dictionary
config_json = json.dumps(config_dict)  # Convert to JSON
```

# Some Advanced Features

## Access Control and Encapsulation

Python uses naming conventions rather than strict access modifiers for encapsulation:

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner           # Public attribute
        self._balance = balance       # Protected attribute (convention)
        self.__account_number = None  # Private attribute (name mangling)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    @property
    def balance(self):
        """Getter for balance."""
        return self._balance

    @balance.setter
    def balance(self, value):
        """Setter for balance with validation."""
        if value >= 0:
            self._balance = value
        else:
            raise ValueError("Balance cannot be negative")

# Using the class
account = BankAccount("Alice", 1000)
print(account.owner)    # Public: Alice
print(account.balance)  # Using property: 1000

account.deposit(500)
print(account.balance)  # 1500

# This works but is discouraged (accessing protected attribute)
print(account._balance)  # 1500

# This raises an AttributeError (name mangling)
# print(account.__account_number)  # Error

# But you can still access it with the mangled name
# print(account._BankAccount__account_number)  # None
```

The `@property` decorator allows you to define getter, setter, and deleter methods for attributes, providing controlled access while maintaining a clean interface.

## Abstract Classes

Abstract classes define interfaces that derived classes must implement. Python provides the `abc` module for creating abstract base classes:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

    def describe(self):
        """Non-abstract method that can be inherited."""
        return f"A shape with area {self.area()} and perimeter {self.perimeter()}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# This would raise TypeError because Shape is abstract
# shape = Shape()

# These work because they implement the abstract methods
rectangle = Rectangle(5, 4)
circle = Circle(3)

print(rectangle.area())      # Output: 20
print(circle.area())         # Output: 28.27431
print(rectangle.describe())  # Output: A shape with area 20 and perimeter 18
```

Abstract classes cannot be instantiated directly and force subclasses to implement specific methods, ensuring a consistent interface.

## Metaclasses

Metaclasses are "classes of classes" that define how classes themselves behave. The default metaclass for all Python classes is `type`.

```python
# The type metaclass can create classes dynamically
Person = type('Person', (), {'name': 'Unknown', 'greet': lambda self: f"Hello, I'm {self.name}"})

# Equivalent to:
# class Person:
#     name = 'Unknown'
#     def greet(self):
#         return f"Hello, I'm {self.name}"

p = Person()
print(p.greet())  # Output: Hello, I'm Unknown
```

Custom metaclasses can modify class creation:

```python
class LoggingMeta(type):
    def __new__(mcs, name, bases, attrs):
        # Add logging to all methods
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith('__'):
                attrs[attr_name] = LoggingMeta.add_logging(attr_value)

        return super().__new__(mcs, name, bases, attrs)

    @staticmethod
    def add_logging(method):
        def wrapper(*args, **kwargs):
            print(f"Calling {method.__name__}")
            result = method(*args, **kwargs)
            print(f"{method.__name__} returned {result}")
            return result
        return wrapper

class Service(metaclass=LoggingMeta):
    def process(self, data):
        return data.upper()

    def analyze(self, data):
        return len(data)

# Using the class with automatic logging
service = Service()
service.process("hello")
# Output:
# Calling process
# process returned HELLO

service.analyze("world")
# Output:
# Calling analyze
# analyze returned 5
```

Metaclasses are powerful but should be used sparingly, as they can make code harder to understand.

## Class Dectorators

Class decorators modify or enhance classes after they've been defined:

```python
def add_repr(cls):
    """Add a simple __repr__ method to the class."""
    def __repr__(self):
        attrs = ', '.join(f"{key}={value!r}" for key, value in self.__dict__.items())
        return f"{cls.__name__}({attrs})"

    cls.__repr__ = __repr__
    return cls

@add_repr
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# The Person class now has a __repr__ method
person = Person("Alice", 30)
print(person)  # Output: Person(name='Alice', age=30)
```

Another example that adds methods to a class:

```python
def add_methods(*methods):
    """Add multiple methods to a class."""
    def decorator(cls):
        for method in methods:
            setattr(cls, method.__name__, method)
        return cls
    return decorator

def say_hello(self):
    return f"Hello, I'm {self.name}"

def say_goodbye(self):
    return f"Goodbye from {self.name}"

@add_methods(say_hello, say_goodbye)
class Person:
    def __init__(self, name):
        self.name = name

# The Person class now has the added methods
person = Person("Bob")
print(person.say_hello())    # Output: Hello, I'm Bob
print(person.say_goodbye())  # Output: Goodbye from Bob
```

Class decorators provide a clean way to apply cross-cutting concerns to multiple classes.

## Descriptors

Descriptors control attribute access and are the mechanism behind properties, class methods, and static methods:

```python
class Validator:
    """A descriptor that validates attribute values."""

    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
        self.name = None

    def __set_name__(self, owner, name):
        """Store the attribute name."""
        self.name = name

    def __get__(self, instance, owner):
        """Return the attribute value."""
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        """Validate and set the attribute value."""
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be at least {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be no more than {self.max_value}")

        instance.__dict__[self.name] = value

class Person:
    age = Validator(min_value=0, max_value=120)
    height = Validator(min_value=0, max_value=300)

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

# Using the class with validated attributes
person = Person("Alice", 30, 165)

try:
    person.age = -5  # This will raise a ValueError
except ValueError as e:
    print(e)  # Output: age must be at least 0

try:
    person.height = 350  # This will raise a ValueError
except ValueError as e:
    print(e)  # Output: height must be no more than 300
```

Descriptors are powerful for implementing attribute validation, lazy properties, and other attribute-related behaviors.

## Method Resolution Order (MRO)

The Method Resolution Order (MRO) determines the order in which Python searches for methods in a class hierarchy, especially with multiple inheritance:

```python
class A:
    def method(self):
        return "A.method"

class B(A):
    def method(self):
        return "B.method"

class C(A):
    def method(self):
        return "C.method"

class D(B, C):
    pass

# View the MRO
print(D.__mro__)
# Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# Method resolution follows the MRO
d = D()
print(d.method())  # Output: B.method
```

Python uses the C3 linearization algorithm to determine the MRO, which ensures:

1. A subclass comes before its base classes
2. Base class order is preserved
3. No class appears twice in the MRO

Understanding MRO is crucial when working with complex inheritance hierarchies, especially with `super()` calls:

```python
class A:
    def method(self):
        print("A.method called")

class B(A):
    def method(self):
        print("B.method called")
        super().method()

class C(A):
    def method(self):
        print("C.method called")
        super().method()

class D(B, C):
    def method(self):
        print("D.method called")
        super().method()

d = D()
d.method()
# Output:
# D.method called
# B.method called
# C.method called
# A.method called
```

The `super()` function follows the MRO, not just the immediate parent class, which is why `C.method` is called after `B.method` in this example.
