"""
TransformToList Module
"""


def conv_to_list(expression: str) -> list:
    """
    Returns a list of elements of conventional expression
    """
    expression = expression.replace(' ', '')
    current_number = ''
    exp_list = []
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


def rpn_to_list(expression: str) -> list:
    """
    Returns a list of elements of RPN expression
    """
    return expression.split()
