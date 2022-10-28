# Technical Documentation for [RPN Calculator](https://github.com/lyutl/rpn-calculator)

[README.md](https://github.com/lyutl/rpn-calculator/README.md)

## Main files

### [**`main.py`**](https://github.com/lyutl/rpn-calculator/main.py)

Structure of `TransformExpression` and `Calculator` classes.

- class *TransformExpression* contains the single method `transformation` that converts conventional notation expression to RPN expression
- class *Calculator* contains method `display_calculation` that calculates solution for RPN expression using **operator** module
- function `check_expression` checks if an expression is entered correctly in order to prevent errors

### [**`graphic_calculator.py`**](https://github.com/lyutl/rpn-calculator/graphic_calculator.py)

Creates interface of calculator using [tkinter](https://docs.python.org/3/library/tkinter.html) library. 
> This module starts the calculator.

### [**`button_action.py`**](https://github.com/lyutl/rpn-calculator/button_action.py)

Structure of `ButtonAction` class that states actions for calculator buttons.

|function|operation|
|---|---|
|`bt_click`| presses a button |
|`bt_clear`| clears input field |
|`bt_character_clear`| deletes last inputted character |
|`bt_equal`| outputs the result of expression |

### [**`transform_to_list.py`**](https://github.com/lyutl/rpn-calculator/transform_to_list.py)

Contains split function for various types of expressions:
- `conv_to_list`returns a list of elements of conventional expression
- `rpn_to_list` returns a list of elements of RPN expression

### [**`stack.py`**](https://github.com/lyutl/rpn-calculator/stack.py)

Realisation of `Stack` class for storing elements.

|method|operation|
|---|---|
|`push`| pushes element to stack |
|`pop`| pops element from stack |
|`empty`| checks if stack is empty |
|`top`| returns top element |
|`size`| checks size of stack |

## Other files

| File | Realised logic |
|---|---|
| [`requirements.txt`](https://github.com/lyutl/rpn-calculator/requirements.txt) | states the required packages |
| [`rpn_calculator_test.py`](https://github.com/lyutl/rpn-calculator/rpn_calculator_test.py) | tests the accuracy of calculations and ability to deal with wrong input |
| [`rpn_transform_test.py`](https://github.com/lyutl/rpn-calculator/rpn_calculator_test.py) | tests the accuracy of transformation of expression into reverse polish notation |
