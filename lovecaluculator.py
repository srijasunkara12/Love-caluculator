name1 = input("Enter name of 1st person: ")
name2 = input("Enter name of 2nd person: ")
combine_string = name1 +name2
lower_case_string  = combine_string.lower()
t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')
l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')
a = t+r+u+e
b = l+o+v+e
c = (a*10)+b
print("True love is "+str(c)+"%")
roll =[18,2,4,3,10]
print(roll[1])
roll.reverse()
print(roll)
print(max(roll))
print(min(roll))
roll.sort()
print(roll)
roll.remove(4)
print(roll)



