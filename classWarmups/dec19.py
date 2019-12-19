# question 1
# multipy each element in the list by 2
# you can mutate the list
# expected output [2,4,6,8,10,12,14]


list1 = [1,2,3,4,5,6,7]
#solution 1
for i in list1:
  print(i * 2)

# solution 2
for i in range(len(list1)):
  print(list1[i] * 2)


# question 2 
# multiply each even element by 2
# you can mutate the array 
# Expected output [1,4,3,8,5,12,7,16]

list2 = [1,2,3,4,5,6,7,8]

for i in list2:
  if i % 2 == 0:
    print(i * 2)
  else:
    print(i)


# question 3
# please remove duplicates in the list
#bonus: also sort the list after duplicates have been removed
#expected output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list3 =[1,2,3,4,5,0,1,2,3,4,5,6,7,8,9,0]


#solution
def removeDups(list1):
  newList = []
  for i in list1:
    print(i,"before the if statement")
    if i not in newList:
      print(i, "the i")
      newList.append(i)
      newList.sort()
      print(newList)


#teach students about sets and it is another way to remove duplicates
# print(set(list1))
removeDups(list3)


#print(type(set(list1)))
