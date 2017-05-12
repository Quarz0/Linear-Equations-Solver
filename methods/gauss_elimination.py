from util import *


def gauss_elimination(A, B):
    n = len(B)
    o = [i for i in xrange(n)]
    forward_elimination(n, o, A, B)
    return back_substitution(n, o, A, B)

# A = [[25.0, 5.0, 1.0], [64.0, 8.0, 1.0], [144.0, 12.0, 1.0]]
# B = [106.8, 177.2, 279.2]
# A = [[1.0, 1.0, 1.0], [1.0, 1.0, 2.0], [1.0, 2.0, 2.0]]
# B = [1.0, 2.0, 1.0]
# A = [[25.0, 5.0, 1.0]]
# print gauss_elimination(A, B)
