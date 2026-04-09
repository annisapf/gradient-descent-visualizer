# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def plot_function_and_path(f, x_history, x_min=-6, x_max=6):
    """
    Plot the function curve and the points visited by gradient descent.
    """
    x_values = np.linspace(x_min, x_max, 400)
    y_values = [f(x) for x in x_values]

    plt.figure(figsize=(8, 5))
    plt.plot(x_values, y_values, label="f(x)")
    plt.scatter(x_history, [f(x) for x in x_history], label="Gradient descent steps")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Gradient Descent Path on Function")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_loss_history(f_history):
    """
    Plot function value versus iteration.
    """
    iterations = range(len(f_history))

    plt.figure(figsize=(8, 5))
    plt.plot(iterations, f_history, marker="o")
    plt.xlabel("Iteration")
    plt.ylabel("f(x)")
    plt.title("Loss vs Iteration")
    plt.grid(True)
    plt.show()