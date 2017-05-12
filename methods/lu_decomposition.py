from util import forward_elimination


def LU_decomposition(A, B):
    n = len(B)
    o = [i for i in xrange(n)]
    forward_elimination(n, o, A)

    Y = [B[o[0]] for i in xrange(n)]
    for i in xrange(1, n):
        Y[i] = B[o[i]] - sum([A[o[i]][j] * Y[j] for j in xrange(0, i)])

    X = [Y[n - 1] / A[o[n - 1]][n - 1] for i in xrange(n)]
    for i in xrange(n - 2, -1, -1):
        X[i] = (Y[i] - sum([A[o[i]][j] * X[j] for j in xrange(i + 1, n)])) / A[o[i]][i]

    return X


    # A = [[25.0, 5.0, 1.0], [64.0, 8.0, 1.0], [144.0, 12.0, 1.0]]
    # B = [106.8, 177.2, 279.2]
    # A = [[1.0, 1.0, 1.0], [1.0, 1.0, 2.0], [1.0, 2.0, 2.0]]
    # B = [1.0, 2.0, 1.0]
    # A = [[25.0, 5.0, 1.0]]
    # print LU_decomposition(A, B)
