
import random

userInput = input("hello what is your name? ")
print("hello" + " " + userInput)

print("we are going to begin by starting to show you a range of numbers up to your favorite number.")

favoriteNumber = int(input("what is your favorite number "))

computerFavRan = int(random.randint(1,100))


print(f"ahhh, i see your favorite number is {favoriteNumber}. My favorite number is {computerFavRan}")

print("lets begin by looping through the range of your favorite numbers")

computerFinalResponse = False

def favNumberRange(myFavorite, computerFavorite):
  found = False
  if myFavorite == computerFavorite:
    print(f"| (• ◡•)| my {computerFavorite} is within your range")

  for i in range(1, myFavorite + 1):
    if computerFavorite == int(i):
      print(f"| (• ◡•)| my {computerFavorite} is within your range")
      found = True
      global computerFinalResponse
      computerFinalResponse = True
  
  if found == False:
    print("""
        ||•  -  •  ||
      √ ||--–----||√
        ||+   °  •||

        my favorite number {0} is not within your range
    """.format(computerFavorite))


favNumberRange(favoriteNumber, computerFavRan)

if computerFinalResponse == True:
  print("""
  ＼(＾O＾)／ my favoriteNumber {0} was present. Thank you for playing.
  """.format(computerFavRan))

elif computerFinalResponse == False:
  print("Thank you {0} for playing. Next time i hope my favorite number of {1} is in range".format(userInput, computerFavRan))
