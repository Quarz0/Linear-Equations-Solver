import timeit

from resultset import ResultSet
from table import Table
from util import *


def gauss_seidel(A, B, X0, variables=None, iterations=50, eps=0.00001):
    B = matrixToVector(B)
    X_new, X_old = X0[:], X0[:]
    n = len(X0)

    iterationRows = [[] for i in xrange(n)]
    ea = ['-' for i in xrange(n)]
    ea_rel = ['-' for i in xrange(n)]
    roots = [[] for i in xrange(n)]

    for j in xrange(n):
        roots[j].append((1, X0[j]))
        iterationRows[j].append([1, X0[j], '-'])

    startTime = timeit.default_timer()

    for t in xrange(iterations):
        max_ea = -1
        for i in xrange(n):
            sum1 = sum([A[i][k] * X_new[k] for k in xrange(0, i)])
            sum2 = sum([A[i][k] * X_old[k] for k in xrange(i + 1, n)])
            X_new[i] = (B[i] - sum1 - sum2) / A[i][i]

            ea[i] = abs(X_new[i] - X_old[i])
            ea_rel[i] = abs(X_new[i] - X_old[i]) / max(abs(X_new[i]), abs(X_old[i]))
            max_ea = max(max_ea, ea[i])
            iterationRows[i].append([t + 2, X_new[i], ea[i]])
            roots[i].append((t + 2, X_new[i]))

        X_old = X_new[:]
        if max_ea < eps:
            break

    executionTime = timeit.default_timer() - startTime

    if variables == None: variables = ['x' + str(i + 1) for i in xrange(n)]
    tables = {}
    for i in xrange(n):
        tables[variables[i]] = Table(str(variables[i]), ['Step', 'x' + str(i + 1), 'Abs. Error'], iterationRows[i])

    return ResultSet('Gauss-Seidel', tables, vectorToMatrix(X_new), calcPrecision(ea_rel, variables), executionTime, t + 2, roots)

# A = [[12, 3, -5], [1, 5, 3], [3, 7, 13]]
# C = [1, 0, 1]
# B = [[1], [28], [76]]
# castMatrixToFloat(A)
# castMatrixToFloat(B)
# castMatrixToFloat(C)
# print gauss_seidel(A, B, C, eps=0.00000001)
