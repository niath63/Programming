

'''a=int(input("Enter your choice"))


if a>60:
    print("I like Apple")
elif a>30:
    print("I like Chocolate")
elif a>20:
    print("I like Ice Cream")
else:
    print("I do not like anything")
'''
'''year=int(input("Enter Year"))
if(year % 4==0 and year % 100 != 0) or (year % 400 == 0):
    print("Year is Leap")
else:
    print("Year is not Leap")'''

side1=float(input("Enter 1st side"))
side2=float(input("Ender 2nd side"))
side3=float(input("Ender 3rd side"))

if(side1>0 and side2>0 and side3>0):
 if(side1==side2==side3):
    print("Triangle is Equilateral")
 elif( side1==side2 or side1==side3 or side2==side3):
    print("Triangle is Isosceles")
 elif(side1!=side2!=side3):
    print("Triangle is Scalene")
else:
 print("invelid Input")



