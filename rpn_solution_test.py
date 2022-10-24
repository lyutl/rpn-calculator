# pylint: skip-file
"""
Checks the solution
"""

import unittest
import random
from main import Stack, TransformExpression, Solution, check_expression


class CalculateExpression(unittest.TestCase):
    """
    Tests calculations
    """

    def test_random_expression(self):
        """
        Checks calculations with random numbers
        """
        nums = [random.randint(1, 1000) for i in range(5)]

        expression = f'{nums[1]} * {nums[2]} + {nums[0]} ^ 4 - {nums[3]} / {nums[4]}'
        print(expression)
        expected = nums[1] * nums[2] + nums[0] ** 4 - nums[3] / nums[4]

        stack_test = Stack()
        RPN = TransformExpression(stack_test)
        expression = check_expression(expression)
        rpn_list = RPN.to_list(expression)
        post = RPN.transformation(rpn_list)

        num1 = Solution(post)
        actual = num1.display_calculation(post)

        self.assertEqual(expected, actual)

    def test_expression_with_brackets(self):
        """
        Checks calculations with brackets
        """
        nums = [random.randint(1, 1000) for i in range(6)]

        expression = f'{nums[1]} * (({nums[2]} + {nums[3]} ^ 4) - ({nums[0]} + {nums[4]})) / {nums[5]}'
        print(expression)
        expected = nums[1] * ((nums[2] + nums[3] ** 4) - (nums[0] + nums[4])) / nums[5]

        stack_test = Stack()
        RPN = TransformExpression(stack_test)
        expression = check_expression(expression)
        rpn_list = RPN.to_list(expression)
        post = RPN.transformation(rpn_list)

        num1 = Solution(post)
        actual = num1.display_calculation(post)

        self.assertEqual(expected, actual)

    def test_expression_with_negative_numbers(self):
        """
        Checks calculations with negative numbers
        """
        nums = [random.randint(1, 1000) for i in range(5)]

        expression = f'-{nums[1]} * (-{nums[2]}) + (-{nums[0]} ^ 4) - (-{nums[3]}) / (-{nums[4]})'
        print(expression)
        expected = -nums[1] * (-nums[2]) + (-nums[0] ** 4) - (-nums[3]) / (-nums[4])

        stack_test = Stack()
        RPN = TransformExpression(stack_test)
        expression = check_expression(expression)
        rpn_list = RPN.to_list(expression)
        post = RPN.transformation(rpn_list)

        num1 = Solution(post)
        actual = num1.display_calculation(post)

        self.assertEqual(expected, actual)

    def test_expression_with_float_numbers(self):
        """
        Checks calculations with float numbers
        """
        nums = [random.uniform(1, 1000) for i in range(6)]

        expression = f'{nums[1]} * ({nums[2]} + {nums[3]} ^ 4) - ({nums[0]} + {nums[4]}) / {nums[5]}'
        print(expression)
        expected = nums[1] * (nums[2] + nums[3] ** 4) - (nums[0] + nums[4]) / nums[5]

        stack_test = Stack()
        RPN = TransformExpression(stack_test)
        expression = check_expression(expression)
        rpn_list = RPN.to_list(expression)
        post = RPN.transformation(rpn_list)

        num1 = Solution(post)
        actual = num1.display_calculation(post)

        self.assertEqual(expected, actual)


class WrongInputExpression(unittest.TestCase):
    """
    Tests cases with wrong input
    """

    def test_empty_expression(self):
        """
        Tests if empty input returns None
        """
        expression = ''
        expected = None

        stack_test = Stack()

        RPN = TransformExpression(stack_test)
        expression = check_expression(expression)
        rpn_list = RPN.to_list(expression)
        post = RPN.transformation(rpn_list)
        num1 = Solution(post)

        actual = num1.display_calculation(post)

        self.assertEqual(expected, actual)

    def test_no_operation_digits(self):
        """
        Tests if program returns the same number in case with no operation digits
        """
        num = random.randint(1, 1000)

        expression = f'{num}'
        print(expression)
        expected = num

        stack_test = Stack()

        RPN = TransformExpression(stack_test)
        expression = check_expression(expression)
        rpn_list = RPN.to_list(expression)
        post = RPN.transformation(rpn_list)
        num1 = Solution(post)

        actual = num1.display_calculation(post)

        self.assertEqual(expected, actual)

    def test_only_operation_digits(self):
        """
        Tests if program returns None in case with only operation digits
        """
        expression = f'+-*/()'
        expected = None

        stack_test = Stack()

        RPN = TransformExpression(stack_test)
        expression = check_expression(expression)
        rpn_list = RPN.to_list(expression)
        post = RPN.transformation(rpn_list)
        num1 = Solution(post)

        actual = num1.display_calculation(post)

        self.assertEqual(expected, actual)

    def test_expression_with_unclosed_brackets(self):
        """
        Tests if program returns None in case with wrong brackets
        """
        expression = '12 + 13 * ((14 + 15) / 16 - 17'
        print(expression)
        expected = None

        stack_test = Stack()
        RPN = TransformExpression(stack_test)
        expression = check_expression(expression)
        rpn_list = RPN.to_list(expression)
        post = RPN.transformation(rpn_list)

        num1 = Solution(post)
        actual = num1.display_calculation(post)

        self.assertEqual(expected, actual)
