# -*- coding: utf-8 -*-

def gradient_descent(f, grad_f, x0, learning_rate, n_iterations):
    """
    Perform 1D gradient descent.

    Returns a dictionary containing:
    - x_history: points visited
    - f_history: function values
    """
    x = x0
    x_history = [x]
    f_history = [f(x)]

    for _ in range(n_iterations):
        gradient = grad_f(x)
        x = x - learning_rate * gradient
        x_history.append(x)
        f_history.append(f(x))

    return {
        "x_history": x_history,
        "f_history": f_history,
    }