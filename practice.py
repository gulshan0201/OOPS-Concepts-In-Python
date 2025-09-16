# num = input("Enter a two digit number ")

# num_one = num[0]
# num_two = num[1]

# print(int(num_one) + int(num_two))


# height = int(input("Enter your height "))
# weight = float(input('Enter you weight '))
# BMI = weight/(height**2)
# print(BMI)

# a,b = 4,7
# c = (a+b) # 11
# a += 2 # 6
# print(a)
# c += a # 11 + 6
# c /= a
# c // a
# print(c)
# # b %= a
# print(b)

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print("Array:", arr)
# print(arr[0])
# arr[1] = 90
# print(arr)
# # print("Memory address of first element:", arr.ctypes.data)

# arr = [67,89,55,43,12]

# for i in range(10):
#     print(i)

# arr = [10, 20, 30, 40, 50]

# for i in range(len(arr)):
#     print(f"Index {i} has value {arr[i]}")

# Identity operators in python
#identity operators in this below solution we will get a ouput True why? 
#In this case as we can notice that both a and b have same value but the logic behind this is both the values 
# of a and b are getting stored in the same values so in this case it will give true as python is a object oriented 
# programing language the object is getting stored in the same id..  
a = 5
b = 5
print(id(a)) #102962020996136
print(id(b)) #102962020996136
print(a  is b) #True