import tkinter as tk
from tkinter import messagebox
class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # 显示器
        self.result = tk.StringVar()
        self.result.set(0)
        self.result_label = tk.Label(self.master, textvariable=self.result, font=("Arial", 18), width=20, anchor="e")
        self.result_label.grid(row=0, column=0, columnspan=4)

        # 数字按钮
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("0", 4, 1)

        # 运算符按钮
        self.create_button("+", 1, 3)
        self.create_button("-", 2, 3)
        self.create_button("*", 3, 3)
        self.create_button("/", 4, 3)

        # 其他按钮
        self.create_button(".", 4, 0)
        self.create_button("C", 4, 2)
        self.create_button("=", 5, 3)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, font=("Arial", 18), width=5,
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=column)

    def on_button_click(self, text):
        if text == "C":
            # 清空显示器
            self.result.set(0)
            return

        if text == "=":
            # 计算结果
            try:
                result = eval(self.result.get())
                self.result.set(result)
            except:
                messagebox.showerror("Error", "Invalid expression")
            return

        # 更新显示器
        if self.result.get() == "0": # 如果显示器为0
            self.result.set(text) # 直接替换
            print(f"text: {text}")
        else:
            self.result.set(self.result.get() + text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
