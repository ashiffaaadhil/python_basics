#Assignment 1
print("Welcome to Assignment-1")
#Assigment 2
Num1=10
Num2=30
Add=Num1+Num2
print("Num1= ",Num1)
print("Num2= ",Num2)
print("Add= ",Add)
#Assignment 3
print("Body Mass Index")
bmi=float(input("Enter the body mass index value"))
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obesity")
    
#Extra Assignment-1
#print
print("HOPE AI")
#buy input
name=input("Enter your institute name? :")
print(name)
#buy inputs
myname=input("Enter your name? :")
age=input("Enter your age? :")
school_name=input("Enter your school name? :")
degree=input("Enter your degree? :")
print(myname)
print(age)
print(school_name)
print(degree)

#addition
Num1=int(input("Enter your number 1? :"))
Num2=int(input("Enter your number 2? :"))
Add=Num1+Num2
print("Num1= ",Num1)
print("Num2= ",Num2)
print("Add= ",Add)
#subtraction
Num1=int(input("Enter your number 1? :"))
Num2=int(input("Enter your number 2? :"))
Sub=Num1-Num2
print("Num1= ",Num1)
print("Num2= ",Num2)
print("Sub= ",Sub)
#multiplicatiom
Num1=int(input("Enter your number 1? :"))
Num2=int(input("Enter your number 2? :"))
Mul=Num1*Num2
print("Num1= ",Num1)
print("Num2= ",Num2)
print("Mul= ",Mul)
#division
Num1=int(input("Enter your number 1? :"))
Num2=int(input("Enter your number 2? :"))
Div=Num1/Num2
print("Num1= ",Num1)
print("Num2= ",Num2)
print("Div= ",Div)
#floor division
Num1=int(input("Enter your number 1? :"))
Num2=int(input("Enter your number 2? :"))
floordiv=Num1//Num2
print("Num1= ",Num1)
print("Num2= ",Num2)
print("floor div= ",floordiv)
#modulus
Num1=int(input("Enter your number 1? :"))
Num2=int(input("Enter your number 2? :"))
mod=Num1%Num2
print("Num1= ",Num1)
print("Num2= ",Num2)
print("modulus= ",mod)
#power
Num1=int(input("Enter your base? :"))
Num2=int(input("Enter your power? :"))
powerval=Num1**Num2
print("Num1= ",Num1)
print("Num2= ",Num2)
print("power val= ",powerval)
#print 0 to 20
for x in range(0,20):
    print(x)
#print 10 to 20
for x in range(10,21):
    print(x)
#print number of items in list
list_num=[1,2,3,4,5,7,6,0,9,8,7,12]
print(len(list_num))
#print single character
title="artifitial intelligense"
for x in title:
    print(x)
#print odd even number in list
list_num=[1,2,3,4,5,6,7,8,9,0,100,99,87,83,88]
for x in list_num:
    if x%2==0:
        print(x,"is even")
    else:
        print(x," is odd")
#check the entered val is 10
i=int(input("enter the number "))
if i==10:
    print("correct")
else:
    print("in correct")
#check password value
password=input("enter password:")
if password=="Abc123%":
    print("your password is correct")
else:
    print("your password is incorrect")
#age calculator child,adult citizen
age=int(input("enter your age:"))
if age<6:
    print("child")
elif 6<age<20:
    print("Adult")
elif 21<age<60:
    print("Citizen")
elif 60<age<120:
    print("Senior citizen")
else:
    print("invalid age")
#check the number is positive or negative
num=int(input("enter your number:"))
if num<=0:
    print("negative number")
else:
    print("positive number")
#check the number is divide by 5
num=int(input("enter your number:"))
if num%5==0:
    print("The number is divide by 5")
else:
    print("The number is not divide by 5")
#function Assignment-1
def Subfields():
    print("Sub-fields in AI are:")
    list=["machine learning","neural networks","vision","robotics","speech processing","natural language processing"]
    for x in list:
        print(x)
#function to check odd or even
def OddEven():
    num=int(input("enter your number:"))
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")
#check function to marriage is eligible
def Eligible():
    gender=input("enter your gender(male,female)")
    age=int(input("enter your age:"))
    if age>21 and gender=="female":
        print("Eligible")
    elif age>25 and gender=="male":
        print("eligible")
    else:
        print("not eligible")

Eligible()




