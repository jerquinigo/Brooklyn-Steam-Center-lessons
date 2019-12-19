# Dictionaries and sets 

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