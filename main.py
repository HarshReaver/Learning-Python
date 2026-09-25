"""salary=int(input("Enter your salary: "))
if(salary<30000):
    print("5% tax")
elif(salary>=30000 and salary<=70000):
    print("15% tax")
else:
    print("25% tax")"""

""" number1=int(input("Enter a number1: "))
number2=int(input("Enter a number2: "))
for i in range(number1,number2+1):
    if(i%2==0):
        print(i)     """

""" def function1(n):
    for number in str(n):
        print(number)
number=int(input("Enter a number: "))
print(function1(number)) """

"""def count_function(n):
    count=0
    sum=0
    while(n>0):
        sum=sum+n%10
        n=n//10
    return sum  
number=int(input("Enter a number: "))
print(count_function(number))   """

"""def multiples(n):
    for i in range(1,n+1):
        if(i%3==0 and i%5==0):
            print(i)
number=int(input("Enter a number: "))
print(multiples(number))"""

"""while(True):
    user_input=(input("Enter a number: "))
    if(user_input=="quit" or user_input=="QUIT" or user_input=="Quit"):
        break   
    number=float(user_input)
    if(number>0):
        print("Positive")
    elif(number<0):
        print("Negative")
    else:
        print("Zero")"""

"""def calculator(a,b,operation):
    if(operation=="+"):
        return a+b
    elif(operation=="-"):
        return a-b
    elif(operation=="*"):
        return a*b
    elif(operation=="/"):
        if b != 0:
            return a/b
        else:
            return "Error: Division by zero is not allowed."
number1=float(input("Enter a number1: "))
number2=float(input("Enter a number2: "))
operation=input("Enter an operation (+, -, *, /): ")
print(calculator(number1,number2,operation))"""

"""def prime(n):
    if(n<=1):
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True
number=int(input("Enter a number: "))
if(prime(number)):
    print("Prime")
else: print("Not Prime")"""

"""s="Python"
print(s[0:2])
print(s[2:])
print(s[:3])
print(s[::2])
print(s[::-1])"""

""" name = "Rahul" 
age = 25 
text = "My name is {1} and I am {0} years old".format(name, age) 
print(text) """

""" a=3
b=5
print(f"The sum of {a} and {b} is {(a+b)}/2") """

""" nums=[1,2,3,4,5]
nums.insert(1,10)
print(nums) """

""" t=(1,2,3,4,5)
sum=0
for val in t:
    sum+=val
print(sum)   """

# Assignment 3
""" def palindrome(s):
    s=s.replace(" ","").lower()
    return s==s[::-1]
string=input("Enter a string: ")
if(palindrome(string)):
    print("Palindrome")
else:  print("Not Palindrome") """

""" def average(list):
    sum=0
    for val in list:
        sum+=val
    return sum/len(list)
list=[1,2,3,4,5]
print (average(list)) """

""" list1 = [
    int(x) for x in input("Enter a list of numbers separated by commas: ").split(",")
]
list2 = [
    int(x) for x in input("Enter another list of numbers separated by commas: ").split(",")
]
mergedlist = sorted(list1 + list2)
print(mergedlist) """

""" tuple1 = tuple(
    int(x) for x in input("Enter a tuple of numbers separated by commas: ").split(",")
)
tuple2 = tuple(everyvalue for everyvalue in tuple1 if everyvalue % 2 == 0)
print(tuple2) """

""" dictionary1={} 

print("A-add student \nB-update student \nC-Search for a student \nD- Display all students and marks")
Input=input("Enter your choice:")
if(Input=="A" or Input=="a"):
    name=input("Enter student name: ")
    marks=float(input("Enter marks: "))
    print("Added marks")
    dictionary1[name]=marks
elif(Input=="B" or Input=="b"):
    name=input("Enter student name: ")
    marks=float(input("Enter new marks: "))
    print("Updated marks")
    dictionary1[name]=marks
elif(Input=="C" or Input=="c"):
    name=input("Enter student name: ")
    print("Get marks")
    if(name not in dictionary1):
        print("Student not found")
    else : print(dictionary1.get(name, "Student found"))
elif(Input=="D" or Input=="d"):
    print("Display all students")
    for name,marks in dictionary1.items():
        print(f"{name}: {marks}")  
else:
    print("Invalid choice") """

