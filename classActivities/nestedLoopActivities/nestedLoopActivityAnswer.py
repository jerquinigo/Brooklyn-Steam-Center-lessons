# 1. using randint, create a range from 1-20 and store it to a variable. use that range to create a list starting with 1 and ending with the last value in the range that was selected. create another list with elements ["red", "blue", "yellow"]. do a nested for loop on both list and print out the values

import random





number = random.randint(1,20)
list2 = ["red", "blue"]

newList = []
for i in range(1,number):
  newList.append(i)

print(newList)


for i in newList:
  print(i)
  for j in list2:
    print(j)




# 2. using the two lists below, create a nested loop using a while loop and a for loop to print out both elements of the list
list1 = [1,2,3,4,5]
list2 = ["blue", "green", "red"]


# for i in list1:
#   print(i)
#   for j in list2:
#     print(j)



i = 0

while i <= len(list1) - 1:
  print(list1[i])
  i = i + 1
  for j in list2:
    print(j)