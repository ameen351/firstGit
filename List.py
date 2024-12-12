
myList = ["apple", "orange","kiwi", "cherry"]

myList.sort()

print (myList)
newList = []

for fruit in myList:
    if 'a' in fruit:
        newList.append(fruit)

print (newList)

list3 = myList + newList

print (list3)

print(list3.count("apple"))

