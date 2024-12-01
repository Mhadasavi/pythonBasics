# percentage = 85.27
# print("{:.2f}%".format(percentage))
import keyword
from colorsys import yiq_to_rgb
from tokenize import String

# variables
# a = 50
# b = a
# print(id(a))
# print(id(b))
# a = 51
# print(id(a))

# local variable
# def test():
#     a = 10
#     print(a)

# print(a)
# test()

# global variable
# x = 100
# def test_global_variable():
#     global x
#     x = 'hi'
#     print(x)
#
# test_global_variable()
# print(x)

# data types

# a = 5
# b = 10.0
# c = 'h'
# d = "h"
# e = True
# f = 2+2j
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(isinstance(a, str))

# print(keyword.kwlist)
# help("keywords")

# import random
# numbers = [ ]
# for val in range(0, 11):
#     numbers.append( random.randint( 0, 11 ) )
# for num in range( 0, 11 ):
#     for i in numbers:
#         if num == i:
#             print( num, end = " " )

# while 1:
#     print("Hello")

#  the sum of squares of the first 15 natural numbers using a while loop.
# i=1
# sum_of_square=0
# while i < 5:
#     sum_of_square += i**2
#     i+=1
# print(sum_of_square)

# list_ = [3, 5, 1, 4, 6]
# list.pop()

# print('what\'s')
# print("what \"is\" this")
# print('''what's "is" this''')
# print('\\')
# print('\a')

# set
# set1 = {}
# set1 = {1, 2, (1,1)}
# print(type(set1))
# print(set1)

# set1 = {1, 2,  (3,4)}
# # Convert the set to a list
# list1 = list(set1)
#
# # Access the nested tuple (assuming you know its position)
# # In this case, let's find the tuple in the set
# nested_tuple = next(item for item in list1 if isinstance(item, tuple))
#
# print(nested_tuple)

# # Create a frozen set
# frozen_set1 = frozenset([1, 2, 3, 4])
# frozen_set2 = frozenset([1, 2, 3, 4, 5, 6])
#
# # Attempt to add an element (this will raise an error)
# # frozen_set.add(5)  # Uncommenting this line will cause an AttributeError
#
# # Use in a set operation
# another_set = {3, 4, 5}
# intersection = frozen_set1 & another_set
#
# print("Frozen Set 1:", frozen_set1)
# print("Intersection:", intersection)
# print(frozen_set1.union(frozen_set2, intersection))

# # Define two sets
# set_a = {1, 2}
# set_b = {1, 2, 3}
#
# # Check subset and superset
# is_subset = set_a.issubset(set_b)        # True
# is_proper_subset = set_a < set_b         # True
# is_superset = set_b.issuperset(set_a)    # True
# is_proper_superset = set_b > set_a       # True
#
# print("Set A:", set_a)
# print("Set B:", set_b)
# print("Is A a subset of B?", is_subset)
# print("Is A a proper subset of B?", is_proper_subset)
# print("Is B a superset of A?", is_superset)
# print("Is B a proper superset of A?", is_proper_superset)

# dict1 = {"Name":'John', (1,2):[1,2,3]}
# # print(dict1.popitem())
# for key in dict1:
#     print(key)
# for key in dict1:
#     print(dict1[key])
# for value in dict1.values():
#     print(value)
# for item in dict1.items():
#     print(item)

# Name
# (1, 2)
# John
# [1, 2, 3]
# John
# [1, 2, 3]
# ('Name', 'John')
# ((1, 2), [1, 2, 3])

# default constructor in python
# class student:
#     name = 'Upkar'
#     roll_no = 66
#
#     def show(self):
#         return self.name + str(self.roll_no)
#
# student_obj = student()
# print(student_obj.show())

class Example:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_string(cls, value_str):
        return cls(int(value_str))

    @classmethod
    def default(cls):
        return cls(0)

obj1 = Example(10)               # Using the standard constructor
obj2 = Example.from_string("20") # Using a class method
obj3 = Example.default()         # Another class method
print(obj1.value, obj2.value, obj3.value)  # Output: 10, 20, 0
print(obj1.__doc__)
print(obj1.__dict__)
print(obj1.__module__)
# print(obj1.__name__)
# print(obj1.__bases__)
