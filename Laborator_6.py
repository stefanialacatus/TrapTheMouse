#exercitiul 1
import math

class Shape:
    def __init__(self, color):
        self.color=color

    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, color, r):
        super().__init__(color)
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def perimeter(self):
        return 2 * 3.14 * self.r
    
class Rectangle(Shape):
    def __init__(self, color, l, L):
        super().__init__(color)
        self.l = l
        self.L = L

    def area(self):
        return self.l * self.L

    def perimeter(self):
        return 2 * (self.l + self.L)
    
class Square(Shape):
    def __init__(self, color, l):
        super().__init__(color)
        self.l = l

    def area(self):
        return self.l * self.l

    def perimeter(self):
        return 4 * self.l

class Triangle(Shape):
    def __init__(self, color, a, b, c):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a+self.b+self.c

print("Exercitiul 1:")
triunghi1 = Triangle("red", 10, 11, 12)
circle1 = Circle("blue", 5)
print(f"Aria triunghiului este {triunghi1.area()}")
print(f"Perimetrul cercului este {circle1.perimeter()}")
print()

#exercitiul 2
class Account:
    def __init__(self, iban, owner, amount):
        self.iban = iban
        self.owner = owner
        self.amount = amount

    def __str__(self):
        return "IBAN: " + self.iban + ", Owner: " + self.owner + ", Amount: " + str(self.amount)

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        if self.amount < amount:
            print("Insufficient funds")
        else:
            self.amount -= amount

    def transfer(self, account, amount):
        if self.amount < amount:
            print("Insufficient funds")
        else:
            self.amount -= amount
            account.amount += amount

class SavingsAccount(Account):
    def __init__(self, iban, owner, amount, interest):
        super().__init__(iban, owner, amount)
        self.interest = interest

    def add_interest(self):
        self.amount += self.amount * self.interest
    
    def deposit(self, amount):
        self.amount += amount
        self.add_interest()
    
    def withdraw(self, amount):
        if self.amount < amount:
            print("Insufficient funds")
        else:
            self.amount -= amount
            self.add_interest()

class CheckingAccount(Account):
    def __init__(self, iban, owner, amount, fee):
        super().__init__(iban, owner, amount)
        self.fee = fee

    def withdraw(self, amount):
        if self.amount < amount + self.fee:
            print("Insufficient funds")
        else:
            self.amount -= amount + self.fee

    def deposit(self, amount):
        self.amount += amount

    def transfer(self, account, amount):
        if self.amount < amount + self.fee:
            print("Insufficient funds")
        else:
            self.amount -= amount + self.fee
            account.amount += amount
print()    
svng = SavingsAccount("RO123", "John Doe", 100, 0.1)
acc1 = CheckingAccount("RO124", "Amalia", 200, 10)
print("Exercitiul 2:")
print(svng)
print(acc1)
svng.deposit(100)
acc1.withdraw(50)
print("Inainte de transfer:")
print(svng)
print(acc1)
svng.transfer(acc1, 150)
print("Dupa transfer:")
print(svng)
print(acc1)
print()

#exercitiul 3
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return "Brand: " + self.brand + ", Model: " + self.model + ", Year: " + str(self.year)
    
class Car(Vehicle):
    def __init__(self, brand, model, year, fuel):
        super().__init__(brand, model, year)
        self.fuel = fuel

    def __str__(self):
        return super().__str__()
    
    def mileage(self, km):
        return km / self.fuel
    
    def towing_capacity(self):
        return 100
    
    def refuel(self, fuel):
        self.fuel += fuel

    def drive(self, distance):
        fuel_needed = distance / 15
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            return f"Drove {distance} km. Remaining fuel: {self.fuel} liters"
        else:
            return "Not enough fuel."
        
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, fuel):
        super().__init__(brand, model, year)
        self.fuel = fuel

    def __str__(self):
        return super().__str__() + ", Fuel: " + self.fuel
    
    def mileage(self, km):
        return km / self.fuel
    
    def refuel(self, fuel):
        self.fuel += fuel

    def ride(self, distance):
        fuel_needed = distance / 10
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            return f"Rode {distance} km. Remaining fuel: {self.fuel} liters"
        else:
            return "Not enough fuel."
        
class Truck(Vehicle):
    def __init__(self, brand, model, year, fuel, capacity):
        super().__init__(brand, model, year)
        self.fuel = fuel
        self.capacity = capacity

    def __str__(self):
        return super().__str__() + ", Fuel: " + self.fuel + ", Capacity: " + self.capacity
    
    def mileage(self, km):
        return km / self.fuel
    
    def towing_capacity(self):
        return self.capacity
    
    def refuel(self, fuel):
        self.fuel += fuel

    def drive(self, distance):
        fuel_needed = distance / 20
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            return f"Drove {distance} km. Remaining fuel: {self.fuel} liters"
        else:
            return "Not enough fuel."

print()        
car = Car("Audi", "A4", 2019, 5)
motorcycle = Motorcycle("Yamaha", "R1", 2020, 3)
truck = Truck("Volvo", "FH16", 2018, 10, 5000)
print("Exercitiul 3:")
print(car)
print(car.mileage(100))
print(car.drive(100))
print()

#exercitiul 4
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return "Name: " + self.name + ", Salary: " + str(self.salary)
    
class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.ActiveEmployees = []
        self.PastEmployees = []

    def __str__(self):
        return super().__str__()
    
    def income(self):
        return self.salary
    
    def employ(self, employee):
        self.ActiveEmployees.append(employee)

    def fire(self, employee):
        self.ActiveEmployees.remove(employee)
        self.PastEmployees.append(employee)

    def showEmployees(self):
        print("Active employees:")
        for employee in self.ActiveEmployees:
            print(employee)
        print("Past employees:")
        for employee in self.PastEmployees:
            print(employee)

