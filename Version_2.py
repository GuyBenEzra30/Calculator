import math
import tkinter as tk
from tkinter import messagebox

# Button click
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Operations
def operate(op):
    current = entry.get()
    if current == "":
        messagebox.showerror("Error", "Please enter a number first!")
    else:
        entry.insert(tk.END, op)

# Calculate the result
def calculate():
    try:
        expression = entry.get()
        if "√" in expression:
            number = float(expression[1:])  # Get the number after √
            result = math.sqrt(number)
        
        elif "%" in expression:
            number = float(expression[:-1])  # Get the number before %
            result = number / 100
        
        elif "^" in expression:
            number1 = float(expression[:expression.index("^")]) # Get the number before ^
            number2 = float(expression[expression.index("^") + 1:]) # Get the number after ^
            result = number1 ** number2
        
        else:
            result = eval(expression)
        
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed!")
        entry.delete(0, tk.END)
    except Exception:
        messagebox.showerror("Error", "Invalid input!")
        entry.delete(0, tk.END)


# Clear the entry box
def clear():
    entry.delete(0, tk.END)

# Function for square root
def square_root():
    try:
        number = float(entry.get())
        if number < 0:
            messagebox.showerror("Error", "Cannot calculate the square root of a negative number!")
        else:
            entry.delete(0, tk.END)
            entry.insert(0, math.sqrt(number))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# Function for percentage
def percentage():
    try:
        number = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, number / 100)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# Function for power (x^y)
def power():
    current = entry.get()
    if current == "":
        messagebox.showerror("Error", "Please enter a number first!")
    else:
        entry.insert(tk.END, "**")  # '**' is used for power in Python


# Main window
root = tk.Tk()
root.title("Basic Calculator")

# Display numbers and operations
entry = tk.Entry(root, width=35, borderwidth=5, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=5, padx=20, pady=20)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
    ("0", 4, 1), (".", 4, 0), ("C", 4, 2),
]

for (text, row, col) in buttons:
    if text == "C":
        tk.Button(root, text=text, width=10, command=clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=10, command=lambda t=text: button_click(t)).grid(row=row, column=col)

# Operation buttons
operations = [("+", 1, 3), ("-", 2, 3), ("*", 3, 3), ("/", 4, 3)]
for (symbol, row, col) in operations:
    tk.Button(root, text=symbol, width=10, command=lambda s=symbol: operate(s)).grid(row=row, column=col)

# Special operation buttons
tk.Button(root, text="√", width=10, command=square_root).grid(row=5, column=0)  # Square root
tk.Button(root, text="%", width=10, command=percentage).grid(row=5, column=1)  # Percentage
tk.Button(root, text="^", width=10, command=power).grid(row=5, column=2)  # Power
tk.Button(root, text="=", width=10, command=calculate).grid(row=5, column=3)  # Equals

# Run the application
root.mainloop()
