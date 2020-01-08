## Functions, default values,return, args, kwargs, pass, continue, break
___
functions are a block of code that runs the instructions inside its block of code once it has been invoked. It will return its values and reset back to its default settings that were programmed. Once the function completed its task, the results will dissapear. 

Functions should only do one thing. An example of a function doing one thing would be to have one sort a list and return a sorted list. This is good programming habits. We should also include documentation String in our functions so when other programmers use your created functions, they will have an idea how to use it.
An example of using documentation strings in your function

```python
def testFunc():
  '''
  DOCSTRING: Information about the function
  INPUT:  no input...
  OUTPUT: hello test function
  '''
  print("test")


help(testFunc)

# This will return
testFunc()
    DOCSTRING: Information about the function
    INPUT:  no input...
    OUTPUT: hello test function



```

Adding the documentation string will allow the the method help() to print the string information that has been added with instructions on how to use the function.



Functions should only do one thing at a time and also need to return an answer. So far, we have been using print in our functions and it prints the answer to our terminal. If we start working outside terminal, such as using frameworks for web development or backend server development, print might not give us the values we need for our projects. It just prints out the current value of the function at the time print is requested and the function resets itself. To get a value out, we use return and can store the return results to a variable.
Example below.

```python
def addingNums(num1, num2):
  return num1 + num2
answer1 = addingNums(7,7)
print(answer1, "is the answer")
```

using this method, we can have the results of addingNums function and use it wherever we need for the rest of our project, or even use the variable inside another function.


## Default Values
___
functions take in arguments through the parenthesis such as this.
Example
```python
def addNums(arg1, arg2)
```

arg1 and arg2 are placeholders for programmers to pass in their own values for the function to use. It is also good to set up default values in case a programmer does not enter any values or some values. This is so the function will have data to work with regardless of what is entered.

Example
```python
def addNums(arg1=10, arg2=20)
    return arg1 + arg2

results = addNums()
print(results)
```


results will equal 30 if the programmers passes no arguments into the function. Please keep this in mind when creating functions.

## *Args
___
*args is a keyword in python that allows multiple arguments entered in a function to be converted into a tuple. It is a wildcard and is able to take in multiple entries. 
Example of using *args

```python
def printingAll(*args):
    return args
print(printingAll(1,2,3,4))

# will return 
(1, 2, 3, 4)
```

All arguments passed in *args will be return as a tuple


## *kwargs
*kwargs is another keyword in python that allows multiple arguments entered in a function to be converted into a tuple with a dictionary(key value pair). think of nesting. The dictionary key value pair exists within the tuple.

example of using *kwargs
```python
def printingAll2(**kwargs):
  return kwargs,"is the kwargs in the function"
print(printingAll2(person="jonathan", person2="nathalie"))

## will return
({'person': 'jonathan', 'person2': 'nathalie'}, 'is the kwargs in the function')
```

## pass, continue and break

using pass is like using a temporary placeholder. If you leave a block of code incomplete and run it in pycharm, python will respond back with an error stating that code is not working. Sometimes, a programmer might still be figuring out the right logic to put into a block of code and needs to work with other functions. To bypass this in python, we use the keyword pass. It is temporary and should be removed before code goes into production.

Example of using pass

```python
if 10 > 2:
    pass
print("i bypassed it so i can figure out the for loop below")

for i in range(1,101):
    print(i)

```

By using pass, we were able to run the other blocks of code without error, but will need to return to finishing up the block of code currently holding pass.

Continue and break are used to break a running block of code and continue the processes based on a condition. An example would be if a number is present in the range, break loop. Otherwise continue searching the range until end.

example code of using break continue

```python
for i in range(1,51):
  print(i)
  if i == 25:
    break
  else:
    continue
```

In this example, in the if statement, when i is equal to 25, it will break out the loop and end. Any code below break will not be executed. Be aware of that. If the number was not in the range, the else will pick up and continue searching.
