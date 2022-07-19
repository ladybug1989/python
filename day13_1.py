#  map()  applies a function to each item in an iterable (list, tuple)
# map(function, iterable)

# store = [("shirt", 100.80),
#          ("pants", 88.90),
#          ("shoes", 50.00),
#          ("dress", 72.50)
#          ]
# converting money to euros
# to_euros = lambda data: (data[0], data[1]*0.82)

# convert euros to usd
# to_dollars = lambda data: (data[0], data[1]/0.82)
#
# store_euros = list( map(to_euros,store))
# 2nd part when converting to dollars
# store_dollars = list( map(to_dollars, store))
#
# for i in store_euros:
#     print(i)

# 3rd part in converting euros into dollars
# for i in store_dollars:
#     print(i)
#################################################
# 57. filter function
# filter() creates a collection of elements from an iterable from which a function returns true
# filter( function, iterable)
# tuple of friends
# friends = [("Max", 24),
#            ("Stephanie", 15),
#            ("Ericka", 19),
#            ("Kendra", 16),
#            ("Rose", 26)
#            ]
# age = lambda data: data[1] >= 18
#
# persons_drink = list(filter(age, friends))
#
# for i in persons_drink:
#     print(i)
#########################################
#  58.  reduce () apply a function to an iterable and reduce it to a single cumulative value.
# performs function on first two elements and repeats process until 1 value remains
# reduce (function, iterable)

# import functools

# letters = ["B", "E", "R", "L", "I", "N"]
# word = functools.reduce(lambda x, y,: x + y, letters)
# print(word)

# factorial = [4, 3, 2, 1]
# result = functools.reduce(lambda x, y,: x * y, factorial)
# print(result)
###################################################
# 59. list comprehension
#  a way to create a new list with less syntax can
# mimic certain lambda functions, easier to read
# list = [expression for item in iterable]
# list =[expression for item in iterable if conditional ]
# list =[expression if/else for item iterable]

# function that counts numbers in squares
# squares = []
# for i in range(1, 11):
#     squares.append(i * i)
# print(squares)

# use the list comprehension
# squares = [i * i for i in range(1, 11)]
# print(squares)

# students = [100, 20, 90, 50, 67, 87, 86, 98, 55]
# filter all the students that passed by having 60 and above
# passed_students = list(filter(lambda x: x >= 60, students))
# list comprehension
# passed_students = [i for i in students if i >= 60]
#
# passed_students = [i if i >= 60 else "FAILED" for i in students]
#
# print(passed_students)

