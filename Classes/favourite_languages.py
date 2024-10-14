# Orederdict module and python standard library
from collections import OrderedDict
fav_langs = OrderedDict()

fav_langs['jen'] = 'python'
fav_langs['sarah'] = 'c'
fav_langs['edward'] = 'ruby'
fav_langs['phil'] = 'python'

for n, lang in fav_langs.items():
    print(n.title()+ "'s favorite language is" , 
          lang.title())