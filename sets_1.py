# set  = store multiple values in single variable
# unordered
#unchangable / immutable
#duplicate not allow






mySet = {"car","bike","truck","bike",1,2}
mySet2 = {1,2,3}
i = "bike"
if i in mySet:
    print(i)
else:
    print("No")    

tuple1 = ("H","E","L","L","O")
p = list(tuple1)
print(p[0]+p[1]+p[2]+p[3]+p[4])

mySet.add("cycle")
mySet.update(mySet2)
print(mySet)
output2 = mySet2.union(mySet)
output1 = mySet2.symmetric_difference(mySet)
print(output1)
input = mySet2.intersection(mySet2)
print(input)

