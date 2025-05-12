#
# Credit: Sasha Rush - MiniTorch
#
"""
Collection of the core mathematical operators used throughout the code base.
"""

import math
from types import NotImplementedType
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.
#


def mul(x: float, y: float) -> float:
    """
    $f(x, y) = x * y$

    Args:
        x: float
        y: float

    Returns:
        float: $x * y$
    """
    raise NotImplementedError("mul not implemented")


def id(x: float) -> float:
    """
    $f(x) = x$

    Args:
        x: float

    Returns:
        float: x
    """
    raise NotImplementedError("id not implemented")


def add(x: float, y: float) -> float:
    """
    $f(x, y) = x + y$

    Args:
        x: float
        y: float

    Returns:
        float: $x + y$
    """
    raise NotImplementedError("add not implemented")


def neg(x: float) -> float:
    """
    $f(x) = -x$

    Args:
        x: float

    Returns:
        float: $-x$
    """
    raise NotImplementedError("neg not implemented")


def lt(x: float, y: float) -> float:
    """
    $f(x) =$ 1.0 if x is less than y else 0.0

    Args:
        x: float
        y: float

    Returns:
        float: 1.0 if x is less than y else 0.0
    """
    raise NotImplementedError("lt not implemented")


def eq(x: float, y: float) -> float:
    """
    $f(x) =$ 1.0 if x is equal to y else 0.0

    Args:
        x: float
        y: float

    Returns:
        float: 1.0 if x is equal to y else 0.0
    """
    raise NotImplementedError("eq not implemented")


def max(x: float, y: float) -> float:
    """
    $f(x) =$ x if x is greater than y else y

    Args:
        x: float
        y: float

    Returns:
        float: x if x is greater than y else y
    """
    raise NotImplementedError("max not implemented")


def is_close(x: float, y: float) -> float:
    """
    $f(x) = |x - y| < 1e-2$

    Args:
        x: float
        y: float

    Returns:
        float: 1.0 if |x - y| < 1e-2 else 0.0
    """
    raise NotImplementedError("is_close not implemented")


def sigmoid(x: float) -> float:
    r"""
    $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$

    (See https://en.wikipedia.org/wiki/Sigmoid_function )

    Calculate as

    $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$

    for stability.

    Args:
        x: float

    Returns:
        float: $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$
    """
    raise NotImplementedError("sigmoid not implemented")


def relu(x: float) -> float:
    """
    $f(x) =$ x if x is greater than 0, else 0

    (See https://en.wikipedia.org/wiki/Rectifier_(neural_networks) .)


    Args:
        x: float

    Returns:
        float: x if x is greater than 0, else 0
    """
    raise NotImplementedError("relu not implemented")


EPS = 1e-6


def log(x: float) -> float:
    """
    $f(x) = log(x)$

    Args:
        x: float

    Returns:
        float: $log(x)$
    """
    raise NotImplementedError("log not implemented")


def exp(x: float) -> float:
    """
    $f(x) = e^{x}$

    Args:
        x: float

    Returns:
        float: $e^{x}$
    """
    raise NotImplementedError("exp not implemented")


def log_back(x: float, d: float) -> float:
    """
    If $f = log$ as above, compute $d \times f'(x)$

    Args:
        x: float
        d: float

    Returns:
        float: $d \times f'(x)$
    """
    raise NotImplementedError("log_back not implemented")


def inv(x: float) -> float:
    """
    $f(x) = 1/x$

    Args:
        x: float

    Returns:
        float: $1/x$
    """
    raise NotImplementedError("inv not implemented")


def inv_back(x: float, d: float) -> float:
    """
    If $f(x) = 1/x$ compute $d \times f'(x)$

    Args:
        x: float
        d: float

    Returns:
        float: $d \times f'(x) = - 1 / x^2$
    """
    raise NotImplementedError("inv_back not implemented")


def relu_back(x: float, d: float) -> float:
    """
    If $f = relu$ compute $d \times f'(x)$

    Args:
        x: float
        d: float

    Returns:
        float: $d \times f'(x)$
    """
    raise NotImplementedError("relu_back not implemented")


def map(fn: Callable[[float], float]) -> Callable[[Iterable[float]], Iterable[float]]:
    """
    Higher-order map.

    See https://en.wikipedia.org/wiki/Map_(higher-order_function)

    Args:
        fn: Function from one value to one value.

    Returns:
        A function that takes a list, applies `fn` to each element, and returns a
         new list
    """

    raise NotImplementedError("map not implemented")


def negList(ls: Iterable[float]) -> Iterable[float]:
    """
    Negates each element in the list `ls` using `map` and `neg`.

    Args:
        ls: Iterable[float]

    Returns:
        Iterable[float]: Negated list
    """
    raise NotImplementedError("negList not implemented")


def zipWith(
    fn: Callable[[float, float], float]
) -> Callable[[Iterable[float], Iterable[float]], Iterable[float]]:
    """
    Higher-order zipwith (or map2).

    See https://en.wikipedia.org/wiki/Map_(higher-order_function)

    Args:
        fn: combine two values

    Returns:
        Function that takes two equally sized lists `ls1` and `ls2`, produce a new list by
         applying fn(x, y) on each pair of elements.
    """

    raise NotImplementedError("zipWith not implemented")


def addLists(ls1: Iterable[float], ls2: Iterable[float]) -> Iterable[float]:
    """
    Add the elements of `ls1` and `ls2` using `zipWith` and `add`.

    Args:
        ls1: Iterable[float]
        ls2: Iterable[float]

    Returns:
        Iterable[float]: List of added elements
    """
    raise NotImplementedError("addLists not implemented")


def reduce(
    fn: Callable[[float, float], float], start: float
) -> Callable[[Iterable[float]], float]:
    r"""
    Higher-order reduce.

    Args:
        fn: combine two values
        start: start value $x_0$

    Returns:
        Function that takes a list `ls` of elements
         $x_1 \ldots x_n$ and computes the reduction :math:`fn(x_3, fn(x_2,
         fn(x_1, x_0)))`
    """

    raise NotImplementedError("reduce not implemented")


def sum(ls: Iterable[float]) -> float:
    """
    Sum up a list using `reduce` and `add`.

    Args:
        ls: Iterable[float]

    Returns:
        float: Sum of the list
    """
    raise NotImplementedError("sum not implemented")


def prod(ls: Iterable[float]) -> float:
    """
    Product of a list using `reduce` and `mul`.

    Args:
        ls: Iterable[float]

    Returns:
        float: Product of the list
    """
    raise NotImplementedError("prod not implemented")
