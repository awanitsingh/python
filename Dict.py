#Dictionary are use to store data values in key value pair
#Ordered
#Duplicates are not allowed
#mutable/changable

myDictionary = {
    "name" : "Awanit",
    "age" : 18,
    "roll no" : 60,
    "CGPA" : 9.9
}
myDictionary["age"] = 20
myDictionary.update({"age":22})
a = myDictionary.get("name")
b = myDictionary["name"] = "Babusaheb"
c =myDictionary.pop("name")
print(a)
print(b)
print(c)
print(myDictionary)
print(len(myDictionary))
print(myDictionary.keys())
print(myDictionary.values())
print(myDictionary.items())


myDictionary1 = {
    "class":{
        "student":{
            "name" : "abc",
            "marks" : {
                "python" : 90,
                "web" : 95
            }
        }
    }
}

print(myDictionary1["class"]["student"]["marks"]["web"])