class Engineer(Employee):
    def __init__(self, name, salary, skills):
        super().__init__(name, salary)
        self.projects = []
        self.skills = skills

    def __str__(self):
        return super().__str__() + ", Skills: " + str(self.skills)
    
    def income(self):
        return self.salary + len(self.skills) * 100
    
    def addSkill(self, skill):
        self.skills.append(skill)

    def startProject(self, project):
        self.projects.append(project)

    def showProjects(self):
        for project in self.projects:
            print(project)
    
    def finishProject(self, project):
        self.projects.remove(project)


class SalesPerson(Employee):
    def __init__(self, name, salary, sales):
        super().__init__(name, salary)
        self.sales = sales

    def __str__(self):
        return super().__str__()
    
    def income(self):
        return self.salary + self.sales * 0.1
    
    def makeSale(self, sale):
        self.sales += sale
    
    def showSales(self):
        return self.sales
    
print()
engineer1 = Engineer("Dave", 5000, ["Python", "Java"])
engineer1.startProject("Project 1")
engineer1.startProject("Project 2")
print("Exercitiul 4:")
print(engineer1)
engineer1.addSkill("C++")
print("Dave's projects: ")
engineer1.showProjects()
engineer1.finishProject("Project 1")
engineer1.showProjects()
manager = Manager("John", 10000)
print(manager)
sale_person = SalesPerson("Alice", 3000, 57)
print(sale_person)
manager.employ(sale_person)
manager.employ(engineer1)
manager.showEmployees()
print("Employees after firing:")
manager.fire(engineer1)
manager.showEmployees()
sale_person.makeSale(10)
print("Alice salary: %d" %sale_person.income())
print()

#exercitiul 5
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name: " + self.name + ", Age: " + str(self.age)
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"
    
class Bird(Animal):
    def __init__(self, name, age, size, wingspan):
        super().__init__(name, age)
        self.size = size
        self.wingspan = wingspan

    def __str__(self):
        return super().__str__() + ", Size: " + self.size + ", Wingspan: " + self.wingspan
    
    def fly(self):
        return f"{self.name} is flying"
    
    def sing(self):
        return f"{self.name} is singing"
    
    def maxHeight(self):
        wingspan = float(self.wingspan)
        return f"{self.name} can fly as high as {5000 + wingspan * 1000} metres."

class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return super().__str__()
    
    def run(self):
        return f"{self.name} is running"
    
    def swim(self):
        return f"{self.name} is swimming"
    
class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age)
        self.water_type = water_type

    def __str__(self):
        return super().__str__() + ", Water type: " + self.water_type
    
    def swim(self):
        return f"{self.name} is swimming"
    
print()
vulture = Bird("Vulture", 5, "medium", "2")
leopard = Mammal("Leopard", 10)
shark = Fish("Shark", 3, "saltwater")
print("Exercitiul 5:")
print(vulture)
print(vulture.fly())
print(vulture.sing())
print(vulture.maxHeight())
print()
print(leopard)
print(leopard.eat())
print(leopard.run())
print(leopard.sleep())
print()
print(shark)
print(shark.swim())
print()
    
#exercitiul 6
class LibraryItem:
    def __init__(self, title, creator, publication_year):
        self.title = title
        self.creator = creator 
        self.publication_year = publication_year
        self.is_checked_out = False
        self.score = 0
    
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            self.score += 1
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."


    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} wasn't checked out."

    def getPopularity(self):
        if(self.score < 1):
            return "Not popular"
        elif(self.score < 3 and self.score >= 2):
            return "Medium popularity"
        elif(self.score >= 3):
            return "Very popular"

    def display_info(self):
        return f"Title: {self.title}, Creator: {self.creator}, Year: {self.publication_year}, Popularity: {self.getPopularity()}"


class Book(LibraryItem):
    def __init__(self, title, author, publication_year, pages, genre):
        super().__init__(title, author, publication_year)
        self.pages = pages
        self.genre = genre
    
    def display_info(self):
        return f"{super().display_info()}, Genre: {self.genre}, Number of pages: {self.pages}, Popularity: {self.getPopularity()}"


class DVD(LibraryItem):
    def __init__(self, title, director, publication_year, duration, genre):
        super().__init__(title, director, publication_year)
        self.duration = duration
        self.genre = genre
    
    def display_info(self):
        return f"{super().display_info()}, Duration: {self.duration} minutes, Genre: {self.genre}, Popularity: {self.getPopularity()}"


class Magazine(LibraryItem):
    def __init__(self, title, publisher, publication_year, issue_number, category):
        super().__init__(title, publisher, publication_year)
        self.issue_number = issue_number
        self.category = category
    
    def display_info(self):
        return f"{super().display_info()}, Category: {self.category}, Issue Number: {self.issue_number}, Popularity: {self.getPopularity()}"

print()
book = Book("Harry Potter", "J.K. Rowling", 1997, 500, "Fiction/Fantasy")
dvd = DVD("Inception", "Christopher Nolan", 2010, 150, "Sci-Fi")
magazine = Magazine("National Geographic", "National Geographic Society", 1888, 1, "Science")
print("Exercitiul 6:")
book.check_out()
book.return_item()
book.check_out()
book.return_item()
print(book.display_info())
print(book.check_out())
print(book.check_out())
print(book.return_item())
print()
dvd.check_out()
dvd.return_item()
dvd.check_out()
dvd.return_item()
dvd.check_out()
dvd.return_item()
print(dvd.display_info())
print(dvd.check_out())
print(dvd.return_item())
print()
print(magazine.display_info())
print(magazine.check_out())
print(magazine.return_item())
print()