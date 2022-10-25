"""
Reverse Polish Notation Calculator
"""

import tkinter as tk
import re
from main import Stack, TransformExpression, Solution, check_expression

win = tk.Tk()
win.geometry("312x324")
win.resizable(0, 0)
win.title("RPN CALCULATOR")

if __name__ == '__main__':
    EXPRESSION = ""
    stack_test = Stack()
    RPN = TransformExpression(stack_test)


class Calculator:
    """
    Actions for calculator buttons
    """
    def __init__(self):
        self.expression = ""

    def bt_click(self, item):
        """
        Presses a button
        """
        self.expression = self.expression + str(item)
        unexpected_combos = ['+-', '+*', '+/', '+^', '-+', '-*', '-/', '-^', '*+', '*-',
                             '*/', '*^', '/+', '/-', '/*', '/^', '^+', '^-', '^*', '^/',
                             '++', '--', '**', '//', '^^', '+.', '-.', '*.', '/.', '^.',
                             '.+', '.-', '.*', './', '.^']
        if self.expression[-2:] in unexpected_combos:
            self.expression = self.expression[:-1]
        input_text.set(self.expression)

    def bt_clear(self):
        """
        Clears input field
        """
        self.expression = ""
        input_text.set("")

    def bt_equal(self):
        """
        Outputs the result of expression
        """
        self.expression = check_expression(self.expression)
        rpn_list = RPN.to_list(self.expression)
        num1 = Solution(stack_test)
        rpn_str = RPN.transformation(rpn_list)
        result = num1.display_calculation(num1.to_list(rpn_str))
        result_str = str(result)
        if result_str[-2:] == '01':
            result_str = re.sub('[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?01',
                                '', result_str)
            result = float(result_str)
        self.expression = ""
        input_text.set(result)


calculator = Calculator()
input_text = tk.StringVar()

input_frame = tk.Frame(win, width=312, height=50, bd=0, highlightbackground="black",
                       highlightcolor="black", highlightthickness=2)
input_frame.pack(side=tk.TOP)
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text,
                       width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)
btns_frame = tk.Frame(win, width=312, height=272.5, bg="grey")
btns_frame.pack()

CLEAR = tk.Button(btns_frame, text="C", fg="black", width=10, height=3, bd=0, bg="#eee",
                  cursor="hand2", command=calculator.bt_clear)
CLEAR.grid(row=0, column=0, padx=1, pady=1)
LEFT_BRACKET = tk.Button(btns_frame, text="(", fg="black", width=10, height=3, bd=0, bg="#eee",
                         cursor="hand2",
                         command=lambda: calculator.bt_click('('))
LEFT_BRACKET.grid(row=0, column=1, padx=1, pady=1)
RIGHT_BRACKET = tk.Button(btns_frame, text=")", fg="black", width=10, height=3, bd=0, bg="#eee",
                          cursor="hand2",
                          command=lambda: calculator.bt_click(')'))
RIGHT_BRACKET.grid(row=0, column=2, padx=1, pady=1)
DIVIDE = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee",
                   cursor="hand2",
                   command=lambda: calculator.bt_click("/"))
DIVIDE.grid(row=0, column=3, padx=1, pady=1)
SEVEN = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff",
                  cursor="hand2",
                  command=lambda: calculator.bt_click(7))
SEVEN.grid(row=1, column=0, padx=1, pady=1)
EIGHT = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff",
                  cursor="hand2",
                  command=lambda: calculator.bt_click(8))
EIGHT.grid(row=1, column=1, padx=1, pady=1)
NINE = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff",
                 cursor="hand2",
                 command=lambda: calculator.bt_click(9))
NINE.grid(row=1, column=2, padx=1, pady=1)
MULTIPLY = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee",
                     cursor="hand2",
                     command=lambda: calculator.bt_click("*"))
MULTIPLY.grid(row=1, column=3, padx=1, pady=1)
FOUR = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff",
                 cursor="hand2",
                 command=lambda: calculator.bt_click(4))
FOUR.grid(row=2, column=0, padx=1, pady=1)
FIVE = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff",
                 cursor="hand2",
                 command=lambda: calculator.bt_click(5))
FIVE.grid(row=2, column=1, padx=1, pady=1)
SIX = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff",
                cursor="hand2",
                command=lambda: calculator.bt_click(6))
SIX.grid(row=2, column=2, padx=1, pady=1)
MINUS = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee",
                  cursor="hand2",
                  command=lambda: calculator.bt_click("-"))
MINUS.grid(row=2, column=3, padx=1, pady=1)
ONE = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff",
                cursor="hand2",
                command=lambda: calculator.bt_click(1))
ONE.grid(row=3, column=0, padx=1, pady=1)
TWO = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff",
                cursor="hand2",
                command=lambda: calculator.bt_click(2))
TWO.grid(row=3, column=1, padx=1, pady=1)
THREE = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff",
                  cursor="hand2",
                  command=lambda: calculator.bt_click(3))
THREE.grid(row=3, column=2, padx=1, pady=1)
PLUS = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee",
                 cursor="hand2",
                 command=lambda: calculator.bt_click("+"))
PLUS.grid(row=3, column=3, padx=1, pady=1)
ZERO = tk.Button(btns_frame, text="0", fg="black", width=10, height=3, bd=0, bg="#fff",
                 cursor="hand2",
                 command=lambda: calculator.bt_click(0))
ZERO.grid(row=4, column=0, padx=1, pady=1)
EXPONENTIATION = tk.Button(btns_frame, text="x^y", fg="black", width=10, height=3, bd=0,
                           bg="#fff", cursor="hand2",
                           command=lambda: calculator.bt_click("^"))
EXPONENTIATION.grid(row=4, column=1, padx=1, pady=1)
POINT = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee",
                  cursor="hand2",
                  command=lambda: calculator.bt_click("."))
POINT.grid(row=4, column=2, padx=1, pady=1)
EQUALS = tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee",
                   cursor="hand2",
                   command=calculator.bt_equal)
EQUALS.grid(row=4, column=3, padx=1, pady=1)

win.mainloop()
