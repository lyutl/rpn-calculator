"""
Reverse Polish Notation Calculator
"""


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
        if expression and expression[0] == '-':
            expression = '0' + expression
        for element in expression:
            if element.isdigit() or element == '.':
                current_number += element
            elif exp_list and exp_list[-1] == '(' and element == '-' and not current_number:
                exp_list.append('0')
                exp_list.append(element)
            else:
                if current_number:
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
        
        flag = 0
        for element in expression:
            if element.isdigit():
                flag = 1
                break
        if flag == 0:
            return None

        counter = 0
        for element in expression:
            if element == '(':
                counter += 1
            if element == ')':
                counter -= 1
        if counter != 0:
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
