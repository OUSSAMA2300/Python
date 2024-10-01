import sandwiches
sandwiches.make_sadwich('tuna', 'honey')

from sandwiches import make_sadwich
make_sadwich('garlic')

from sandwiches import make_sadwich as ms
ms('jam')

import sandwiches as sand
sand.make_sadwich('grilled cheese')

from sandwiches import *
sandwiches.make_sadwich('flafel')