

"""
Student Name: Vrushali Kadam
Student id: 1001514762


Age Classifier
Write a program that asks the user to enter a person’s age. The program should display a
message indicating whether the person is an infant, a child, a teenager, or an adult. Following
are the guidelines:
If the person is 1 year old or less, he or she is an infant.
If the person is older than 1 year, but younger than 13 years, he or she is a child.
If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
If the person is at least 20 years old, he or she is an adult."""

Age = float(input("Please input the age for the person to determine age category: "))

#condition to check if the person is an infant
if Age <= 1:
  print("The person is an infant.")

#condition to check if the person is a child.
elif Age > 1 and Age < 13:
  print("The person is a child.")

#condition to check if the person is a teenager.
elif Age >= 13 and Age < 20:
  print("The person is a teenager.")

#condition to check if the person is an adult.
elif Age >= 20:
  print("The person is an adult.")

