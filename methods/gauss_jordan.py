import timeit

from resultset import ResultSet
from table import Table
from util import *


def gauss_jordan(A, B, variables=None, iterations=50, eps=0.0000):
    tempA, tempB = A, B
    B = matrixToVector(B)

    n = len(B)
    o = [i for i in xrange(n)]
    if variables == None: variables = ['x' + str(i + 1) for i in xrange(n)]

    startTime = timeit.default_timer()
    for k in xrange(0, n):
        partial_pivot(n, k, A, o)
        for i in xrange(0, n):
            if i == k: continue
            factor = A[o[i]][k] / A[o[k]][k]
            for j in xrange(k + 1, n):
                A[o[i]][j] -= factor * A[o[k]][j]
            B[o[i]] -= factor * B[o[k]]

    X = [B[o[i]] / A[o[i]][i] for i in xrange(n)]

    executionTime = timeit.default_timer() - startTime

    tables = {}
    for i in xrange(n):
        tables[variables[i]] = Table(str(variables[i]), ['Step', variables[i], 'Abs. Error'], [1, X[i], '-'])

    return ResultSet(tempA, tempB, variables, 'Gauss-Jordan', tables, vectorToMatrix(X),
                     calcPrecision([0 for i in xrange(n)], variables), executionTime, 1)

# A = [[25.0, 5.0, 1.0], [64.0, 8.0, 1.0], [144.0, 12.0, 1.0]]
# B = [106.8, 177.2, 279.2]
# A = [[1.0, 1.0, 1.0], [1.0, 1.0, 2.0], [1.0, 2.0, 2.0]]
# B = [1.0, 2.0, 1.0]
# A = [[25.0, 5.0, 1.0]]
# print gauss_jordan(A, B)

# print B
