"""
Student Name: Vrushali Kadam
Student id: 1001514762


Time Calculator
Write a program that asks the user to enter a number of seconds and works as follows:
There are 60 seconds in a minute. If the number of seconds entered by the user is greater
than or equal to 60, the program should convert the number of seconds to minutes and
seconds.
There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater
than or equal to 3,600, the program should convert the number of seconds to hours,
minutes, and seconds.
There are 86,400 seconds in a day. If the number of seconds entered by the user is greater
than or equal to 86,400, the program should convert the number of seconds to days, hours,
minutes, and seconds.
"""

seconds=int(input("Enter seconds:"))
if seconds>=60 and seconds<3600:
    mins=seconds//60
    remaining_seconds=seconds%60
    print("The calculated time is ",mins," minutes and " ,remaining_seconds, "seconds.")


elif seconds>=3600 and seconds<86400:
    hour=seconds//3600
    remainder=seconds%3600
    mins=remainder//60
    remaining_seconds=remainder%60
    print("The calculated time is ",hour,"hours ",mins," minutes and " ,remaining_seconds, "seconds.")


elif seconds>=86400:
    day=seconds//86400
    rem=seconds%86400
    hour=rem//3600
    rem=rem%3600
    mins=rem//60
    remaining_seconds=rem%60
    print("The calculated time is ",day," day ",hour,"hours ",mins," minutes and " ,remaining_seconds, "seconds.")


else:
    print("The calculated time is ",seconds," seconds.")