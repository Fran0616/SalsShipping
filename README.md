# SalsShipping
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package:

Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.


Ground Shipping
=

| Weight of Package | Price per Pound  |Flat Charge  |
| ---------------   | -------------    | -------------|
| 2 lb or less      | $1.50   | $20.00 |
| Over 2 lb but less than or equal to 6 lb	      | $3.50     |$20.00  |
| Over 6 lb but less than or equal to 10 lb	     | $4.00    | $20.00 |
| Over 10 lb    | $4.75    |$20.00  |

Drone Shipping
=

| Weight of Package | Price per Pound |Flat Charge   |
| -------------     | ------------- | -------------|
| 2 lb or less    | $4.50 | $0.00 |
| Over 2 lb but less than or equal to 6 lb     | $9.00 |$0.00  |
| Over 6 lb but less than or equal to 10 lb     | $12.00   | $0.00 |
| Over 10 lb        | $14.25    |$0.00 |



Ground Shipping Premium
=
Flat charge: $125.00


Code
=
```
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
```

Test Data 
=
```
Ground Shipping $ 217.12
Premium groud shipping: $ 125.0
Drone Shipping $ 591.38
```

Conclusion 
= 

In order to solve this problem I used the control flow. The control flow are used in programming to make decisions. The program runs and start moving through its checklist. if the condition is met than an execution occurs. The if statement is used to create control flow in the code, it is accomponny by the elif statement to build additional checks into the if statemnt. The elif statement helps control the order the program check each of the condition in the statement. First the if statement is checked, then each elif statement is checked from top to bottom, then finally the else code is executed if none of the previous conditions have been met.
