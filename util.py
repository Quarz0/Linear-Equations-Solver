import math


def calcPrecision(ea):
    return ['Exact' if k == 0 else int(-1 * math.log10(2.0 * k)) for k in ea]


def castMatrixToFloat(matrix):
    for i in xrange(len(matrix)):
        if type(matrix[i]) == type([]):
            for j in xrange(len(matrix[i])):
                matrix[i][j] = float(matrix[i][j])
        else:
            matrix[i] = float(matrix[i])


def partial_pivot(n, k, A, o):
    p = k
    for i in xrange(k + 1, n):
        if abs(A[o[i]][k]) > abs(A[o[p]][k]):
            p = i
    o[k], o[p] = o[p], o[k]


def forward_elimination(n, o, A, B=None):
    for k in xrange(0, n - 1):
        partial_pivot(n, k, A, o)
        for i in xrange(k + 1, n):
            factor = A[o[i]][k] / A[o[k]][k]
            for j in xrange(k + 1, n):
                A[o[i]][j] -= factor * A[o[k]][j]
            if B != None:
                B[o[i]] -= factor * B[o[k]]
            A[o[i]][k] = factor


def back_substitution(n, o, A, B):
    X = [0 for i in xrange(len(B))]
    X[n - 1] = B[o[n - 1]] / A[o[n - 1]][n - 1]
    for i in xrange(n - 2, -1, -1):
        sum_ = sum([A[o[i]][j] * X[j] for j in xrange(i + 1, n)])
        X[i] = (B[o[i]] - sum_) / A[o[i]][i]
    return X
