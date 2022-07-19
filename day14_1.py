# dictionary comprehension = create dictionaries using an expression
# can replace for loops and certain lambda functions

# dictionary = { key: expression for (key, value) in iterable}

# temps_of_cities_F = {'New York': 32, 'Boston': 75, 'The Bahamas': 84, 'Haiti': 90}

# will be creating a separate dictionary but this time it will be in celius

# cities_temps_C = {key: () for (key, value) in temps_of_cities_F.items()}
# this is what it should look like and now add the values to convert
# F to C

# cities_temps_C = {key: round((value - 32) * (5 / 9)) for (key, value) in temps_of_cities_F.items()}
# print(cities_temps_C)

# the round will round the results from decimal to whole numbers
# with dictionary comprehension you can also add if conditionals

# we want to create a dictionary that have only sunny whether only

# weather = {'New York': "snowing", 'The Bahamas': "sunny", 'Haiti': "sunny", 'Cuba': " cloudy"}
# sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
# print(sunny_weather)

# using dictionary with if/else
# cities = {'New York': 32, 'Boston': 75, 'The Bahamas': 84, 'Haiti': 90}

# desc_cities = {key: ("warm" if value >= 40 else "cold") for (key,value) in cities.items()}
# print(desc_cities)

# ------------------------------------------------------------------------------------------------------------------------------------------------
# 61 zip function
# zip function will aggregate elements for two or more iterables (list, tuples, sets, etc.)
# create a zip object with paired elements stored in tuples for each element

# usernames = ["Dude", "Belly", "shoes"]
# passwords = ("chicken", "turkey", "food")
#
# users = zip(usernames, passwords)
# for i in users:
#     print(i)
# if you want to convert zip object to list
#users = list(zip(usernames, passwords))

