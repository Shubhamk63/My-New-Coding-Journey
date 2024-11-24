# # using exponentiation

# a = int(input("enter any number: ")) 

# sr = a**(0.5)

# print("the square root of the number is:",sr) 

# # # using math module  

# import math 

# a = int(input("enter any number: ")) 

# sr = math.sqrt(a) 
# print(sr)  

# from functools import reduce

# a = [2,3,4,5]

# def sum(a,b):
#     return a+b

# sum8 = reduce(sum,a) 
# print(sum8) 

# finding area of circle

# a = int(input("enter any nubmber: "))
# b = 22/7
# c = (b*a*2)
# print(c) 

a = [9,25,49,64,81]

b = map(lambda x:x**0.5 ,a)
print(list(b))  