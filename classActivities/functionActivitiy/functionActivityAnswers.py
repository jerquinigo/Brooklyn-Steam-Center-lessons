
# Please create a function that takes in a number and prints the range of that number with even numbers representing the text "fizz" and odd numbers representing the text "buzz" and the rest of the number with "fizzbuzz". If no number is passed into the argument, please give it a default value of 100

# def fizzbuzz(number = 100):
#   for i in range(1,number + 1):
#     if i % 2 == 0:
#       print("fizz")
#     elif i % 3 == 0:
#       print("buzz")
#     else: print("fizzbuzz")


# fizzbuzz(10)

# please create a function that will take in a string and will remove any vowels from the strings. vowels = ['a','e','i','o','u']. if no string is entered in the argument, please have a default value of "hello world"
def remove_vowels(string = "hello world"):
	vowels = ['a','e','i','o','u']
	s = ''
	for thing in string:
		if thing not in vowels:
			s+=thing
	return s

print(remove_vowels())


#Create a function that counts the number of times a particular letter shows up in the word search. A list is provided. Please create a function with two arguments. First argument should take in listCounter list and second argument should take in a letter from the list. If no letter is passed in, please make the letter default value to equal "D"
listCounter =  ["D", "E", "Y", "H","A", "D","C", "B", "Z", "Y", "J", "K","D", "B", "C", "A", "M", "N","F", "G", "G", "R", "S", "R","V", "X", "H", "A", "S", "S"]

def letter_counter(list1, letter = "D"):
  count = 0
  for i in list1:
    if i == letter:
      count = count + 1
  return count

print(letter_counter(listCounter, "D"))



for i in range(1,51):
  print(i)
  if i == 25:
    break
  else:
    continue