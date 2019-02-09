"""
Student Name: Vrushali Kadam
Student id: 1001514762


Software Sales
A software company sells a package that retails for $99. Quantity discounts are given according
to the following table:
Quantity Discount
10–19 10%
20–49 20%
50–99 30%
100 or more 40%
Write a program that asks the user to enter the number of packages purchased. The program
should then display the amount of the discount (if any) and the total amount of the purchase
after the discount.
"""

quantity=int(input("enter no. of packages: "))
#calculating the initial price withput discount
price=quantity*99

#calculating the no discount quantity since discounts are only available for quantity more than 10
if quantity<10:
    print("No discount.")
    discount=0
#calculating the discount for quantity between 10 to 19
elif quantity>=10 and quantity<=19:
    discount = price*0.1
    print("CONGRATULATIONS!! you got a discount of 10%")

#calculating the discount for quantity between 20 to 49
elif quantity>=20 and quantity<=49:
    discount = price*0.2
    print("CONGRATULATIONS!! you got a discount of 20%")

#calculating the discount for quantity between 50 to 99
elif quantity>=50 and quantity<=99:
    discount = price*0.3
    print("CONGRATULATIONS!! you got a discount of 30%")

#calculating the discount for quantity more than 100
else:
    discount = price*0.4
    print("CONGRATULATIONS!! you got a discount of 40%")

#printing the discount calculated based on the quantity entered
print("you got a discount of: $",discount)

#calculating the final price
final_price=price-discount

#printing the final price
print("the total amount is: $", final_price)