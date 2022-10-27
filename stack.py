"""
Stack Module
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