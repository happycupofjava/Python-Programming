
"""
Student Name: Vrushali Kadam
Student id: 1001514762


Restaurant Selector
You have a group of friends coming to visit for your high school reunion, and you want to take
them out to eat at a local restaurant. You aren’t sure if any of them have dietary restrictions, but
your restaurant choices are as follows:

Joe’s Gourmet Burgers—Vegetarian: No, Vegan: No, Gluten-Free: No
Main Street Pizza Company—Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
Corner Café—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten-Free: No
The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
Write a program that asks whether any members of your party are vegetarian, vegan, or glutenfree,
to which then displays only the restaurants to which you may take the group. Here is an

example of the program’s output:
Is anyone in your party a vegetarian? yes
Is anyone in your party a vegan? no
Is anyone in your party gluten-free? yes
Here are your restaurant choices:
Main Street Pizza Company
Corner Cafe
The Chef's Kitchen

Here is another example of the program’s output:
Is anyone in your party a vegetarian? yes
Is anyone in your party a vegan? yes
Is anyone in your party gluten-free? yes
Here are your restaurant choices:
Corner Cafe
The Chef's Kitchen
"""
#initializing the flags for the three options
veg=False
vegan=False
gluten=False

#taking the user input
var1=input("Is anyone in your party a vegetarian?")
var2=input("Is anyone in your party a vegan?")
var3=input("Is anyone in your party gluten-free?")

#conditions to set the flags
if var1=='Yes' or var1=='yes' or var1=='YES':
	veg=True
if var2=="Yes" or var2=='yes' or var2=='YES':
	vegan=True
if var3=='Yes' or var3=='yes' or var3=='YES':
	gluten=True

#printing the choices based on the flags
print("Here are you choices:")

#Corner Café—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes and The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
if veg== True and vegan== True and gluten==True:
	print("The Chef’s Kitchen or Corner Café—Vegetarian")

#Joe’s Gourmet Burgers—Vegetarian: No, Vegan: No, Gluten-Free: No
if veg== False and vegan== False and gluten== False:
	print("Joe’s Gourmet Burgers—Vegetarian")

#Main Street Pizza Company—Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
if veg==True and vegan==False and gluten==True:
	print("Main Street Pizza Company—Vegetarian")

#Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten-Free: No
if veg==True and vegan==False and gluten==False:
	print("Mama’s Fine Italian—Vegetarian")
