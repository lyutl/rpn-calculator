# pylint: skip-file
"""
Checks the solution
"""

import unittest
import random
from main import Stack, TransformExpression, Solution


class CalculateExpression(unittest.TestCase):
    """
    Tests calculating expression
    """

    def test_two_digit_random_expression(self):
        """
        Checks calculations with two-digit numbers
        """

        nums = [random.randint(10, 99) for i in range(5)]

        equation = f'{nums[1]} * {nums[2]} + {nums[0]} ^ 4 - {nums[3]} / {nums[4]}'
        print(equation)
        expected = nums[1] * nums[2] + nums[0] ** 4 - nums[3] / nums[4]

        stack_test = Stack()
        RPN = TransformExpression(stack_test)
        rpn_list = RPN.to_list(equation)
        post = RPN.postfix(rpn_list)

        num1 = Solution(post)
        actual = num1.display_calculation(post)

        self.assertEqual(expected, actual)

    def test_expression_with_brackets(self):
        """
        Checks calculations with brackets
        """
        nums = [random.randint(1, 99) for i in range(6)]

        equation = f'{nums[1]} * ({nums[2]} + {nums[3]}) - ({nums[0]} + {nums[4]}) / {nums[5]}'
        print(equation)
        expected = nums[1] * (nums[2] + nums[3]) - (nums[0] + nums[4]) / nums[5]

        stack_test = Stack()
        RPN = TransformExpression(stack_test)
        rpn_list = RPN.to_list(equation)
        post = RPN.postfix(rpn_list)

        num1 = Solution(post)
        actual = num1.display_calculation(post)

        self.assertEqual(expected, actual)

    def test_expression_with_float_numbers(self):
        """
        Checks calculations with float numbers
        """
        nums = [random.uniform(1, 99) for i in range(6)]

        equation = f'{nums[1]} * ({nums[2]} + {nums[3]}) - ({nums[0]} + {nums[4]}) / {nums[5]}'
        print(equation)
        expected = nums[1] * (nums[2] + nums[3]) - (nums[0] + nums[4]) / nums[5]

        stack_test = Stack()
        RPN = TransformExpression(stack_test)
        rpn_list = RPN.to_list(equation)
        post = RPN.postfix(rpn_list)

        num1 = Solution(post)
        actual = num1.display_calculation(post)

        self.assertEqual(expected, actual)


class WrongInputExpression(unittest.TestCase):
    """
    Tests calculating expression
    """

    def test_wrong_type_of_input(self):
        """
        Tests if non-string input returns None
        """
        equation = [13, '*', 12, '+', 67]
        expected = None

        stack_test = Stack()
        RPN = TransformExpression(stack_test)
        rpn_list = RPN.to_list(equation)
        post = RPN.postfix(rpn_list)

        num1 = Solution(post)
        actual = num1.display_calculation(post)

        self.assertEqual(expected, actual)

    def test_wrong_type_of_symbols(self):
        """
        Tests if input with non-suitable symbols returns None
        """
        equation = '5ac67be'
        expected = None

        stack_test = Stack()
        RPN = TransformExpression(stack_test)
        rpn_list = RPN.to_list(equation)
        post = RPN.postfix(rpn_list)

        num1 = Solution(post)
        actual = num1.display_calculation(post)

        self.assertEqual(expected, actual)

    def test_empty_expression(self):
        """
        Tests if empty input returns None
        """
        equation = ' '
        expected = None

        stack_test = Stack()

        RPN = TransformExpression(stack_test)
        rpn_list = RPN.to_list(equation)
        post = RPN.postfix(rpn_list)
        num1 = Solution(post)

        actual = num1.display_calculation(post)

        self.assertEqual(expected, actual)

    def test_no_operation_digits(self):
        """
        Tests if program returns the same number in case with no operation digits
        """
        num = random.randint(100, 1000)

        equation = f'{num}'
        print(equation)
        expected = num

        stack_test = Stack()

        RPN = TransformExpression(stack_test)
        rpn_list = RPN.to_list(equation)
        post = RPN.postfix(rpn_list)
        num1 = Solution(post)

        actual = num1.display_calculation(post)

        self.assertEqual(expected, actual)
