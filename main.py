"""
Reverse Polish Notation Calculator
"""

from tkinter import *

win = Tk()
win.geometry("312x324")  
win.resizable(0, 0)
win.title("RPN CALCULATOR")

class Stack:
    """
    Stack for storing elements
    """

    def __init__(self):
        self.stack = []

    def push(self, element):
        """
        Pushes element to stack
        """
        self.stack.append(element)

    def pop(self):
        """
        Pops element from stack
        """
        return self.stack.pop()

    def empty(self):
        """
        Checks if stack is empty
        """
        if not self.stack:
            return True
        else:
            return False

    def top(self):
        """
        Returns top element
        """
        return self.stack[-1]

    def size(self):
        """
        Checks size of stack
        """
        return len(self.stack)

class TransformExpression:
    """
    Transforms conventional notation expression to RPN expression
    """
    
    def __init__(self, stack: Stack):
        self.stack = stack
        self.priority = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }

    def to_list(self, expression: str) -> list:
        """
        Returns a list of elements of expression
        """
        expression = expression.replace(' ', '')
        exp_list = []
        current_number = ''
        for element in expression:
            if element.isdigit() or element == '.':
                current_number += element
            else:
                exp_list.append(current_number)
                exp_list.append(element)
                current_number = ''
        exp_list.append(current_number)

        new_exp_list = []
        for element in exp_list:
            if element.isdigit():
                new_exp_list.append(int(element))
            elif '.' in element:
                new_exp_list.append(float(element))
            else:
                new_exp_list.append(element)
        return new_exp_list

    def transformation(self, expression: list) -> str:
        """
        Returns a string with RPN expression
        """
        postfix_exp = ''
        for el in expression:
            if isinstance(el, int) or isinstance(el, float):
                postfix_exp += str(el) + ' '
            elif el in self.priority.keys():
                if not self.stack.empty() and self.stack.top() != '(':
                    if self.priority[el] > self.priority[self.stack.top()]:
                        self.stack.push(el)
                    else:
                        while not self.stack.empty() and self.stack.top() != '(' \
                                and self.priority[el] <= self.priority[self.stack.top()]:
                            postfix_exp += self.stack.pop() + ' '
                        self.stack.push(el)
                else:
                    self.stack.push(el)
            elif el == '(':
                self.stack.push(el)
            elif el == ')':
                while not self.stack.empty() and self.stack.top() != '(':
                    postfix_exp += self.stack.pop() + ' '
                self.stack.pop()
        while not self.stack.empty():
            postfix_exp += self.stack.pop() + ' '
        return postfix_exp


class Solution:
    """
    Calculates solution for RPN expression
    """
    
    def __init__(self, expression: str):
        self.post = expression

    def display_calculation(self, expression: str) -> list or None:
        """
        Returns calculated result
        """
        if not expression:
            return None
        answer = []
        expression = expression.split()
        stack_solution = [] 
        for element in expression:
            if element.isdigit():
                stack_solution.append(int(element))
            elif '.' in element:
                stack_solution.append(float(element))
            else:
                stack_solution.append(element)
        for t in stack_solution:
            if isinstance(t, int) or isinstance(t, float):
                answer.append(t)
            else:
                a = answer.pop()
                b = answer.pop()
                if t == "+":
                    c = b + a
                elif t == '-':
                    c = b - a
                elif t == '*':
                    c = b * a
                elif t == '/':
                    c = b / a
                    c_str = str(c)
                    if c_str[-2:] == '.0':
                        c = int(c)
                elif t == '^':
                    c = b ** a
                answer.append(c)
        return answer[-1]


if __name__ == '__main__':
    expression = ""
    stack_test = Stack()
    RPN = TransformExpression(stack_test)
    
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear():
    global expression
    expression = ""
    input_text.set("")

def bt_equal():
    global expression
    rpn_list = RPN.to_list(expression)
    num1 = Solution(RPN.transformation(rpn_list))
    result = num1.display_calculation(RPN.transformation(rpn_list))
    result_str = str(result)
    if result_str[-2:] == '01':
        result_str = re.sub('[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?01', '', result_str)
        result = float(result_str)
    input_text.set(result)
    expression = result_str
    
input_text = StringVar()

input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=2)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)
btns_frame = Frame(win, width=312, height=272.5, bg="grey")
btns_frame.pack()

clear = Button(btns_frame, text="C", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: bt_clear()).grid(row=0, column=0, padx=1, pady=1)
left_bracket = Button(btns_frame, text="(", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_click('(')).grid(row=0, column=1, padx=1, pady=1)
right_bracket = Button(btns_frame, text=")", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_click(')')).grid(row=0, column=2, padx=1, pady=1)
divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)
seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)
four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)
one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
              command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)
zero = Button(btns_frame, text="0", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(0)).grid(row=4, column=0, padx=1, pady=1)
exponentiation = Button(btns_frame, text="x^y", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click("^")).grid(row=4, column=1, padx=1, pady=1)
point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)

win.mainloop()
