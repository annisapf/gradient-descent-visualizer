# -*- coding: utf-8 -*-

def quadratic_function(x : float) -> float :
    """
    Compute a quadratic function: y = ax^2 + bx + c
    Example coefficients: a=1, b=2, c=3
    """
    a = 1.0
    b = 2.0
    c = 3.0
    return a * (x**2) + b * x + c 

def quadratic_gradient(x: float) -> float :
    """
    Compute a gradient of quadratic function: y = 2ax + b
    """
    a = 1.0
    b = 2.0 
    return 2 * a * x + b