""" words =["apple","banana","kiwi","cherry","mango"]
dictionary1={}
for word in words:
    dictionary1={word:len(word) for word in words}
print(dictionary1) """

""" s=input("Enter a string\n")
print("string_count",s.count(" ")) """

""" list1 =[1,2,3,4] 
list2 =[4,6,7,8]
if(set(list1) & set(list2)):
    print("Lists have common elements")
else: print("Lists don't have common elements") """

""" string1=input("Enter a string: ")
unique=set(string1)
print("Unique characters:", unique)
print("Number of unique characters:", len(unique))
 """

""" lst = [1,2,3,2,4,5,3,6]
seen = set()
duplicates = set()
for x in lst:
    if x in seen:
        duplicates.add(x)
    else:
        seen.add(x)
print("Repeated elements:", duplicates) """

#Assignment 4
""" class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number=account_number
        self.owner_name=owner_name
        self.balance=balance
    def check_balance(self): #getter method
        return self.balance
    def deposit(self, amount): #setter method
        if amount>0:
            self.balance+=amount
            print(f"Deposited Rupees {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount): #setter method
        if amount>0:
            if amount<=self.balance:
                self.balance-=amount
                print(f"Withdrew Rupees {amount}. New balance: {self.balance}")
            else :
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")     
account=BankAccount("123456789","Rahul",1000)
print("Current balance:", account.check_balance())
account.deposit(int(input("Enter amount to deposit:")))
withdraw_amount = int(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount) """

""" class Book:
    def __init__(self, title, author, list_of_reviews):
        self.title=title
        self.author=author
        self.list_of_reviews=list_of_reviews
    def add_review(self, review):
        self.list_of_reviews.append(review)
    def count_reviews(self):
        return len(self.list_of_reviews)
    def display_reviews(self):
        print(f"\nReviews for '{self.title}' by {self.author}:")
        for review in self.list_of_reviews:
            print(f"\n- {review}")
title=input("Enter book title: ")
author=input("Enter book author: ")
book=Book(title, author, [])
print("\nChoose option:")
print("1 - Add a book review")
print("2 - Count total reviews")
print("3 - Display all reviews")
print("4 - Exit")
while True:
    choice = input("Enter your choice: ")
    if choice == "1":
        review = input("Enter review: ")
        book.add_review(review)
    elif choice == "2":
        print("Total reviews:", book.count_reviews())
    elif choice == "3":
        book.display_reviews()
    elif choice == "4":
        break
    else:
        print("Invalid option") """
        
""" class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks
    def get_name(self):
        return self.__name
    def get_roll_no(self):
        return self.__roll_no
    def get_marks(self):
        return self.__marks
    def set_name(self, name):
        if name.strip() == "":
            print("Name cannot be empty")
        else: self.__name = name
    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self.__roll_no = roll_no
        else: print("Roll number must be between 1 and 100")
    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else: print("Marks cannot be negative")
s1 = Student("Rahul", 20, 80)
print(s1.get_marks())
s1.set_marks(-9)
print(s1.get_marks()) """

""" class Shape:
    def area(self):
        print("Area method should be overridden")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

option= int(input("Choose an option \n1.Area of Circle \n2.Area of Rectangle \n3.Area of Triangle \n"))
if(option==1):
    radius=input("Enter a radius :")
    circle=Circle(float(radius))
    print("Area of Circle:", circle.area())
elif(option==2):
    length=input("Enter a length :")
    width=input("Enter a width :")
    rectangle=Rectangle(float(length), float(width))
    print("Area of Rectangle:", rectangle.area())
elif(option==3):
    base=input("Enter a base :")
    height=input("Enter a height :")
    triangle=Triangle(float(base), float(height))
    print("Area of Triangle:", triangle.area()) """
    
