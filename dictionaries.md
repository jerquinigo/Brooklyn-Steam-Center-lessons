

## Dictionaries
___
In python, Dictionaries are made up of unordered collection of key value pairs. Dictionaries use curly braces and a colon to set up the data type. Dictionary keys need to be unique, there are no repeats. Values can repeat.


example:

```python
    people = {
        "Jonathan": 28,
        "Nathalie": 25,
        "Daniel": 35
    }
```

Within the curly braces, the values on the left side of the colon will be the keys and to the right of the colon will be keys. Commas are places at the end of each key value pair to seperate each pair. Without this comma, python will throw an error. We can print all key value pairs for a dictionary. Printing all people would result 

```python
print(people)
#results below
{'Jonathan': 28, 'Nathalie': 25, 'Daniel': 35}
```

if we want to retrieve a value, lets say the age of jonathan, we would have to use the key to get to the value. we would use the key we want from the dictionary, and the dictonary will match it with its own key and return the value. If i want to retrieve Jonathan's age, i would use the key "Jonathan" and and key into my dictionary, the dictionary will compare if the key "Jonathan" exists. If it exists, it will return the value of 28.

example
``` python
print(people["Jonathan"])
# using the key to get the value of that key 
#returns 28
28
```

we can also overwrite values in the dictionary. Lets say Jonathan's birthday just recently passed and now he is 29 years old. The dictionary still shows that he is younger than he is supposed to be. Using the method to key into the dictionary, we can use it to overwrite his age.

example
```python
    people["Jonathan"] = 29
    print(people)
    #results
    {'Jonathan': 29, 'Nathalie': 25, 'Daniel': 35}

```

only the value of the key got affected, the rest of the key value pairs remain the same.

We can also loop through dictionaries. It only loops either by key or value. An example of printing all the keys would be

```python 

for i in people:
    print(i)
#results
#Jonathan
#Nathalie
#Daniel
```

to print out all the values of the keys example (key into the values)

```python
for i in people:
    print(people[i])
#results 
#28
#25
#35
```

there is also a value method that can be used that will print out all the values just like example above

```python
for i in people.values():
    print(i)
#results
#28
#25
#35
```

we can also create new key value pairs for the dictionary. To create a new pair, first add a unique key and key into the dictionary and assign a value to the key as so

```python
    people["Derek"] = 22
```

Derek has been added to the people dictionary with his age. What if i want to check if one of the people currently exists in the dictionary?

we can use conditional statement and keyword * in *

```python
if "Derek" in people:
    print("Derek is present")
else:
    print("not Present")
```

___
## Advance dictionary functions
___

We can print out both the keys and values with items() method. The results will be returned as a tuple(* we will cover tuples in the future * )

```python
    for i, j in people.items():
        print(i,j)
    #results
#('Jonathan', 28)
#('Nathalie', 25)
#('Daniel', 35)

# the parenthesis around the data represent tuple data type. 
```

___
## Extra functions for dictionaries

to check the length of a dictionary
```python
print(len(people))
```

we can use the pop() method similar to lists and specify which key value pair to remove my selecting the specific key
example
```python
people.pop("Jonathan")
print(people)
#results 
# {'Nathalie': 25, 'Daniel': 35}
# key and value of jonathan and 28 are now removed
```




