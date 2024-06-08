import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(0, 0)
        
        self.expression = ""
        
        self.display_text = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Entry widget for display
        display_frame = tk.Frame(self.root)
        display_frame.pack(expand=True, fill="both")
        
        display_entry = tk.Entry(display_frame, font=('Arial', 24), textvariable=self.display_text, justify='right', bd=20)
        display_entry.pack(expand=True, fill="both")
        
        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill="both")
        
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '←',
            '1', '2', '3', '-', '(',
            '0', '.', '=', '+', ')'
        ]
        
        row = 0
        col = 0
        
        for button in buttons:
            button_command = lambda x=button: self.on_button_click(x)
            b = tk.Button(button_frame, text=button, font=('Arial', 18), command=button_command)
            b.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
            
            col += 1
            if col > 4:
                col = 0
                row += 1
        
        # Configure grid weights
        for i in range(5):
            button_frame.columnconfigure(i, weight=1)
        for i in range(5):
            button_frame.rowconfigure(i, weight=1)
    
    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '←':
            self.expression = self.expression[:-1]
        elif char == '=':
            try:
                result = eval(self.expression)
                self.expression = str(result)
            except:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
        else:
            self.expression += str(char)
        
        self.display_text.set(self.expression)

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
