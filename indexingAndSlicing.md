## Indexing And Slicing
___

Lists are a collection of elements which are ordered and able to be mutated. Elements in the lists are indexed and can be retrieved by keying into the list and retrieve or modify the element.

index count starts from 0. If we want to access the first element in a list, we use the number zero.

Example below will demonstrate how we retrieve the first element in a list.

```python
list1 = ["dog", "cat", "parrot"]
print(list1[0])
# will return 
#"dog"
```

we use the variable name the list is stored in and use the square brackets and insert our index number. 

* String characters are also indexed. We can access a character based on its index number.

How would we access the last letter of the string here
```python
name = "Jonathan"
```

using -1 or len(name) -1 will always get the last index of the str or list.

Working on some examples
In class presentation


## Slicing
___
Slice will work on both strings and lists. we will be using square brackets for slicing and it will have a start, stop and stepper

syntax for python- list1[start:stop:step]

lets say we have a string "python" and we want "pyt" we will begin by typing out the string "python" and adding the square brackets next to it. We begin by selecting the index 0 since we want to include "p". to include "pyt", we will have to add one more value to the index. the stop is not inclusive so we have to add one extra number. If we use the index 2, it will not return "t". It will return "py" only. To have it included, we will have to go one number higher. So the stop will be 3. by default, if we do not put anything into the step, by default it will be one.
 the syntax to print out "pyt" will be below

 ```python
 "python"[0:3]
 # will return 
 # "pyt"
 ```

 There are more ways to use slice, and we can even use negative values to move within an index value. We will continue by doing examples in class.
