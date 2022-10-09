#company will give bonous based on following criteria

#time spent in company           Bonus

#greater than 10 years            10%

#more than 6 and less 
#        than 10                   8%

#less than 6                        5%




#ask the salary and time spent from the user
#print the net bonous amount accordingly



salary = int(input("current salary:" ))
time = int(input("time spent:"))


if time > 10:
    print(salary + salary*1/10)

elif time > 6 and time < 10:
    print(salary + salary*8/100)  

elif time < 6:
    print(salary + salary*5/100)     