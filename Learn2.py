
# # Login page format
# email = input('Write your email: ')

# if '@' in email:
#         password = input('write your password for login: ')

#         if email == 'abhi123@yahoo.com' and password == '1234':
#             print('Access guaranted')
#         elif email == 'abhi123@yahoo.com' and password != '1234':
#             print('Access Denied')
#             password = input('write your password again for login: ')
#             if password == '1234':
#                 print('login successful')
#             else:
#                 print('Login Failed')
#         else:
#             print('Try after some time')
# else:
#     print('Email is invalid, write it again')
    
# # Print any table by given number by using loop.   
# number = int(input("write your number: "))

# i = 1

# while i < 11:
#     print(number * i)
#     i +=1
  
# # Write a program where you'll generate the random numbers and you'll ask input to the user through guesses and when user will guess the write
# # number you'll say you did it along with the number of attempts which he took. 

# import random

# jackpot = random.randint(1,100)

# Guess = int(input("Enter your guess number: "))
# counter = 1 

# while Guess != jackpot:
#     if Guess < jackpot:
#         print('Guess Higher')
#     else:
#         print("Guess Lower")

#     Guess = int(input("Enter your guess number: "))
#     counter += 1
    
# print("You did rihgt guess. But you took",counter,'attempts')

# # For loop use.
# row = int(input('Write any number: '))

# for i in range(1,row + 1):
#     for j in range(0,i):
#         print('*',end=' ')
#     print('')
    
# # Math

# import math as mp

# mp.factorial(5)

# # Random

# import random 

# random.randint(1,50)

# a = [1,2,3,4,5,6]

# random.shuffle(a)
# print(a)

# # Write a program were you have to capitalize every first word of the given string without using title operation on that.

# sample = 'hey, how are you.?'

# print(sample.split())
# x = []

# for i in sample.split():
#     print(i.capitalize())
#     x.append(i.capitalize())
    
# print(x)
# print(' '.join(x))

# # Write a programe to get the email before the @.?

# email = 'abc@yahoo.com'

# print(email[:email.find('@')])

# # Write a programe to filter only distinct values from the given list.?

# l1 = [1,1,2,3,3,4,5,5]

# l = []

# for i in l1:
#     if i not in l:
#         l.append(i)
# print(l)

# def f():
#     print('inside f')
#     def g():
#         print('inside g')
#     g()
    
# f()


# # Write a program to check the given string is a palindrom or not.?
# def palindrom(text):
#     if len(text) <= 1:
#         print('palindrom')
#     else:
#         if text[0] == text[-1]:
#             palindrom(text[1:-1])
#         else:
#             print('Not palindrom')
            
# palindrom('madam')
# palindrom('nitin')
# palindrom('porsche')

# #if 2 new born rabbits are put in a pen, how many rabbits will be in the pen after a year and assume that rabbit produe one male and one female 
# # offspring, can reprodue once every month, can reproduce once they are one month old, will never die.!!!

# def fib(m):
#     if m == 0 or m == 1:
#         return 1
#     else:
#         return fib(m-1) + fib(m-2)
    
# print(fib(500)) # this will take time in excution so will write a new program that will take less time by using memoisation.

# def memo(m,d):
    
#     if m in d:
#         return d[m]
#     else:
#         d[m] = memo(m-1,d) + memo(m-2,d)
#         return d[m]
# d = {0:1,1:1}
# print(memo(50,d))

# # Lambda Function.
# a = lambda x: x ** 2
# a(5)

# a = lambda x,y : x + y
# a(2,4)

# # Map, Reduce, Filter
# # Oop

# class ATM:
    
#     def __init__(self):
#         self.pin = ""
#         self.balance = 0
        
#         self.menu()
#     def menu(self):
#         user_input = input("""
#                            Hello, How would you like to proceed.?
#                            1.Enter 1 to Create Pin
#                            2.Enter 2 to Deposit
#                            3.Enter 3 to Withdraw
#                            4.Enter 4 to Check Balance
#                            5.Enter 5 to Exit
#                            """)
#         if user_input == '1':
#             self.create_pin()
#         elif user_input == '2':
#             self.deposit()
#         elif user_input == '3':
#             self.withdraw()
#         elif user_input == '4':
#             self.check_balance()
#         else:
#             print('Thanks for using the services')
    
#     def create_pin(self):
#         self.pin = input('Enter your pin')
#         print('pin set successfully')
        
#     def deposit(self):
#         temp = input('Enter your pin')
#         if temp == self.pin:
#             amount = int(input('Enter the amount'))
#             self.balance = self.balance + amount
#             print('Deposit Successful')
#         else:
#             print('Invalid Pin')
            
#     def withdraw(self):
        
