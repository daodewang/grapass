# analysis the grapass of cellphone

import numpy as np

"""
a b c
d e f
g h i
"""

"""
a c i g b d f h e
"""


neib = [[0,0,0,0,1,1,0,0,1],
        [0,0,0,0,1,0,1,0,1],
        [0,0,0,0,0,0,1,1,1],
        [0,0,0,0,0,1,0,1,1],
        [1,1,0,0,0,1,1,0,1],
        [1,0,0,1,1,0,0,1,1],
        [0,1,1,0,1,0,0,1,1],
        [0,0,1,1,0,1,1,0,1],
        [1,1,1,1,1,1,1,1,0]]

m = np.array(neib)

print(m)

print(m*m)
