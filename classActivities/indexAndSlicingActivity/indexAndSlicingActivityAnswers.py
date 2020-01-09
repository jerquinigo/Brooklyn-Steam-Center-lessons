
# 1. we have a list of animals. A new animal has entered the showroom. We can to remove dog and update it display room with a wolf. Please use animals1 list below
animals1 = ["cat", "dog", "weasel", "mouse"]

animals1[1] = "wolf"

print(animals1)


# 2. there are strings in our list of numbers. We want to change the elements that are strings into integer datatypes. We should be able to print out the list with all integer values. Please only modify the datatype. Please use numbers1 list below
numbers1 = [4,2,"7", 11, "33", "99"]
numbers1[2] = int(numbers1[2])
numbers1[4] = int(numbers1[4])
numbers1[-1] = int(numbers1[-1])

print(numbers1)


# 3. we have a string "hello world". We want to reverse the string without using a for loop and capitalize all the letters in the string. Please use the variable below

greetings = "hello world"

print(greetings[::-1].upper())


# 4. Please use listNumbers list below. Please slice the list to have the output of [3,5,7,9,11,13]
listNumbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print(listNumbers[2:-1:2])



# 5. Please slice the bracketString variable below. Please slice ["waste"] including the square brackets.
bracketString = 'reduce["waste"]in ny'
print(bracketString[6:15])


# 6. please use randrange to create a list from range 1-20. After a list has been created, please step 2 elements at a time from the beginning of the list to the end of the list

import random

randomNumber1 = random.randrange(1,20)
print(randomNumber1)

newList = []
for i in range(1,randomNumber1):
  newList.append(i)

print(newList[::2])

