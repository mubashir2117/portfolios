# class points:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return points(self.x + other.x, self.y + other.y)
#     def __sub__(self, other1):
#         return points(self.x - other1.x, self.y - other1.y)
#     def __mul__(self, other2):
#         return points(self.x * other2.x, self.y * other2.y)
#     def __truediv__(self, other3):
#         return points(self.x / other3.x, self.y / other3.y)

#     def __str__(self):
#         return f"points({self.x}, {self.y})"
    
# p1 = points(5,6)
# p2 = points(1,3)
# p3 = p1 + p2
# p4 = p1 - p2
# p5 = p1 * p2
# p6 = p1 / p2
# print(p3)
# print(p4)
# print(p5)
# print(p6)








# class Example:
#     count = 0

#     def __init__(self):
#         Example.count += 1

#     @classmethod
#     def get_count(cls):
#         return cls.count

#     @staticmethod
#     def greet():
#         return "Hello"

# e1 = Example()
# e2 = Example()
# print(Example.get_count())  # Output: 2
# print(Example.greet())      # Output: Hello



# class Car:
#     wheels = 4  # Class attribute
#     doors = 2  # Class attribute


#     def __init__(self, color):
#         self.color = color  # Instance attribute

# car1 = Car("Red")
# print(car1.color)     # Output: Red
# print(Car.wheels)     # Output: 4
# print(Car.doors)     # Output: 4



# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         return "Bark"

# class Cat(Animal):
#     def make_sound(self):
#         return "meow"
# dog = Dog()
# cat = Cat()

# print(cat.make_sound())  # Output: meow
# print(dog.make_sound())  # Output: Bark




# class Father:
#     def skills(self):
#         return "Gardening"

# class Mother:
#     def skills(self):
#         return "Cooking"

# class Child( Mother, Father):
#     pass

# c = Child()
# print(c.skills())  # Output: Gardening (based on MRO)
# # print(c.skills())  # Output: Cooking (based on MRO)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

# p1 = Point(1, 2)
# p2 = Point(3, 4)
# result = p1 + p2
# print(result.x, result.y)  # Output: 4 6



# class A: pass
# class B(A): pass
# class C(A): pass
# class D(B, C): pass

# print(D.__mro__)
