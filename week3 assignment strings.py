#The program takes a string and checks if it is a pangram or not.
string="The quick brown fox jumps over the lazy dog"

alpha="qwertyuiopasdfghjklzxcvbnm"

sel=""
i=0
for char in alpha.lower():
    if char in string.lower():
        sel+=char
    
if sel==alpha:
    print("Yes! String is a Pangram ")    
else:
    print("String is Not a Pangram ")


# The program takes a string and replaces every blank space with a hyphen.
string2="The quick brown fox jumps over the lazy dog"
new_string2=string2.replace(' ','-')

print(new_string2)


#display which letters are in the two strings but not in both.
string3="abcz"
string4="abcdefg"

for char in string3:
    if char in string4:
        pass
    else:
        print(char)

for char in string4:
    if char in string3:
        pass
    else:
        print(char)

#Find the Larger String without using Built-in Functions

string5="hello donw"
string6="hello don"

num1=0
num2=0
for i in string5:
    num1+=1

for i in string6:
    num2+=1

if num1>num2:
    print("string 1 have large lenght")
else:
    print("string 2 have large lenght")


#The program takes a string and counts the number of lowercase letters and uppercase letters in the string.
string7="My name is Alisha"

countch=0
countchl=0
for ch in string7:
    if ch.isupper():
        countch+=1
    elif ch.islower():
        countchl+=1
    
print("upper letter in srting is :",countchl)
print("upper letter in srting is :",countch)


#Check if Two Strings are Anagram
string8="listen o"
string9="silent o"

n_string8=string8.replace(" ","").lower()
n_string9=string9.replace(" ","").lower()

if sorted(n_string8)==sorted(n_string9):
    print("Anagram")
else:
    print("Not Anagram")


# Check if the substring is present in the main string
main_string = input("Enter the main string: ")
substring = input("Enter the substring to check: ")

if substring in main_string:
    print(substring," is present in the main string.")
else:
    print(substring,"is not present in the main string.")




#The problem is the display all permutations of a string in lexicographic or dictionary order.


#The program takes a string and calculates the length of the string without using library functions.
istring=input("Enter string to count length ")
count=0
for c in istring:
    if c !=' ':
        count+=1

print("length of string is: ",count)

#Create a New String Made up of First and Last 2 Characters
flstring=input("Enter string to print First and Last 2 Characters: ")

fl=0
if len(flstring)<=4:
    print("enter string more then 4 words")
else:
    print(flstring[0:2],flstring[-2:])


