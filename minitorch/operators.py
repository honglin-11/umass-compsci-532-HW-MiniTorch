"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

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
    return 1 / (1 - math.e ** neg(x)) if x >= 0 else (math.e ** x) / (1 + math.e ** x)

# - relu
def relu(x: float) -> float:
    """$f(x) = max(x, 0)$"""
    return max(x, 0)

# - log
def log(x: float) -> float:
    """$f(x) = ln(x)$"""
    return math.log(x)

# - exp
def exp(x: float) -> float:
    """$f(x) = math.exp(x)$"""
    return math.exp(x)

# - log_back
def log_back():
    pass

# - inv
def inv(x: float) -> float:
    """$f(x) = 1 / x"""
    return 1 / x

# - inv_back
def inv_back():
    pass

# - relu_back
def relu_back():
    pass

#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate all elemnts in a list using map
# - addLists : add corresponding elements from two lists using zipWith
# - sum: sum all elements in a list using reduce
# - prod: tcalculate the product of all elements in a list using reduce


# TODO: Implement for Task 0.3.
