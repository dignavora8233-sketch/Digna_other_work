print("Welcome", end=" ")
print("to Python!")

print("Apple", "Banana", "Mango", sep=" | ")


name = input("Enter your name: ")
age = input("Enter your age: ")
hobby = input("Enter your favourite hobby: ")

print(f"Hello , {name} , At {age} , enjoying {hobby} sounds fun!!!!")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)
print("Floor Division =", num1 // num2)
print("Modulus =", num1 % num2)
print("Exponentiation =", num1 ** num2)


integer_num = 10
float_num = 12.5
string_value = "Python"
boolean_value = True
complex_num = 2 + 3j

print(integer_num, type(integer_num))
print(float_num, type(float_num))
print(string_value, type(string_value))
print(boolean_value, type(boolean_value))
print(complex_num, type(complex_num))


a = input("Enter first boolean value (True/False): ") == "True"
b = input("Enter second boolean value (True/False): ") == "True"

print("AND Result :", a and b)
print("OR Result  :", a or b)
print("NOT First  :", not a)
print("NOT Second :", not b)

num = 5
print("Initial Value =", num)

num += 5
print("+= 5 :", num)

num -= 3
print("-= 3 :", num)

num *= 2
print("*= 2 :", num)

num /= 4
print("/= 4 :", num)

