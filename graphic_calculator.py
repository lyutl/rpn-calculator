"""
Reverse Polish Notation Calculator
"""

import tkinter as tk
from button_action import ButtonAction


win = tk.Tk()
win.geometry("312x324")
win.resizable(0, 0)
win.title("RPN CALCULATOR")

if __name__ == '__main__':
    EXPRESSION = ""

input_text = tk.StringVar()
button = ButtonAction(input_text)

input_frame = tk.Frame(win, width=312, height=50, bd=0, highlightbackground="black",
                       highlightcolor="black", highlightthickness=2)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text,
                       width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

buttons_frame = tk.Frame(win, width=312, height=272.5, bg="grey")
buttons_frame.pack()

CLEAR = tk.Button(buttons_frame, text="C", fg="black", width=10, height=3, bd=0, bg="#eee",
                  cursor="hand2", command=button.bt_clear)
CLEAR.grid(row=0, column=0, padx=1, pady=1)
LEFT_BRACKET = tk.Button(buttons_frame, text="(", fg="black", width=10, height=3, bd=0, bg="#eee",
                         cursor="hand2",
                         command=lambda: button.bt_click('('))
LEFT_BRACKET.grid(row=0, column=1, padx=1, pady=1)
RIGHT_BRACKET = tk.Button(buttons_frame, text=")", fg="black", width=10, height=3, bd=0, bg="#eee",
                          cursor="hand2",
                          command=lambda: button.bt_click(')'))
RIGHT_BRACKET.grid(row=0, column=2, padx=1, pady=1)
DIVIDE = tk.Button(buttons_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee",
                   cursor="hand2",
                   command=lambda: button.bt_click("/"))
DIVIDE.grid(row=0, column=3, padx=1, pady=1)
SEVEN = tk.Button(buttons_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff",
                  cursor="hand2",
                  command=lambda: button.bt_click(7))
SEVEN.grid(row=1, column=0, padx=1, pady=1)
EIGHT = tk.Button(buttons_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff",
                  cursor="hand2",
                  command=lambda: button.bt_click(8))
EIGHT.grid(row=1, column=1, padx=1, pady=1)
NINE = tk.Button(buttons_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff",
                 cursor="hand2",
                 command=lambda: button.bt_click(9))
NINE.grid(row=1, column=2, padx=1, pady=1)
MULTIPLY = tk.Button(buttons_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee",
                     cursor="hand2",
                     command=lambda: button.bt_click("*"))
MULTIPLY.grid(row=1, column=3, padx=1, pady=1)
FOUR = tk.Button(buttons_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff",
                 cursor="hand2",
                 command=lambda: button.bt_click(4))
FOUR.grid(row=2, column=0, padx=1, pady=1)
FIVE = tk.Button(buttons_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff",
                 cursor="hand2",
                 command=lambda: button.bt_click(5))
FIVE.grid(row=2, column=1, padx=1, pady=1)
SIX = tk.Button(buttons_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff",
                cursor="hand2",
                command=lambda: button.bt_click(6))
SIX.grid(row=2, column=2, padx=1, pady=1)
MINUS = tk.Button(buttons_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee",
                  cursor="hand2",
                  command=lambda: button.bt_click("-"))
MINUS.grid(row=2, column=3, padx=1, pady=1)
ONE = tk.Button(buttons_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff",
                cursor="hand2",
                command=lambda: button.bt_click(1))
ONE.grid(row=3, column=0, padx=1, pady=1)
TWO = tk.Button(buttons_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff",
                cursor="hand2",
                command=lambda: button.bt_click(2))
TWO.grid(row=3, column=1, padx=1, pady=1)
THREE = tk.Button(buttons_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff",
                  cursor="hand2",
                  command=lambda: button.bt_click(3))
THREE.grid(row=3, column=2, padx=1, pady=1)
PLUS = tk.Button(buttons_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee",
                 cursor="hand2",
                 command=lambda: button.bt_click("+"))
PLUS.grid(row=3, column=3, padx=1, pady=1)
ZERO = tk.Button(buttons_frame, text="0", fg="black", width=10, height=3, bd=0, bg="#fff",
                 cursor="hand2",
                 command=lambda: button.bt_click(0))
ZERO.grid(row=4, column=0, padx=1, pady=1)
EXPONENTIATION = tk.Button(buttons_frame, text="x^y", fg="black", width=10, height=3, bd=0,
                           bg="#fff", cursor="hand2",
                           command=lambda: button.bt_click("^"))
EXPONENTIATION.grid(row=4, column=1, padx=1, pady=1)
POINT = tk.Button(buttons_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee",
                  cursor="hand2",
                  command=lambda: button.bt_click("."))
POINT.grid(row=4, column=2, padx=1, pady=1)
EQUALS = tk.Button(buttons_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee",
                   cursor="hand2",
                   command=button.bt_equal)
EQUALS.grid(row=4, column=3, padx=1, pady=1)

win.mainloop()
