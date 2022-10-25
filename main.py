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

    def transformation(self, expression: list) -> str or None:
        """
        Returns a string with RPN expression
        """
        postfix_exp = ''
        for element in expression:
            if isinstance(element, (float, int)):
                postfix_exp += str(element) + ' '
            elif element in self.priority:
                if not self.stack.empty() and self.stack.top() != '(':
                    if self.priority[element] > self.priority[self.stack.top()]:
                        self.stack.push(element)
                    else:
                        while not self.stack.empty() and self.stack.top() != '(' \
                                and self.priority[element] <= self.priority[self.stack.top()]:
                            postfix_exp += self.stack.pop() + ' '
                        self.stack.push(element)
                else:
                    self.stack.push(element)
            elif element == '(':
                self.stack.push(element)
            elif element == ')':
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

    def __init__(self, stack: Stack):
        self.stack = stack

    def display_calculation(self, expression: str) -> list or None:
        """
        Returns calculated result
        """
        result = None
        expression = expression.split()
        for element in expression:
            if element.isdigit():
                self.stack.push(int(element))
            elif '.' in element:
                self.stack.push(float(element))
            else:
                first_number = self.stack.pop()
                second_number = self.stack.pop()
                if element == "+":
                    result = second_number + first_number
                elif element == '-':
                    result = second_number - first_number
                elif element == '*':
                    result = second_number * first_number
                elif element == '/':
                    result = second_number / first_number
                elif element == '^':
                    result = second_number ** first_number
                self.stack.push(result)
        return self.stack.pop() if not self.stack.empty() else None


def check_expression(expression):
    """
    Checks if an expression is correct
    """
    if expression and expression[0] == '-':
        expression = '0' + expression
    stack_list = []
    for element in expression:
        if element == '(':
            stack_list.append(element)
        elif stack_list and element == ')' and '(' == stack_list[-1]:
            stack_list.pop()
        elif element == ')':
            stack_list.append(element)
    if stack_list and ('(' in expression or ')' in expression):
        expression = ''
        return expression

    counter_num = 0
    counter_oper = 0
    for index, element in enumerate(expression):
        if element.isdigit():
            counter_num += 1
        elif '.' in element:
            counter_num += 1
        elif element in ['+', '-', '*', '/', '^'] and expression[index-1] != '(':
            counter_oper += 1
    if counter_oper == counter_num or counter_oper > counter_num or expression == '.':
        expression = ''
    return expression
