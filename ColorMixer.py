"""
Student Name: Vrushali Kadam
Student id: 1001514762


Color Mixer
The colors red, blue, and yellow are known as the primary colors because they cannot be made
by mixing other colors. When you mix two primary colors, you get a secondary color, as shown
here:
When you mix red and blue, you get purple.
When you mix red and yellow, you get orange.
When you mix blue and yellow, you get green.
Design a program that prompts the user to enter the names of two primary colors to mix. If the
user enters anything other than “red,” “blue,” or “yellow,” the program should display an error
message. Otherwise, the program should display the name of the secondary color that results.
"""

print("Primary colors: red | blue | yellow")

primary_color1 = input("Enter primary color 1 from the given choices :")
primary_color2 = input("Enter primary color 2 from the given choices :")

#initializing the primary colors.
red="red"
blue="blue"
yellow="yellow"

#condition to get purple color
if (primary_color1 == red and primary_color2 == blue) or  (primary_color1 == blue and primary_color2 == red):
    print("When you mix red and blue, you get purple.")

#condition to get green color.
elif (primary_color1 == blue and primary_color2 == yellow) or (primary_color1 == yellow and primary_color2 == blue):
    print("When you mix blue and yellow, you get green.")

#condition to get orange color.
elif (primary_color1 == yellow and primary_color2 == red) or (primary_color1 == red and primary_color2 == yellow):
    print("When you mix yellow and red, you get orange.")

#prompting the user that the input was wrong.
else:
    print("You didn't select two primary colors from the given option.")