# 9-13
from collections import OrderedDict
glossery2 = OrderedDict()

glossery2['variable'] = 'A name that refers to a value stored in memory.'
glossery2['tuple'] = 'An immutable collection of items in a particular order.'
glossery2['loop'] = 'An immutable collection of items in a particular order.'
glossery2['list'] = 'A collection of items in a particular order, mutable and allows duplicate entries.'
glossery2['dictionary'] = 'A collection of key-value pairs, where each key is unique and maps to a value.'



for k, v in glossery2.items():
    print(f"\nTerm: {k.title()}")
    print(f"DEF: {v}")