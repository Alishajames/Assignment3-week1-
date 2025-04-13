#Check if a Key Exists in a Dictionary or Not
dic={"name":"Alsiha","age":25,"class":"python","man":True}
check=input("Enter a key to check key is exist or not :")
if check in dic.keys():
    print("Key Exist in Dictionary")
else:
    print("Key is not Exist")


#Program to Add a Key-Value Pair to the Dictionary
dic.update({"city":"lahore"})
print("updated Dictionary",dic)


#program takes a dictionary and prints the sum of all the items in the dictionary
sumdic={"a":2,"b":3,"c":5}

sumt=sum(sumdic.values())

print("sum of all the items in the dictionary: ",sumt)    

#	Python Program to Multiply All the Items in a Dictionary. 

product=1
for value in sumdic.values():
    product*=value

print("product of vlues is : ",product)

#
n = int(input("Enter a number: "))

squares_dict = {x: x**2 for x in range(1, n + 1)}

print("Dictionary of numbers and their squares:")
print(squares_dict)



dict1 = {
    'a': 1,
    'b': 2
}

# Second dictionary
dict2 = {
    'c': 3,
    'd': 4
}

# Concatenate the dictionaries
# Method 1: Using the update() method
combined_dict = dict1.copy()  # Make a copy so original dict1 isn't changed
combined_dict.update(dict2)

# Print the result
print("Concatenated dictionary:")
print(combined_dict)