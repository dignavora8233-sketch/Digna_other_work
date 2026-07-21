#Q-1

numbers = [10,20,30,40,50]

print("Array Element:")

for i in numbers:
    print(i)


#Q-2

num = [5,10,15,20,25,30]

total = 0
'''
for i in num:
    total += i
'''
for i in num:
    total = total + i

print("Sum =", total)

#Q-3
'''
num =[1,2,3,4,5]

element = int(input("Enter New Element:"))

num.append(element)

print(num)
'''
'''
array = [5,10,15,20,30]

array.insert(4, 25)

print(array)
'''
'''
array = [10, 20, 30, 40, 50]

index = int(input("Enter Position: "))
element = int(input("Enter New Element: "))
'''

#Q-4

num = [10, 20, 30, 40, 50]

num.remove(30)

print(num)

#Q-5

num = [10, 20, 30, 40, 50]

index = int(input("Enter Index: "))
value = int(input("Enter New Value: "))

num[index] = value

print(num)

#Q-7

num1 = [10, 20, 30]
num2 = [40, 50, 60]

num3 = num1 + num2

print(num3)


