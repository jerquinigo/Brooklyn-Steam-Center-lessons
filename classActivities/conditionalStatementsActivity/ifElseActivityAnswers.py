shippingContainers = 50
shippingContainersLeft = 4
# please create a conditional statement that shows if shipping containers are less than or equal to 10, to order more containers, otherwise enough containers are present
if(shippingContainersLeft <= 10):
  print("need to order more containers")
else:
  print("enough containers are present")
currentItemPrice = 5.99
salePrice = 3.49
# please create a conditional statement that shows if the currentItemPrice is not equal to sale price, to return to the customer "item is not on sale". Otherwise, return "current price is 5.99"
if currentItemPrice != salePrice:
  print("item is not on sale")
else:
  print(f"current price is {currentItemPrice}")


# please create a conditional statment that has 10 greater than 5 or 5 is equal to 5, print 10 and 5 are our numbers. Otherwise print out 5 is not greater or equal to 5

if 10 > 5 or 5 == 5:
  print("10 and 5 are our numbers")
else:
  print("5 is not greater or equal to 5")
  
# please fix this conditional statement. Begin by uncommenting the block of code
if 100 < 10:
 print("number is greater")

elif 50 > 30:
    print("50 is greater") 
else:
   print("current numbers are nulled")