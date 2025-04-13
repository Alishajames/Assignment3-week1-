#Python Program to Find the Area of a Triangle
a=float(input("Enter 1st side of Triangle: "))
b=float(input("Enter 1st side of Triangle: "))
c=float(input("Enter 1st side of Triangle: "))

s=(a+b+c)/2
A =s*(s-a)*(s-b)*(s-c)
print("Area of triangle is :",A ** 0.5)
    
#Find Quotient and Remainder of Two Numbers
dividend=int(input("Enter dividend Number: "))
divisor=int(input("Enter divisor Number: "))

print("Quotient is: ",dividend // divisor)
print("Remainder is: ",dividend % divisor)

#The program takes a number n and prints an identity matrix of the desired size.
n=input("Enter a Value :")
s=int(input("Enter size of matrix :"))
for r in range(s):
    for co in range(s):
        if r==co:
            print(n,end=" ")
        else:
            print('0',end=" ")
    print()
    
#The program takes two numbers and prints the LCM of two numbers

#Find the Sum of Natural Numbers. 

natur=int(input("Enter Number to sum of Natural no.: "))
na=1
natural=0
while na<=natur:
    natural+=na
    na+=1

print("The Sum of natural no.: ",natural)


#Check If Two Numbers are Amicable Numbers or Not
ami1 = int(input("Enter first number: "))
ami2 = int(input("Enter second number: "))

sum1 = 0
for i in range(1, ami1):
    if ami1 % i == 0:
        sum1 += i


sum2 = 0
for i in range(1, ami2):
    if ami2 % i == 0:
        sum2 += i

# Check if they are amicable
if sum1 == ami2 and sum2 == ami1:
    print(f"{ami1} and {ami2} are Amicable Numbers.")
else:
    print(f"{ami1} and {ami2} are NOT Amicable Numbers.")




    