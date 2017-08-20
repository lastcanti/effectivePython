"""
    All about slicing sequences. You can access sequences
    with very minimal effort. You can slice str, list, and
    bytes. Slicing can be extended to any python class
    that implements __defitem__ and __setitem__
"""

# don't use 0 at start index or length at end
# slicing is forgiving when out of bounds 
# assinging to a list slice will replace that--
#-range in the original sequence

# the most basic slice is somelist[start:end]
abc = ['a','b','c','d','e','f','g','h']
print('First four: ', abc[:4])
print('Last four: ', abc[-4:])
print('Middle two: ', abc[3:-3])

# slicing from start of list leave out 0
assert abc[:5] == abc[0:5]

# use negative numbers for slices if possible
abc[:]
abc[:5] #['a','b','c','d','e']
abc[:-1]
abc[4:]
abc[3:]
abc[-3:]

# slicing deals with indexes at start and end
firstItemTwentyTimes= abc[:20]

# slicing creates an entirely new list
