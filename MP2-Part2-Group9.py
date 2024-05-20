import tkinter as tk
from sympy import sympify, Symbol, diff
from sympy.utilities.lambdify import lambdify
from tkinter import messagebox

def open_bisection_calculator():
    def bisection(f, a, b, tol, max_iter):
        try:
            f = lambdify(Symbol('x'), f)
        except Exception as e:
            return "Invalid equation: " + str(e), None, None, None

        if f(a) * f(b) >= 0:
            return "Bisection method cannot be applied to this interval.", None, None, None

        iterations = 0
        while (b - a) / 2 > tol and iterations < max_iter:
            c = (a + b) / 2
            if f(c) == 0:
                return "Exact root found.", iterations, c, f(c)
            elif f(a) * f(c) < 0:
                b = c
            else:
                a = c
            iterations += 1

        return "Root approximated within tolerance.", iterations, (a + b) / 2, f((a + b) / 2)

    def calculate():
        equation = entry_equation.get()
        # Replace "^" with "**" for exponents
        equation = equation.replace("^", "**")
        interval_a = float(entry_interval_a.get())
        interval_b = float(entry_interval_b.get())
        error = float(entry_error.get())

        result_label.config(text="")
        iteration_label.config(text="")
        root_label.config(text="")
        function_value_label.config(text="")

        result, iterations, root, function_value = bisection(equation, interval_a, interval_b, error, 1000)

        result_label.config(text=result)
        if iterations is not None:
            iteration_label.config(text="Iterations: " + str(iterations))
        if root is not None:
            root_label.config(text="Root: " + str(root))
        if function_value is not None:
            function_value_label.config(text="Function Value at Root: " + str(function_value))

    def insert_example_equation(example_equation):
        entry_equation.delete(0, tk.END)
        entry_equation.insert(0, example_equation)

    # Create GUI
    root = tk.Toplevel()
    root.title("Bisection Method Calculator")
    root.configure(bg="#F0F0F0")

    frame = tk.Frame(root, padx=10, pady=10, bg="#F0F0F0")
    frame.pack()

    label_equation = tk.Label(frame, text="Enter Equation:", bg="#F0F0F0")
    label_equation.grid(row=0, column=0, sticky="w")

    entry_equation = tk.Entry(frame, width=30)
    entry_equation.grid(row=0, column=1)

    label_interval_a = tk.Label(frame, text="Interval [a]:", bg="#F0F0F0")
    label_interval_a.grid(row=1, column=0, sticky="w")

    entry_interval_a = tk.Entry(frame, width=10)
    entry_interval_a.grid(row=1, column=1)

    label_interval_b = tk.Label(frame, text="Interval [b]:", bg="#F0F0F0")
    label_interval_b.grid(row=2, column=0, sticky="w")

    entry_interval_b = tk.Entry(frame, width=10)
    entry_interval_b.grid(row=2, column=1)

    label_error = tk.Label(frame, text="Error (>0):", bg="#F0F0F0")
    label_error.grid(row=3, column=0, sticky="w")

    entry_error = tk.Entry(frame, width=10)
    entry_error.grid(row=3, column=1)

    calculate_button = tk.Button(frame, text="Calculate", command=calculate, bg="#4CAF50", fg="white")
    calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

    result_label = tk.Label(frame, text="", bg="#F0F0F0")
    result_label.grid(row=5, column=0, columnspan=2)

    iteration_label = tk.Label(frame, text="", bg="#F0F0F0")
    iteration_label.grid(row=6, column=0, columnspan=2)

    root_label = tk.Label(frame, text="", bg="#F0F0F0")
    root_label.grid(row=7, column=0, columnspan=2)

    function_value_label = tk.Label(frame, text="", bg="#F0F0F0")
    function_value_label.grid(row=8, column=0, columnspan=2)

    # Example equations buttons
    example_polynomial_button = tk.Button(frame, text="Polynomial Example", command=lambda: insert_example_equation("x^2 - 4*x + 3"), bg="#2196F3", fg="white")
    example_polynomial_button.grid(row=9, column=0, columnspan=2, pady=5)

    example_trigonometric_button = tk.Button(frame, text="Trigonometric Example", command=lambda: insert_example_equation("sin(x) + cos(x)"), bg="#2196F3", fg="white")
    example_trigonometric_button.grid(row=10, column=0, columnspan=2, pady=5)

    example_exponential_button = tk.Button(frame, text="Exponential Example", command=lambda: insert_example_equation("exp(x) - 2"), bg="#2196F3", fg="white")
    example_exponential_button.grid(row=11, column=0, columnspan=2, pady=5)

    example_fraction_button = tk.Button(frame, text="Fraction Example", command=lambda: insert_example_equation("(1/x) - 2"), bg="#2196F3", fg="white")
    example_fraction_button.grid(row=12, column=0, columnspan=2, pady=5)

    example_combination_button = tk.Button(frame, text="Combination Example", command=lambda: insert_example_equation("(x^2 - 1)/(sin(x) + 1)"), bg="#2196F3", fg="white")
    example_combination_button.grid(row=13, column=0, columnspan=2, pady=5)

