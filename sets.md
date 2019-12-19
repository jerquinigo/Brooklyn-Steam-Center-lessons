##Sets
___

Sets are a collections of keys with no values and is unindex and out of order. Its keys are wrapped around curly braces. Sets can be created manualy or can be created by using the set method set() by converting a list into a set or any other data strcuture into a set. 

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