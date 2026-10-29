# import math
# # import random
# from practical6calculator import add, subtract, multiply, divide

# #calculator

# print(add(5,3))
# print(subtract(5,3))
# print(multiply(5,3))
# print(divide(5,3))


# #Math module
# n=int(input("Enter a number:"))

# if n >= 0:
#     print("Square root:", math.sqrt(n))
#     print("Factorial:",math.factorial(n))

# else:
#     print("Square root not possible")
#     print("Squrae:", n**2)


# #Random quiz
questions=[("2+3=?", "5"),("5*2=?", "10"),("10-4=?", "6"),("12/3=?", "4"),("Square of 4?", "16")]

q = random.choice(questions)
print("Random Question :", question[0])


answer = input("Answer: ")

if answer == q[1]:
    print("Correct!")
else:
    print("Wrong! Answer:", q[1])



