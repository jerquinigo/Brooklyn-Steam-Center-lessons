## If Else / Nested If Else Statements
___

so far we have an understanding that if else statements are conditional logic based on a condition being true or false. Depending on the outcome, the correct block of code will be executed.

```python
if condition1:
    print("printing in the if block")
else:
    print("printing in the else block")
```
with nested if else statements, we pass in another set of conditional logic within the block of code of the first set of conditional logic. Below is an example of how nested statements look. 

```python
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
```