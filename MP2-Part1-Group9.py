import tkinter as tk
from tkinter import messagebox
import sympy as sp

class RootFindingCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Root Finding Calculator")
        self.geometry("400x400")

        self.equation_label = tk.Label(self, text="Enter Equation:")
        self.equation_label.pack()

        self.equation_entry = tk.Entry(self)
        self.equation_entry.insert(tk.END, "x**2 - 4")  # Example polynomial equation
        self.equation_entry.pack()

        self.example_label = tk.Label(self, text="Example: Polynomial: x**2 - 4, Trigonometric: sin(x), Fraction: 1/x, Combination: x**2 + cos(x)")
        self.example_label.pack()

        self.initial_guess_label = tk.Label(self, text="Initial Guess (Newton-Raphson):")
        self.initial_guess_label.pack()

        self.initial_guess_entry = tk.Entry(self)
        self.initial_guess_entry.insert(tk.END, "2.0")  # Example initial guess
        self.initial_guess_entry.pack()

        self.interval_label = tk.Label(self, text="Interval (Bisection):")
        self.interval_label.pack()

        self.interval_entry = tk.Entry(self)
        self.interval_entry.insert(tk.END, "0, 2")  # Example interval
        self.interval_entry.pack()

        self.epsilon_label = tk.Label(self, text="Epsilon (Error Tolerance):")
        self.epsilon_label.pack()

        self.epsilon_entry = tk.Entry(self)
        self.epsilon_entry.insert(tk.END, "0.001")  # Example epsilon
        self.epsilon_entry.pack()

        self.newton_button = tk.Button(self, text="Newton-Raphson", command=self.newton_raphson)
        self.newton_button.pack()

        self.bisection_button = tk.Button(self, text="Bisection", command=self.bisection)
        self.bisection_button.pack()

    def newton_raphson(self):
        equation_str = self.equation_entry.get()
        initial_guess = float(self.initial_guess_entry.get())
        epsilon = float(self.epsilon_entry.get())

        x = sp.Symbol('x')
        try:
            equation = sp.sympify(equation_str)
            derivative = sp.diff(equation, x)
            f = sp.lambdify(x, equation)
            f_prime = sp.lambdify(x, derivative)

            root, iterations = self.newton_raphson_method(f, f_prime, initial_guess, epsilon)
            messagebox.showinfo("Newton-Raphson Result", f"Root: {root}\nDerivative: {derivative}\nIterations: {iterations}")
        except (sp.SympifyError, ValueError):
            messagebox.showerror("Error", "Invalid input. Please enter a valid polynomial equation and initial guess.")

    def newton_raphson_method(self, f, f_prime, initial_guess, epsilon, max_iterations=1000):
        x_old = initial_guess
        iterations = 0
        while True:
            iterations += 1
            if iterations > max_iterations:
                messagebox.showwarning("Warning", "Max iterations reached. No convergence.")
                return None, iterations

            x_new = x_old - f(x_old) / f_prime(x_old)
            if abs(x_new - x_old) < epsilon:
                return x_new, iterations
            x_old = x_new

    def bisection(self):
        equation_str = self.equation_entry.get()
        interval_str = self.interval_entry.get()
        epsilon = float(self.epsilon_entry.get())

        x = sp.Symbol('x')
        try:
            equation = sp.sympify(equation_str)
            f = sp.lambdify(x, equation)
            a, b = map(float, interval_str.split(','))
            if f(a) * f(b) > 0:
                messagebox.showerror("Error", "Bisection method cannot be applied. Change interval.")
                return

            root, iterations = self.bisection_method(f, a, b, epsilon)
            messagebox.showinfo("Bisection Result", f"Root: {root}\nIterations: {iterations}\nValue at Root: {f(root)}")
        except (sp.SympifyError, ValueError):
            messagebox.showerror("Error", "Invalid input. Please enter a valid equation, interval, and epsilon.")

    def bisection_method(self, f, a, b, epsilon, max_iterations=1000):
        iterations = 0
        while True:
            iterations += 1
            if iterations > max_iterations:
                messagebox.showwarning("Warning", "Max iterations reached. No convergence.")
                return None, iterations

            c = (a + b) / 2
            if abs(f(c)) < epsilon:
                return c, iterations

            if f(a) * f(c) < 0:
                b = c
            else:
                a = c

if __name__ == "__main__":
    app = RootFindingCalculator()
    app.mainloop()