def open_fraction_polynomial_window():
    fraction_polynomial_window = tk.Toplevel(root)
    fraction_polynomial_window.title("Fraction Polynomial")
    fraction_polynomial_window.configure(bg="#F0F0F0")

    # Numerator entry
    numerator_label = tk.Label(fraction_polynomial_window, text="Numerator:", bg="#F0F0F0")
    numerator_label.grid(row=0, column=0, sticky="w")
    numerator_entry = tk.Entry(fraction_polynomial_window)
    numerator_entry.grid(row=0, column=1, sticky="w")

    # Denominator entry
    denominator_label = tk.Label(fraction_polynomial_window, text="Denominator:", bg="#F0F0F0")
    denominator_label.grid(row=1, column=0, sticky="w")
    denominator_entry = tk.Entry(fraction_polynomial_window)
    denominator_entry.grid(row=1, column=1, sticky="w")

    def return_values():
        numerator = numerator_entry.get()
        denominator = denominator_entry.get()
        polynomial_str = f"({numerator})/({denominator})"
        polynomial_entry.delete(0, tk.END)
        polynomial_entry.insert(0, polynomial_str)
        fraction_polynomial_window.destroy()

    return_button = tk.Button(fraction_polynomial_window, text="Return", command=return_values, bg="#4CAF50", fg="white")
    return_button.grid(row=2, columnspan=2, pady=10)

def calculate_newton_raphson():
    polynomial_str = polynomial_entry.get()
    x_val = float(x_val_entry.get())
    epsilon_error = float(epsilon_entry.get())

    x = Symbol('x')
    polynomial = sympify(polynomial_str)
    derivative = diff(polynomial, x)

    try:
        derivative_solve = diff(polynomial, x)
    except Exception as e:
        messagebox.showerror("Error", "Error: " + str(e) + "\nPlease check your polynomial.")
        return

    if derivative_solve == 0:
        messagebox.showerror("Error", "Error: Derivative of the polynomial is zero.\nThe Newton-Raphson method cannot converge.")
        return

    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Derivative of Polynomial: " + str(derivative) + "\n\n")

    iterations = 1
    while True:
        poly_solve = polynomial.subs(x, x_val)
        derivative_solve = derivative.subs(x, x_val)
        iterate_x = x_val - (poly_solve / derivative_solve)
        epsilon = abs(iterate_x - x_val)

        result_text.insert(tk.END, f"Iteration {iterations}:\n")
        result_text.insert(tk.END, f"  Function Value: {poly_solve}\n")
        result_text.insert(tk.END, f"  Derivative: {derivative_solve}\n")
        result_text.insert(tk.END, f"  Root: {iterate_x}\n")
        result_text.insert(tk.END, f"  Error: {epsilon}\n\n")

        if epsilon < epsilon_error:
            break

        x_val = iterate_x
        iterations += 1

    result_text.insert(tk.END, f"Root: {iterate_x}\n")
    result_text.insert(tk.END, f"Function Value at Root: {polynomial.subs(x, iterate_x)}\n")
    result_text.insert(tk.END, f"Derivative of Polynomial: {derivative}\n")
    result_text.insert(tk.END, f"Iterations: {iterations}\n\n")
    result_text.config(state=tk.DISABLED)

# Create main window
root = tk.Tk()
root.title("Main Window")
root.configure(bg="#F0F0F0")

# Polynomial entry
polynomial_label = tk.Label(root, text="Enter your polynomial:", bg="#F0F0F0")
polynomial_label.grid(row=0, column=0, sticky="w")
polynomial_entry = tk.Entry(root, width=50)
polynomial_entry.grid(row=0, column=1, columnspan=2)

# Fraction Polynomial button
fraction_button = tk.Button(root, text="Fraction Polynomial", command=open_fraction_polynomial_window, bg="#4CAF50", fg="white")
fraction_button.grid(row=0, column=3, padx=10)

# Initial value entry
x_val_label = tk.Label(root, text="Enter initial value:", bg="#F0F0F0")
x_val_label.grid(row=1, column=0, sticky="w")
x_val_entry = tk.Entry(root)
x_val_entry.grid(row=1, column=1, sticky="w")

# Error entry
epsilon_label = tk.Label(root, text="Enter error or accuracy value:", bg="#F0F0F0")
epsilon_label.grid(row=2, column=0, sticky="w")
epsilon_entry = tk.Entry(root)
epsilon_entry.grid(row=2, column=1, sticky="w")

# Calculate button for Newton-Raphson Method
calculate_button_newton = tk.Button(root, text="Calculate Newton-Raphson", command=calculate_newton_raphson, bg="#2196F3", fg="white")
calculate_button_newton.grid(row=3, column=1, pady=10)

# Result text
result_text = tk.Text(root, height=20, width=70)
result_text.grid(row=4, column=0, columnspan=4, padx=10, pady=10)
result_text.config(state=tk.DISABLED)

# Example buttons
example_polynomial_button = tk.Button(root, text="Example Polynomial: x^2 - 4*x + 3", command=lambda: polynomial_entry.insert(tk.END, "x**2 - 4*x + 3"), bg="#2196F3", fg="white")
example_polynomial_button.grid(row=5, column=0, columnspan=2, pady=5)

example_fraction_polynomial_button = tk.Button(root, text="Example Fraction Polynomial: (x^2 + 1)/(x - 2)", command=lambda: polynomial_entry.insert(tk.END, "(x**2 + 1)/(x - 2)"), bg="#2196F3", fg="white")
example_fraction_polynomial_button.grid(row=6, column=0, columnspan=2, pady=5)

# Open Bisection Calculator button
open_calculator_button = tk.Button(root, text="Open Bisection Calculator", command=open_bisection_calculator, bg="#FF5722", fg="white")
open_calculator_button.grid(row=7, column=0, columnspan=4, pady=20)

root.mainloop()