#         temp = input('Enter your pin')
#         if temp == self.pin:
#             amount = int(input('Enter the amount'))
#             if amount < self.balance:
#                 self.balance = self.balance - amount
#                 print('Operstion Successful')
#             else:
#                 print('Insufficient Funds')
#         else:
#             print('Invalid Pin')
            
#     def check_balance(self):
#         temp = input('Enter your Pin')
#         if temp == self.pin:
#             print(self.balance)
#         else:
#             print('Invalid Pin')
            
            
# sbi = ATM()
# sbi.deposit()

# # Fractions...........

# class fraction:
#     def __init__(self,n,d):
#         self.num = n
#         self.den = d
        
# x= fraction(2,4)
# type(x)
    
# # What is the data type of True in Python?
# a = True
# type(a)

# # Create a variable storing your age and print its type.
# age = 24
# type(age)

# # Convert string "25" to integer.
# str = "25"
# convert = int(str)
# print(convert)

# # What is the output of: print(type(5.0))?
# print(type(5.0))


# # Write a program to swap two variables.
# x = 5
# y = 10

# x,y = y,x
# print(x,y)

# # What are Python keywords? Give 3 examples.
# # Ans - Python keyword are predifined meaning and funcationality within the language and e.g, if, else, True,False.

# # Check if a number is even or odd using if-else.
# ask = input('Write your number')
# if ask % 2 == 0:
#     print('Number is even')
# else:
#     print('Number is Odd')
    
# # What is the difference between == and =?
# # The single eualto (=)  is used to asign a value in the variable in pyhton, however the double equal too used to compare the two value that both are
# # - equal or not..

# # Write a while loop to print numbers 1 to 10.
# for i in range(1,11):
#     print(i)
    
# # Write a for loop to print all elements in a list.
# fruits = ["apple", "banana", "cherry", "date"]
# for frauit in fruits:
#     print(frauit)
    
# # What is a literal? Give an example.
# # Literal are fixed values in out code, they dosen't change during the code execution.
# age = 23
# hight = 5.8
# pi = 3.4
# complex_num = 2j + 3

# print(age,hight,pi,complex_num)

# # Convert integer 10 to float.
# num = 10
# flt = float(num)
# print(flt)

# # What is the output: 3 + 2 * 5?
# solve = 3 + 2 * 5
# print(solve)

# # Write a program to find the largest of 3 numbers.
# num1 = int(input('Give me your input: '))
# num2 = int(input('Give me your input: '))
# num3 = int(input('Give me your input: '))
# largest = max(num1,num2,num3)
# print(f"The largest num is:{largest}")

# # What does break do in a loop?
# # Ans - Break will end our code when the givrn conditon will met. 

# # What does continue do?
# # Ans - Continue will skip the loop on the given condition and then will continue till the end on of the loop.

# # What does pass do?
# # Ans - Pass do nothing, we use pass to skip the error when we want to run the incomplete code and we wanted to add remaning code later.

# # Print first 5 multiples of 3 using loop.
# for i in range(1,6):
#     print(i * 3)
    
# # What is a nested loop? Give example.
# # Ans - Nested loop means loop inside a loop.

# for i in range(1,4):
#     for j in range(1,4):
#         print(f'{i} * {j} = {i * j}')

# # Write a program to print a multiplication table of 5.
# num = int(input('Enter the number: '))
 
# i = 1
 
# while i < 11:
#     print(f"{num} × {i} = {num * i}")
#     i += 1

# # What is a string in Python?
# # Ans - String ia a data type in python and has sequence of characters which is wrapped in "", which is immutalble.

# # Access the first character of a string.



# # Pass by referance..
# class customer:
    
#     def __init__(self,name,gender,address):
#         self.name = name
#         self.gender = gender
#         self.address = address
#     def edit_profile(self,new_name,new_city,new_pincode,new_state):
#         self.name = new_name
#         self.address.change_address(new_city,new_pincode,new_state)
    
# class address:
#     def __init__(self,city,pincode,state):
#         self.city = city
#         self.pincode = pincode
#         self.state = state
#     def change_address(self,new_city,new_pincode,new_state):
#         self.city = new_city
#         self.pincode = new_pincode
#         self.state = new_state
        
# add = address('Ballia',277403,'U.P')
# cust = customer('Rohit','Male',add)

# cust.edit_profile('Rahul','Pune',444402,'Maharastra')
# print(cust.address.state)

# # Inheritance in python..
# class user:   #-------- Parent Class, this can not fatch the values from child class.
    
#     def login(self):
#         print('Login')
        
#     def register(self):
#         print('Register')
        
# class student(user):      #--------- Child class which can access all the details from the parent. 
    
