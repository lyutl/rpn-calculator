"""
Reverse Polish Notation Calculator
"""

import operator
from stack import Stack
from transform_to_list import conv_to_list, rpn_to_list


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

    def transformation(self, expression: str) -> str or None:
        """
        Returns a string with RPN expression
        """
        postfix_exp = ''
        for element in conv_to_list(expression):
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


class Calculator:
    """
    Calculates solution for RPN expression
    """

    def __init__(self, stack: Stack):
        self.stack = stack
        self.math_operators = {'+': operator.add, '-': operator.sub,
                               '*': operator.mul, '/': operator.truediv,
                               '^': operator.pow}

    def display_calculation(self, expression: str) -> list or None:
        """
        Returns calculated result
        """
        result = None
        for element in rpn_to_list(expression):
            if element.isdigit():
                self.stack.push(int(element))
            elif '.' in element:
                self.stack.push(float(element))
            elif element in self.math_operators:
                first_number = self.stack.pop()
                second_number = self.stack.pop()
                result = self.math_operators[element](second_number, first_number)
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
    if counter_oper == counter_num or counter_oper > counter_num or expression == '.' \
            or '/0' in expression:
        expression = ''
    return expression
