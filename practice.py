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

# ---------------------------------------Identity operators in python------------------------------------------
#identity operators in this below solution we will get a ouput True why? 
#In this case as we can notice that both a and b have same value but the logic behind this is both the values 
# of a and b are getting stored in the same values so in this case it will give true as python is a object oriented 
# programing language the object is getting stored in the same id..  
# a = 5
# b = 5
# print(id(a)) #102962020996136
# print(id(b)) #102962020996136
# print(a  is b) #True


#----------------------------Membership Operator------------------------
# Operators of membership operators are "in" and "not in" 
# Example 

# name = "Gulshan" # In this string suppose we want to check weather the letter small "s" is present in the name or not
# print("s" in name)  #True
# print('b' in name) # False
# print('c' not in name) #True

# list_one = [1,90,2,6 ,89]
# print(1 in list_one) #True
# print(1 not in list_one) #False
# print(3 not in list_one) #True


#---------------------------------Coding Exercise----------------------------
#Question: Calculate the BMI the answer must be a round of value 

# weight = int(input("Enter weight in m: "))
# height = float(input("Enter height in cm: "))
# BMI = weight/(height**2)
# print(int(BMI))


#---------------------------Rounding of function------------------------------
# In this case of rounding we are declarin two values in the round function one is the value and second is the 
# no of decimal values which we want to print  

# int = 98.2355
# print(round(int,1))

# n = 11.5
# print(round(n,2))

# m = 656
# print(round(m,-1)) #670 in case of -1 it will return a value closest multiple of 10^-(-1) so it will give 670

# c = 675
# print(round(c,-1)) # this will print 680 as we have the same above value it will print value of 680 closest value of 10^-(-1)

def count_frequencies(arr):
    count_dict = {}
    
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    return count_dict


# Example usage
arr = [1, 2, 3, 4, 5, 6, 1, 2, 3, 1]
result = count_frequencies(arr)

for key, value in result.items():
    print(f"{key} appears {value} times")
