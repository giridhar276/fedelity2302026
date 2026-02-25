





# procedural programming
print("hello")



# object oriented programming
# every class contains methods

class Employee:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

    def displayDetails(self):
        print("Employee name :", self.name)
        print("Employee age  :",self.age)
        print("Employee city:", self.city)

# object creation
emp1 = Employee('rita',20,'Hyderabad')
emp1.displayDetails()

# object creation
emp2 = Employee('sita',21,'Bang')
emp2.displayDetails()

# object creation
emp3 = Employee('gita',22,'Chennai')
emp3.displayDetails()


