## What are Datatypes? How to work with Datatypes

In programming, datatypes are important concepts. It is how we work with different forms of data. Data can be composed of paragraphs of text, we can work with numbers, work with binary numbers, booleans and the list goes on. We have different rules to work with datatypes. It is super important to know what your data is made of before approaching a problem. We can even convert data on the fly to reach our answer.

Todays lesson would be about strings, booleans, numeric types, 

## Strings
___

strings is text that is wrapped with single or double quotes around text 

example:

```python
"hello world"
# or
'hello world'
```

having it either format will still get registered as a string. It is good practice to stick to one format for the duration of the project.

There will be times when you will have to use single quote to seperate items that have an apostrophe. 's

python3 allows ease of use for this, but keep in mind that python2 and other programming languages will throw errors if done this way. Python3 supports this.

example

```python
print("isnt that jonathan's laptop?")
# isnt that jonathan's laptop?
print('yes, that is his "laptop"')
#yes, that is his "laptop"
```
we can also have quotes by having a combination of single and double quotes for string syntax. 

correct way to do this with other programming languages and python2

```python
print('isnt that jonathan\'s laptop?')
# isnt that jonathan's laptop?
print("isnt that jonathan\'s \"laptop\"?")
# isnt that jonathan's "laptop"?
```
whichever string syntax you choose for your project, stick to one standard for the life of the project.


we can also use constructor functions to create strings. We pass in the sting inside the arguments of the str() parenthesis

example
```python
greeting = str("hello world")
print(greeting)
#hello world
```

## Numbers
___

with python, we an work with whole numbers and decimal numbers. We can create variables that has a whole number or decimal number.


example
```python
myNum = 7
myNumDec = 7.7
```

In python, we call decimal values floats. Think of it as a floating decimal point floating around the numbers. There are methods that exists to work with numbers. We have methods to round to the nearest whole number, slicing decimal values and even converting data types


## Boolean

Booleans are either true or false values. Booleans are used for conditional logic (if else statements).

the syntax for boolean is the first letter of the word to be capitalized. Python then recognizes the text of true and false to be python specific keywords

example
```python
True
False
```

## String and Number properties and methods
___

As we start using different datatypes in our project, we might want to check out which type we are working with. There is a method called type() which allows us to check in the command line the datatype we are currently working with

```python
type("hello world")
#return string
```

we can also convert strings into numbers and numbers into strings using str() construtor function and int().

keep in mind if you were to add the string of number "5" with int of 5, you will get an error saying you cannot add two different datatypes. The best solution to this is to convert the string of "5" into an int, and then we would be able to add both values together and get the answer of 10.


```python
print(int("5") + 5)
#return 10
```

try experimenting with str() and int

Last method is help()

help allows us to see the rules the function can do. if we were to see that str() constructor function can do, it will show us the description of what str() will do and the class and methods on that class.

example
```python
help(str())

##returns below
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If en
coding or
 |  errors is specified, then the object must expose a data
 buffer
 |  that will be decoded using the given encoding and error
 handler.
 |  Otherwise, returns the result of object.__str__() (if d
efined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return key in self.
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as describ
ed by format_spec.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getitem__(self, key, /)
 |      Return self[key].
 |
 |  __getnewargs__(...)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __len__(self, /)
 |      Return len(self).
 |
 |  __lt__(self, value, /)
 |      Return self<value.


```

and so on, and you can get an idea of how the method works and use it for your program.



