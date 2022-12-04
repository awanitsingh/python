#colors = ["Red","Black","Red","Blue","23"]
#cars = ["TATA","NANO","ALTO"]
#players = ("Dhoni","Virat","Pant")
#list are ordered 
#list allows duplicate values
#list are non homogenious
#list are mutable that can change value
#tuple are non mutable that can not change value

#colors [0:2] = "Yellow","Orange"       to exchange specific element in list
#print(colors[1])                       to print specific element from list
#print(colors [::])                     to print whole list
#colors.insert(2,"Indigo")              insert: add element in any place in list
#colors.append("BMW")                   insert: only at last in list
#colors.extend(cars)                    extend: add only one list or tuple
#colors.remove("Red")                   to remove something from list
#colors.pop(3)                          to remove some specific index
#del colors[0]                          to remove something
#colors.clear()                         to delete entire list
#sorting                                arranging in accending order
#reverse                                to reverse the list
#print(color)




for x in range(len(cars)):
   print(cars[x])


x = 0
while x < len(cars):
   print(cars[x]) 
   x += 1
[print(x) for x in cars]  


new_list = []
for x in cars:
   if "A" in x:
       new_list.append(x)
print(new_list)        


new_list = [x for x in cars if x!="TATA"]
print(new_list)

numbers = [1,3,8,3,82,4]
numbers.sort()
numbers.reverse()
print(numbers)


numbers = [1,2,3,4,5]
new_list = []
for i in numbers:
   i = i**2
   new_list.append(i)
print(new_list) 



indx = numbers.index(2)
numbers[indx] = 200
print(numbers)


num2 = numbers.copy()
print(num2)
num2 = list(numbers)
print(num2)



list1 = ["x","y","z"]
list2 = [1,2,3]
list3 = list1 + list2
print(list3)


for x in list2:
   list1.append(x)
print(list1)    


list1.extend(list2)
print(list1)


