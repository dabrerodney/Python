# n = int(input("Enter n: "))
# a = 0
# b = 1
# i = 0
# print("Fibonacci series: ")
# while i<n:
#     print (a)
#     c = a + b
#     a = b
#     b = c
#     i += 1

# t1 = (10, 20, 30)
# t2 = (40, 50, 60)
# print("Before interchanging: ")
# print("t1: ",t1)
# print("t2: ",t2)

# t1, t2 = t2, t1
# print("After Interchanging")
# print("t1: ",t1)
# print("t2: ",t2)

# def validate(value): 
#     if value<0: 
#         raise ValueError("Value cannot be less than 0 ") 

# try: 
#     num=int(input("Enter a value : ")) 
#     validate(num) 
#     print("Value is valid") 
# except ValueError as e: 
#     print("Error : "+str(e))

# def con(str1,str2): 
#     concatenated=str1+str2 
#     return concatenated 

# string= input("Enter String1: ")
# string1= input("Enter string2: ") 
# result=con(string,string1) 
# print("Concatenated string are : "+result)

# class Employee:
# 	def __init__(self, id, name):
# 		self.id = id
# 		self.name = name
# 	def dispData(self):
# 		print("ID of the Employee: ",self.id)
# 		print("Name of the Employee: ",self.name)
	
# id = int(input("Enter the ID: "))
# name = input("Enter the name: ")
# employee = Employee(id, name)
# employee.dispData()

# class Fibonacci:
#     def __init__(self, num):
#         self.n = num
#     def calculate(self):
#         a = 0
#         b = 1
#         i = 0
#         while i<self.n:
#             print(a)
#             c = a + b
#             a = b
#             b = c
#             i +=1