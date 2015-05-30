# While loops in Python

vegetables = ['tomato', 'asparagus', 'zucchini', 'cauliflower']

i = 0

while (i < len(vegetables)):
    print "Vegetable number %d is" % (i),
    if (vegetables[i][0:1] in 'aeiou'):
        print "an",
    else:
        print "a",
    print vegetables[i]
    i = i + 1

