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
        result = eval(entry.get())
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

# Equal button
tk.Button(root, text="=", width=10, command=calculate).grid(row=5, column=0, columnspan=4)

# Run the application
root.mainloop()