""" class Vehicle:
    def __init__ (self,brand, model):
        self.brand=brand
        self.model=model
class Bike(Vehicle):
    def __init__(self,brand,model,engine_capacity):
        super().__init__(brand,model)
        self.engine_capacity=engine_capacity
class Car(Vehicle):
    def __init__(self,brand,model,seats):
        super().__init__(brand,model)
        self.seats=seats
car=Car("Toyota","Camry",5)
print("Car Details:", car.brand, car.model, car.seats)
bike=Bike("Honda","CBR",150)
print(f"Bike Details: {bike.brand} {bike.model} {bike.engine_capacity}cc") """
    
""" from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.monthly_salary
class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend
    def calculate_salary(self):
        return self.stipend
full_time_emp = FullTimeEmployee(50000)
part_time_emp = PartTimeEmployee(200, 80)
intern = Intern(15000)
print("Full Time Employee Salary:", full_time_emp.calculate_salary())
print("Part Time Employee Salary:", part_time_emp.calculate_salary())
print("Intern Salary:", intern.calculate_salary()) """

""" class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age if self.age is not None else 'N/A'}")
        print(f"Address: {self.address if self.address is not None else 'N/A'}")
person3 = Person("Vikram")
person1 = Person("Rahul", 25, "123 Main St")
person2 = Person("Anjali", 30)
person2.display_info() """

""" class Player:
    player_count=0
    def __init__(self, name, level):
        self.name=name
        self.level=level
        Player.player_count+=1
    def display_info(self):
        print(f"Player Name: {self.name}, Level: {self.level}")
player1=Player("Rahul", 5)
player2=Player("Anjali", 10)
print("Total Players:", Player.player_count)    
player1.display_info()
player2.display_info() """

""" class Herbivore:
    def herbi(self):
        print("Eating plants")
class Carnivore:
    def carni(self):
        print("Eating meat")
class Omnivore:
    def omni(self):
        print("Eating both plants and meat")
class Bear(Herbivore, Carnivore, Omnivore):
    def eat(self):
        print("Bear can eat everything")
b=Bear()
b.eat()
b.herbi()
b.carni()
b.omni() """

""" #Chat system has classes user, message & chatroom, implementing functions of sending message, viewing chat history, user joining and leaving the chatroom.
class User:
    def __init__(self, username):
        self.username = username
    def send(self, chatroom, text):
        message=Message(self.username, text)
        chatroom.add_message(message)
class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text   
class ChatRoom:
    def __init__(self):
        self.users = []
        self.messages = []
    def add_user(self, user):
        self.users.append(user)
        print(f"{user.username} joined the chatroom.")
    def remove_user(self, user):
        self.users.remove(user)
        print(f"{user.username} left the chatroom.")
    def add_message(self, message):
        self.messages.append(message)
    def view_chat_history(self):
        print("Chat History:")
        for message in self.messages:
            print(f"{message.sender}: {message.text}")
chatroom=ChatRoom()
user1=User("Rahul")
user2=User("Jay")
chatroom.add_user(user1)
chatroom.add_user(user2)
user1.send(chatroom, "Hi")
user2.send(chatroom, "Hello")
chatroom.view_chat_history()
chatroom.remove_user(user1)
chatroom.view_chat_history() """

#Assignment 5

""" with open("names.txt", "w+") as file:
    file.write(input("Enter five names separated by commas: "))
with open("names.txt", "r") as file:
    names = file.read().split(",")
    print("Names in the file:")
    for name in names:
        print(name.strip()) """
    
""" with open("log.txt", "a") as file:
    file.write(f"Program run successfully\n")
with open("log.txt", "r") as file:
    print(file.read()) """
    
""" list=[5,10,15,20,25]
new_list=[x for x in list if x>15]
print(new_list) """

""" import json

cities={
    "New York": 8000000,
    "Los Angeles": 4000000,
    "Chicago": 2700000
}
with open("cities.json", "w") as file:
    json.dump(cities, file)
with open("cities.json", "r") as file:
    data=json.load(file)
for city, population in data.items():
    print(f"{city}: {population}")
city_name=input("Enter a city name: ")
population=input("Enter population: ")
data[city_name]=population
with open("cities.json", "w") as file:
    json.dump(data, file) """
   
""" try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
finally:    print("Program execution completed.") """