#     def enroll(self):
#         print('Enroll')
    
#     def review(self):
#         print('Review')
        
# stu1 = student()
# stu1.enroll()
# stu1.login()
# stu1.register()
# stu1.review()

# #E.g.--
# class phone:
    
#     def __init__(self,price,brand,camera):
#         print('Inside phone constructer')
#         self.price = price
#         self.brand = brand
#         self.camera = camera

# class smartphone(phone):
#     pass

# s = smartphone(20000,'Apple',13)
# print(s.camera)

# # E.g. 2 Inheriting private member.
# class phone:
    
#     def __init__(self,price,brand,camera):
#         print('Inside phone constructer')
#         self.price = price
#         self.__brand = brand
#         self.camera = camera

# class smartphone(phone):
#     pass

# s = smartphone(20000,'Apple',13)
# print(s.camera)

# # E.g.3 - Method over riding example.
# class phone:
#     def __init__(self,price,brand,camera):
#         print("inside  phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
        
#     def buy(self):
#         print('Buying a camera')
        
# class smartphone(phone):
#     def buy(self):
#         print('Buying a smartphone')
        
# s = smartphone(2000,'Apple',13)
# s.buy()

# # E.g.4 - Polymorphism.
# class parent:
    
#     def __init__(self,num):
#         self.__num = num
        
#     def get_num(self):
#         return self.__num

# class child(parent):
    
#     def show(self):
#         print('This is in child class')
        
# son = child(100)
# print(son.get_num)
# son.show()

# # E.g.5 - Polymorphism.
# class parent:
#     def __init__(self,num):
#         self.__num = num
        
#     def get_num(self):
#         return self.__num
    
# class child(parent):      # i'll get error here coz we have the value on the child so that'll not triger into the parent one and we are calling
#                         # to the parrent constructer which is .__num() which has no value.
#     def __init__(self,val,num):  
#         self.__val = val
        
#     def get_val(self):
#         return self.__val

# son = child(100,10)
# print("Parent:Num:",son.get_num())
# print("Child:Val:",son.get_val())

# # Use of Super() Keyword.
# class phone:
    
#     def __init__(self,price,brand,camera):
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
        
#     def buy(self):
#         print('Buying a phone')
        
# class smartphone(phone):
    
#     def buy(self):
#         print('Buying a smartphone')
#         super().buy()
        
# s = smartphone(23000,'Sony',13)
# s.buy()

# # E.g.2(Super_Keyword())
# class phone:
    
#     def __init__(self,price,brand,camera):
#         print('Inside phone constructor')
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
        
# class smartphone(phone):
    
#     def __init__(self, price, brand, camera,os,ram):
#         super().__init__(price, brand, camera)
#         self.os = os
#         self.ram = ram
#         print('Inside smartphone constructor')
        
# s = smartphone(23500,'samsung',12,'Android',2)
# print(s.os)
# print(s.brand)

# # E.g.3(Super_Keyword())
# class parent:
    
#     def __init__(self,num):
#         self.__num = num
        
#     def get_num(self):
#         return self.__num
    
# class child(parent):
    
#     def __init__(self,num,val):
#         super().__init__(num)
#         self.__val = val
        
#     def get_val(self):
#         return self.__val
    
# son = child(100, 200)
# print(son.get_num())
# print(son.get_val())

# # Type of Inheritance.
# # 1. Singlw Level, 2. Multiple Level, 3. Hierachiel Level, 4. Multiple Level

# # Multilevel Inheritance
# class product:
#     def review(self):
#         print('Product customer review')
        
# class phone(product):
#     def __init__(self,price,brand,camera):
#         print('Inside phone constructor')
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
        
#     def buy(self):
#         print('Buying a phone')
        
# class smartphone(phone):
#     pass

# s = smartphone(20000,'Apple',12)
# p = phone(1999,'Samsung',11)

# s.buy()
# s.review()
# p.review()

# # Hierachiel Level...
# class phone:
    
#     def __init__(self,price,brand,camera):
#         print('Inside phone constructor')
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
        
#     def buy(self):
#         print('Buying a phone')
        
# class product:
    
#     def review(self):
#         print('customer review')
        
# class smartphone(phone,product):
#     pass

# s = smartphone(20000,'Apple',12)
# s.buy()
# s.review()

# # Multiple Level...
# class a:
    
#     def m1(self):
#         return 20
    
# class b(a):
    
#     def m1(self):
#         return 30
    
#     def m2(self):
#         return 40
    
# class c(b):
    
#     def m2(self):
#         return 20
    
# obj1 = a()
# obj2 = b()
# obj3 = c()
# print(obj1.m1() + obj3.m1() + obj3.m2())
