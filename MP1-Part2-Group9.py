import sympy as sp
import math
import tkinter as tk
from tkinter import Label, Entry, Button, StringVar, Toplevel
from math import sqrt

def calculate_arccos(x):
    if -1 <= x <= 1:
        return math.acos(x)
    else:
        return "Error: Input value must be between -1<=x<=1"

def taylor_series_arccos(x, c, n):
    x_sym = sp.Symbol('x')
    c_sym = sp.Symbol('c')
    func = sp.acos(x_sym)
    derivatives = [func.diff(x_sym, i) for i in range(n + 1)]
    series = sum(derivatives[i].subs(x_sym, c_sym) * (x_sym - c_sym)**i / sp.factorial(i)
                 for i in range(n + 1))
    approx = series.subs([(x_sym, x), (c_sym, c)])
    return approx

def truncate_decimal(number, decimal_places):
    power_of_ten = 10 ** decimal_places
    truncated_number = int(number * power_of_ten) / power_of_ten
    return truncated_number

def get_fraction():
    fraction_window = Toplevel(window)
    fraction_window.title("Enter Fraction Value")

    Label(fraction_window, text="Enter Numerator:").pack()
    numerator_entry = Entry(fraction_window)
    numerator_entry.pack()

    def set_numerator_to_pi():
        numerator_entry.delete(0, tk.END)
        numerator_entry.insert(0, str(math.pi))

    def set_numerator_to_e():
        numerator_entry.delete(0, tk.END)
        numerator_entry.insert(0, str(math.e))
    def get_numerator():
        numerator_value = float(numerator_entry.get())
        numerator_entry.delete(0, tk.END)
        fraction_window.destroy()
        get_denominator(numerator_value)
    Button(fraction_window, text="π", command=set_numerator_to_pi).pack()
    Button(fraction_window, text="e", command=set_numerator_to_e).pack()
    Button(fraction_window, text="Submit Numerator", command=get_numerator).pack()

def get_denominator(numerator_value):
    denominator_window = Toplevel(window)
    denominator_window.title("Enter Denominator")
    Label(denominator_window, text="Enter Denominator:").pack()
    denominator_entry = Entry(denominator_window)
    denominator_entry.pack()

    def set_denominator_to_pi():
        denominator_entry.delete(0, tk.END)
        denominator_entry.insert(0, str(math.pi))

    def set_denominator_to_e():
        denominator_entry.delete(0, tk.END)
        denominator_entry.insert(0, str(math.e))

    def get_denominator_value():
        denominator_value = float(denominator_entry.get())
        denominator_entry.delete(0, tk.END)
        answer_frac = numerator_value/denominator_value
        fraction = float(answer_frac)
        entry_x.delete(0, tk.END)
        entry_x.insert(0, str(fraction))
        denominator_window.destroy()

    Button(denominator_window, text="π", command=set_denominator_to_pi).pack()
    Button(denominator_window, text="e", command=set_denominator_to_e).pack()
    Button(denominator_window, text="Submit Denominator", command=get_denominator_value).pack()

def sqrt_val():
    try:
        value = math.sqrt(float(entry_x.get()))
        entry_x.delete(0, tk.END)  # Clear the entry widget
        entry_x.insert(0, str(value))  # Insert the square root value into the entry widget
    except ValueError:
        # Handle the case where the input is not a valid number
        entry_x.delete(0, tk.END)
        entry_x.insert(0, "Invalid input")


def calculate_approximation():
    x = float(entry_x.get())
    c = float(entry_c.get())
    n = int(entry_n.get())
    d = int(entry_d.get())

    user_choice = rounding_chopping_var.get()
    taylor_series_approx = taylor_series_arccos(x, c, n)
    absolute_value = calculate_arccos(x)

    if user_choice == "rounding":
        estimated_value = round(taylor_series_approx, d)
        choiceU = "Rounding"
        if d == 0:
            estimated_value = taylor_series_approx  # No rounding
        else:
            estimated_value = round(taylor_series_approx, d)

    elif user_choice == "chopping":
        estimated_value = truncate_decimal(taylor_series_approx, d)
        choiceU = "Chopping"  # Fix the variable name here
        if d == 0:
            estimated_value = taylor_series_approx  # No chopping
        else:
            estimated_value = truncate_decimal(taylor_series_approx, d)

    absolute_error = (absolute_value - estimated_value)
    relative_error = (absolute_error / absolute_value) * 100

    result_text.set(f"True Value: {absolute_value}\n"
                    f"Taylor Series Approx: {taylor_series_approx}\n"
                    f"Estimated Value ({choiceU}): {estimated_value}\n"
                    f"Absolute Error: {abs(absolute_error)}\n"
                    f"Relative Error: {abs(relative_error)}%")

# Create Tkinter window
window = tk.Tk()
window.title("Arccosine Approximation")

# Create input fields
Label(window, text="Enter the value of x (Must be in x|-1<=x<=1):").pack()
entry_x = Entry(window)
entry_x.pack()

Label(window, text="Enter the center point (c):").pack()
entry_c = Entry(window)
entry_c.pack()

Label(window, text="Enter the order of the derivative (n):").pack()
entry_n = Entry(window)
entry_n.pack()

Label(window, text="Enter the number of decimals for approx value:").pack()
entry_d = Entry(window)
entry_d.pack()

# Create radio buttons for rounding/chopping
rounding_chopping_var = StringVar()
rounding_chopping_var.set("rounding")
rounding_button = tk.Radiobutton(window, text="Rounding", variable=rounding_chopping_var, value="rounding")
rounding_button.pack()
chopping_button = tk.Radiobutton(window, text="Chopping", variable=rounding_chopping_var, value="chopping")
chopping_button.pack()

# Create button for fraction input
fraction_button = Button(window, text="Input Fraction", command=get_fraction)
fraction_button.pack()

# Create calculate button
calculate_button = Button(window, text="Calculate", command=calculate_approximation)
calculate_button.pack()

sqrt_button = Button(window, text="Get Square Root", command=sqrt_val)
sqrt_button.pack()

# Create result label
result_text = StringVar()
result_label = Label(window, textvariable=result_text)
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
