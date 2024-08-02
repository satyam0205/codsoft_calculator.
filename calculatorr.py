import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.entry = tk.Entry(root, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.root, text=button, width=5, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(self.root, text="C", width=21, command=self.clear_entry).grid(row=row_val, column=0, columnspan=4)
        tk.Button(self.root, text="**", width=5, command=lambda: self.click_button('**')).grid(row=row_val+1, column=0)
        tk.Button(self.root, text="%", width=5, command=lambda: self.click_button('%')).grid(row=row_val+1, column=1)
        tk.Button(self.root, text="(", width=5, command=lambda: self.click_button('(')).grid(row=row_val+1, column=2)
        tk.Button(self.root, text=")", width=5, command=lambda: self.click_button(')')).grid(row=row_val+1, column=3)

    def click_button(self, button):
        if button == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            self.entry.insert(tk.END, button)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")
calc = Calculator(root)
root.mainloop()