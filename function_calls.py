# Function calls: create a new dictionary showing the frequency of elements in a list [array]

authors = ['Pratchett', 'Clarke', 'Cornwell', 'Pratchett', 'Ende', 'Ende', 'Pratchett']

# reports the frequency of each item
def analyse_this_list(l):

    # One nice empty dictionary.
    counts = {}

    for item in l:
        if item in counts:
            counts[item]=counts[item]+1
        else:
            counts[item]=1

    return counts

counts = analyse_this_list(authors)
print counts

