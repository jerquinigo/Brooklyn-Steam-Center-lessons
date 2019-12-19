## Sets
___

Sets are a collections of keys with no values and is unindex and out of order. Its keys are wrapped around curly braces. Sets can be created manualy or can be created by using the set constructor set() by converting a list into a set or any other data strcuture into a set. 

example of manually creating a set
```python
myset = {"cat", "dog", "chinchilla", "turtle"}
print(myset)
#results
{"cat", "dog", "chinchilla", "turtle"}
```

example of using the set method

```python
list1 = ["cat", "dog", "chinchilla", "turtle"]
animalSet = set(list1)
print(animalSet)
#results
{'cat', 'dog', 'chinchilla', 'turtle'}
```

Sets can be loop through to get all values out
```python
for i in myset:
    print(i)
#results
#chinchilla
#turtle
#dog
#cat

```
We can also check to see if a key exists in a set my creating a conditional statement.
example
```python
if "cat" in myset:
    print("true")

print("cat" in myset)
# this second way would return boolean true or false
```

There are two methods to add to the set. add() and update(). add will add one single key to the set and update will add multiple keys to the list. Keep in mind that sets and dictionaries are unordered collections of data. When you print out your set, all the keys will be randomly place. They are not indexed like lists.

example of using the add() method
```python
myset = {"cat", "dog", "chinchilla", "turtle"}
myset.add("dyno")
print(myset)
#results
{'dog', 'chinchilla', 'dyno', 'cat', 'turtle'}
```

example of using the update() method with brackets and without brackets

if you add data to a set with out using brackets, your string will be seperated into individual characters.
example:
```python
myset = {"cat", "dog", "chinchilla", "turtle"}
myset.update("weasel", "furret")
print(myset)
#results
{'cat', 'l', 'chinchilla', 'u', 'dog', 't', 's', 'turtle','w', 'f', 'e', 'a', 'r'}
```

to fix having data entered into multiple strings, we using the [] brackets for python keep each string as a word and insert it into the set as is.

```python
myset = {"cat", "dog", "chinchilla", "turtle"}

myset.update(["weasel", "furret"])
print(myset)
#results
{'furret', 'chinchilla', 'turtle', 'dog', 'weasel', 'cat'}
```

to remove items from a set, you can use either of the two methods. remove() or discard(). We can also use a method just like lists to pop() the last key off a list.

example of remove and discard. (this will remove the key that is put into the parentheses of either remove and discard)

```python
myset = {"cat", "dog", "chinchilla", "turtle"}
myset.remove("cat")
# or use discard
myset.discard("cat")
print(myset)
#results
{'dog', 'turtle', 'chinchilla'}
```

using pop method to remove last key in the set
```python
myset = {"cat", "dog", "chinchilla", "turtle"}
myset.pop()
print(myset)
#results
{'cat', 'chinchilla', 'dog'}
```

keep in mind that the last key in the set might not be the one that you want to removed because sets are not ordered and index like lists