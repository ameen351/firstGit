

myDict = {
    1   :   "ameen",
    2   :   "ajin",
    'a' :   "Test"
}


myDict ["b"] = "du"

print(myDict.get(2))
print (myDict[1])

print(myDict)


if "a" in myDict:
    print("present")
    
# Prints only key
for x in myDict:
    print(x)
    
# Prints only value    
for x in myDict:
    print(myDict[x])
    
    
    
#nested Dict

diction = {
    "name1" : {
        "a" : "ameen",
        "b" : 34
    },
    "name2" : {
        "c" : "ajin",
        "d" : 35
    },
    "name3" : {
        "e" : "du",
        "f" : "tel"
    }
}


print (diction["name1"]["b"])


for x in diction:
    print(diction)