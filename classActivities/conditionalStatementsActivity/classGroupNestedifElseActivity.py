legalAge = 18
drinkingAge = 21

age = int(input("how old are you? "))

if age >= 18:
  if age >= 21:
    print("legal age to drink")
  else: 
    print("not legal age to drink")
else: 
  print("still a child/under age")

#trash day

trashDay = "wednesday"
emptiedAllTrashBinsInApt = False

if trashDay:
  if not emptiedAllTrashBinsInApt:
    print("trash is ready to be taken down to apt complex trash")
else:
  print("please wait until trash day to get trash ready")

currentNum = 1

if currentNum != 0:
  if currentNum == 1:
    currentNum = (currentNum + 2) * 4
  if currentNum == 10:
    print(f"{currentNum} is the currentNum")
  elif currentNum == 11:
    currentNum = currentNum * 12
  elif currentNum == 12:
    currentNum = currentNum + 8
else:
  print("currentNum is zero")

# what will the current number be after the conditional logic?

dogName = "PlutO"

if dogName.lower() == "pluto" and len(dogName) == 5:
  dogName = len(dogName) + 1
  if dogName == "pluto" or dogName == 6:
    print("dogName has been changed")
else:
  print("no valid dogName")

