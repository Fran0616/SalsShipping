weight = 41.5

#groud shipping
if weight <= 2:
  price = weight * 1.50 + 20
elif weight <= 6:
  price = weight * 3.00 + 20
elif weight <=10:
  price = weight * 4 + 20.00
else:
  price = weight * 4.75 + 20 

print('Ground Shipping $',format(price, ".2f"))
costPremium = 125.00
print("Premium groud shipping: $", costPremium)

#drone shipping
if weight <= 2:
  price = weight * 4.50 
elif weight <= 6:
  price = weight * 9.00 
elif weight <=10:
  price = weight * 12.00 
else:
  price = weight * 14.25
print('Drone Shipping $', format(price, ".2f"))
