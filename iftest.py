age = int(input("Enter your age: "))
citizen = bool(input("Are you a citizen? "))
if (age > 12) and (age < 18):
   print ("You are above age 12,but too young to vote.")
else:
    print ("You are under 12 and can't vote")
if (age < 18) or (citizen == False):
    print ("Also, you are not a citizen so you can't vote.")
else: 
    print ("You are and adult and a citizen so you can vote!")