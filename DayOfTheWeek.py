"""
Student Name: Vrushali Kadam
Student id: 1001514762

Question 1: Day of the Week
Write a program that asks the user for a number in the range of 1 through 7. The program
should display the corresponding day of the week, where 1 = Monday, 2 = Tuesday, 3 =
Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday. The program should
display an error message if the user enters a number that is outside the range of 1 through 7. 
"""


user_input = int(input("Please enter a number from 1 through 7:"))

if user_input== 1:
	print("Monday")

elif user_input==2:
	print("Tuesday")

elif user_input==3:
	print("Wednesday")

elif user_input==4:
	print("Thursday")

elif user_input==5:
	print("Friday")

elif user_input==6:
	print("Saturday")

elif user_input==7:
	print("Sunday")

else:
	print(user_input , " is not a number between 1 through 7.")
	print("Please enter a number within the specific range.")