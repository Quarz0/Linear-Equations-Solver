import timeit
from util import *
from table import Table
from resultset import ResultSet


def gauss_elimination(A, B, variables=None, iterations=50, eps=0.0000):
    tempA, tempB = A, B
    B = matrixToVector(B)
    n = len(B)
    o = [i for i in xrange(n)]
    if variables == None: variables = ['x' + str(i + 1) for i in xrange(n)]

    startTime = timeit.default_timer()
    forward_elimination(n, o, A, B)
    X = back_substitution(n, o, A, B)
    executionTime = timeit.default_timer() - startTime

    tables = {}
    for i in xrange(n):
        tables[variables[i]] = Table(str(variables[i]), ['Step', variables[i], 'Abs. Error'], [1, X[i], '-'])

    return ResultSet(tempA, tempB, variables, 'Gauss-Elimination', tables, vectorToMatrix(X),
                     calcPrecision([0 for i in xrange(n)], variables), executionTime, 1)

# A = [[25.0, 5.0, 1.0], [64.0, 8.0, 1.0], [144.0, 12.0, 1.0]]
# B = [106.8, 177.2, 279.2]
# A = [[1.0, 1.0, 1.0], [1.0, 1.0, 2.0], [1.0, 2.0, 2.0]]
# B = [1.0, 2.0, 1.0]
# A = [[25.0, 5.0, 1.0]]
# print gauss_elimination(A, B)
