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





