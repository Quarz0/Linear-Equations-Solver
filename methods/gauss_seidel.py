
def gauss_seidel(A, B, X0, iterations=50, eps=0.00001):

    X_new, X_old = X0, X0
    n = len(B)

    for t in xrange(iterations):
        for i in xrange(n):
            sum1 = sum([A[i][k] * X_new[k] for k in xrange(0, i)])
            sum2 = sum([A[i][k] * X_old[k] for k in xrange(i+1, n)])
            X_new[i] = (B[i] - sum1 - sum2) / A[i][i]

        X_old = X_new

    return X_new
