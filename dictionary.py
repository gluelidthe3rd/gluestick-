dictionary = {"apple":"A red circular fruit","banana":"A long yellow fruit","sugarcane":"A tall , sweet crop"}

print(dictionary)

print(dictionary["apple"])
print(dictionary.keys())
print(dictionary.values())

for i in dictionary:
    print(i,dictionary[i])

g = input("Enter the word uo think is in the dictionary? -")

if g in dictionary:
    print("This in the dictionary!")
else:
    print("this is not in the dictionary!")