from gauss_elimination import partial_pivot

def gauss_jordan(A, B):
    n = len(B)
    o = [i for i in xrange(n)]
    for k in xrange(0, n):
        partial_pivot(n, k, A, o)
        for i in xrange(0, n):
            if i == k: continue
            factor = A[o[i]][k] / A[o[k]][k]
            for j in xrange(k + 1, n):
                A[o[i]][j] -= factor * A[o[k]][j]
            B[o[i]] -= factor * B[o[k]]

    X = [B[o[i]] / A[o[i]][i] for i in xrange(n)]
    return X


A = [[25.0, 5.0, 1.0], [64.0, 8.0, 1.0], [144.0, 12.0, 1.0]]
B = [106.8, 177.2, 279.2]
# A = [[1.0, 1.0, 1.0], [1.0, 1.0, 2.0], [1.0, 2.0, 2.0]]
# B = [1.0, 2.0, 1.0]
# A = [[25.0, 5.0, 1.0]]
print gauss_jordan(A, B)

# print B
