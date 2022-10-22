# pylint: skip-file
"""
Checks the transformation into RPN
"""

import unittest
import random
from main import Stack, TransformExpression


class RPNTransformation(unittest.TestCase):
    """
    Tests transformation into RPN
    """

    def test_transform_random_expression(self):
        """
        Checks transformation random expression
        """
        nums = [random.randint(1, 1000) for i in range(3)]
        flot = [random.uniform(1, 1000) for i in range(2)]

        equation = f'{nums[1]} * {flot[0]} + {nums[0]} ^ 4 - {flot[1]} / {nums[2]}'
        print(equation)
        expected = f'{nums[1]} {flot[0]} * {nums[0]} 4 ^ + {flot[1]} {nums[2]} / - '

        stack_test = Stack()
        RPN = TransformExpression(stack_test)
        rpn_list = RPN.to_list(equation)

        actual = RPN.transformation(rpn_list)
        print('RPN view: ', actual)

        self.assertEqual(expected, actual)

    def test_transform_brackets_expression(self):
        """
        Checks transformation of expression with brackets
        """
        nums = [random.randint(1, 1000) for i in range(6)]

        equation = f'{nums[1]} * (({nums[2]} + {nums[3]} ^ 4) - ({nums[0]} + {nums[4]})) / {nums[5]}'
        print(equation)
        expected = f'{nums[1]} {nums[2]} {nums[3]} 4 ^ + {nums[0]} {nums[4]} + - * {nums[5]} / '

        stack_test = Stack()
        RPN = TransformExpression(stack_test)
        rpn_list = RPN.to_list(equation)

        actual = RPN.transformation(rpn_list)
        print('RPN view: ', actual)

        self.assertEqual(expected, actual)
