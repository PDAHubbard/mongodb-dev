
fruit = ['apple', 'grape', 'banana']

new_fruits = []

for item in fruit:
    print item
    new_fruits.append(item)

print new_fruits

###
sum = 0

numbers = [1, 2, 3, 5, 8]

for i in numbers:
    sum+=i

print i

###
person = {'name':'Peter', 'height':'short', 'nose_flavour':'pineapple'}

for key in person:
    print key + " :-> " + person[key]

###
people = {'name':'Bob', 'hometown':'Palo Alto', 'favourite_colour':'red'}
for item in people:
    if (item == 'favourite_colour'):
        print people[item]
