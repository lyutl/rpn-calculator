# Calculator based on Reverse Polish Notation (RPN)

---
**RPN Calculator** is an easy-to-use application created for implementation of 
basic mathematical operations. It consists of a keyboard with buttons for digits and basic
arithmetical operations and an output panel.

Calculator uses *Reverse Polish notation* (a mathematical notation in which operators follow their operands)
in order to accelerate calculations.


### Keyboard functions

All functions are available directly from the keyboard. Every keyboard function
also accepts integer numbers as well and float numbers as arguments. Enter the keys and inputs shown 
below and press `=` to evaluate the expression.

`+` Addition.  
*value1 + value2*  
Example:  
9 + 6 returns 15

`-` Subtraction.  
*value1 - value2*  
Example:  
9 - 6 returns 3

`*` Multiplication.  
*value1 * value2*  
Example:  
9 * 6 returns 54

`/` Division.  
*value1 / value2*  
Example:  
9 / 6 returns 1.5

`x^y` x raised to the power of y.  
value<sup>*power*</sup>  
Example:  
2<sup>8</sup> returns 256

`(`, `)` Parentheses.  
Used to enclose a group of objects that should be operated on as a single unit.

> `C` Erases the entire expression.  

> `⌫` Deletes the character to the left of the cursor.

### Wrong input
In the case of wrong input calculator returns `None` value as soon as `=` button is pressed.
Wrong input implies the next cases:

1. Expression is empty;
2. There are only arithmetical operators in expression;
3. Division by zero;
4. Number of arithmetical operators is greater than or equal to the number of arguments;
5. Cases of wrong disposition of brackets (unclosed brackets, closing bracket is before the opening one, etc.).

After getting a `None` value it is necessary to press `C` button and enter a correct expression.

