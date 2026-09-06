import tkinter as tk
import math

class ZeroCalc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Zero Calc - V5 GUI")
        self.geometry("320x450")
        self.configure(bg="#2E3440")
        
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        display = tk.Entry(self, textvariable=self.result_var, font=("Arial", 28), bg="#3B4252", fg="#ECEFF4", bd=0, justify="right")
        display.pack(fill=tk.BOTH, ipadx=8, ipady=20, pady=10, padx=10)
        
        buttons_frame = tk.Frame(self, bg="#2E3440")
        buttons_frame.pack(fill=tk.BOTH, expand=True)
        
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('C', '0', '=', '+')
        ]
        
        for row_idx, row in enumerate(buttons):
            buttons_frame.rowconfigure(row_idx, weight=1)
            for col_idx, text in enumerate(row):
                buttons_frame.columnconfigure(col_idx, weight=1)
                btn = tk.Button(buttons_frame, text=text, font=("Arial", 18, "bold"), bg="#4C566A", fg="#ECEFF4", 
                                activebackground="#5E81AC", bd=0, command=lambda t=text: self.on_button(t))
                btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=2, pady=2)

    def on_button(self, char):
        current = self.result_var.get()
        if char == 'C':
            self.result_var.set("0")
        elif char == '=':
            try:
                res = eval(current, {"__builtins__": None, "math": math})
                self.result_var.set(str(res))
            except Exception:
                self.result_var.set("Error")
        else:
            if current == "0" or current == "Error":
                self.result_var.set(char)
            else:
                self.result_var.set(current + char)

if __name__ == "__main__":
    app = ZeroCalc()
    app.mainloop()
