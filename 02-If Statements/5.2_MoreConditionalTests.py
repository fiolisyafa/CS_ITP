#equality and inequality with strings
session = 'discrete structures'
print(session == 'discrete structures')
print(session != 'character building')

#using the .lower() function
place = 'New York'
print(place == 'new york')
print(place.lower() == 'new york')
print(place != 'Vegas')

#numerical tests
number = 9
print(number == 9)
print(number != 9)
print(number < 8)
print(number > 10)
print(number <= 11)
print(number >= 9)

#using and or
bus = '6M'
print(bus == '6M' or '9C')
stops = 'semanggi'
print(stops == 'semanggi' and stops == 'GBK')

#item in a list
favorite_colors = ['purple', 'blue', 'green']
color = 'green'
if color in favorite_colors:
    print('In list')

#iten not in a list
favorite_colors = ['purple', 'blue', 'green']
color = 'pink'
if color not in list:
    print('Not in list')
