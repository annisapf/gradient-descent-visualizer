# -*- coding: utf-8 -*-
from functions import quadratic_function, quadratic_gradient
from optimizer import gradient_descent
from plotting import plot_function_and_path, plot_loss_history


def main():
    x0 = 5.0
    learning_rate = 0.1
    n_iterations = 15

    results = gradient_descent(
        f=quadratic_function,
        grad_f=quadratic_gradient,
        x0=x0,
        learning_rate=learning_rate,
        n_iterations=n_iterations,
    )

    x_history = results["x_history"]
    f_history = results["f_history"]

    print("Gradient Descent Results")
    print("------------------------")
    print(f"Initial x: {x0}")
    print(f"Learning rate: {learning_rate}")
    print(f"Iterations: {n_iterations}")
    print(f"Final x: {x_history[-1]}")
    print(f"Final f(x): {f_history[-1]}")

    print("\nIteration history:")
    for i, (x, fx) in enumerate(zip(x_history, f_history)):
        print(f"Iteration {i:2d}: x = {x:.6f}, f(x) = {fx:.6f}")

    plot_function_and_path(quadratic_function, x_history)
    plot_loss_history(f_history)