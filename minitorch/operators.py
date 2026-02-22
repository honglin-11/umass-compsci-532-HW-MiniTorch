"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable, Any

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
def mul(x: float, y: float) -> float:
    """$f(x, y) = x * y$"""
    return x * y

# TODO fill in the remaining mathematical operators. Use mul provided above as an example.
# used this page as reference: https://minitorch.github.io/module0/module0/#task-01-operators
# - id
def id(x: float) -> float:
    """$f(x) = x$"""
    return x

# - add
def add(x: float, y: float) -> float:
    """$f(x, y) = x + y$"""
    return x + y

# - neg
def neg(x: float) -> float:
    """$f(x) = -1 * x$"""
    return -1 * x

# - lt
def lt(x: float, y: float) -> bool:
    """$f(x, y) = x < y$"""
    return x < y

# - eq
def eq(x: float, y: float) -> bool:
    """$f(x, y) = x == y$"""
    return x == y

# - max
def max(x: float, y: float) -> float:
    """$f(x, y) = x if x > y else y$"""
    return y if lt(x, y) else x

# - is_close
def is_close(x: float, y: float) -> bool:
    """$f(x, y) = |x - y| < 1e-2$"""
    return abs(x - y) < math.e - 2
    
# - sigmoid
def sigmoid(x: float) -> float:
    """$f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$"""
    return 1 / (1 + math.exp(-1 * x)) if x >= 0 else math.exp(x) / (1 + math.exp(x))

# - relu
def relu(x: float) -> float:
    """$f(x) = x if x > 0 else 0.0$"""
    return x if x > 0 else 0.0

# - log
def log(x: float) -> float:
    """$f(x) = ln(x)$"""
    return math.log(x)

# - exp
def exp(x: float) -> float:
    """$f(x) = math.exp(x)$"""
    return math.exp(x)

# - log_back
def log_back(x: float, y: float) -> float:
    """$f(x) = y / x"""
    return y / x

# - inv
def inv(x: float) -> float:
    """$f(x) = 1 / x"""
    return 1 / x

# - inv_back
def inv_back(x: float, y: float) -> float:
    """$f(x, y) = (-1 * y / x ^ 2)"""
    return -1 * y / x ** 2

# - relu_back
def relu_back(x: float, y: float) -> float:
    """$f(x, y) = y if x > 0 else 0.0"""
    return y if x > 0 else 0.0

# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# reference: https://minitorch.github.io/module0/module0/#task-03-functional-python
# - map
def map(func: Callable, iter: Iterable) -> Iterable:
    """Higher-order function that applies a given function to each element of an iterable"""
    for i in iter:
        yield func(i)

# - zipWith
def zipWith(func: Callable, iter1: Iterable, iter2: Iterable) -> Iterable:
    """Higher-order function that combines elements from two iterables using a given function"""
    for i1, i2 in zip(iter1, iter2):
        yield(func(i1, i2))

# - reduce
def reduce(func: Callable, iter: Iterable, start: object = None) -> Any:
    """Higher-order function that reduces an iterable to a single value using a given function"""
    result = start
    for i in iter:
        result = func(result, i)
    return result
#
# Use these to implement
# - negList : negate all elemnts in a list using map
def negList(lst: list[float]) -> Iterable[float]:
    """Negate all elements in a list using map"""
    return map(neg, lst)

# - addLists : add corresponding elements from two lists using zipWith
def addLists(lst1: list[float], lst2: list[float]) -> Iterable[float]:
    """Add corresponding elements from two lists using zipWith"""
    return zipWith(add, lst1, lst2)

# - sum: sum all elements in a list using reduce
def sum(lst: list[float]) -> float:
    """Sum all elements in a list using reduce"""
    return reduce(add, lst, start=0.0)

# - prod: tcalculate the product of all elements in a list using reduce
def prod(lst: list[float]) -> float:
    """Calculate the product of all elements in a list using reduce"""
    return reduce(mul, lst, start=1.0)

# TODO: Implement for Task 0.3.
