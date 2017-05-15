import math
from PyQt4 import QtCore

USED_VAR = 'x'


def calcPrecision(ea, variables):
    precisions = {}
    for i in xrange(len(ea)):
        precisions[variables[i]] = 'Exact' if ea[i] == 0 else int(-1 * math.log10(2.0 * ea[i]))
    return precisions


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


def sliceEquations(lines):
    A = []
    B = []
    vars = []
    equationsList = lines.split('\n')
    for equation in equationsList:
        A.append(equation.split(','))
    for lis in A:
        for i in xrange(len(lis)):
            lis[i] = lis[i].strip()
    maxSize = 0
    for equ in A:
        maxSize = max(maxSize, len(equ))
    for equ in A:
        for i in xrange(len(equ)):
            if not equ[i]:
                equ[i] = r'0.0'
        while len(equ) != maxSize:
            equ.append(r'0.0')
    if maxSize == 1:
        for lis in A:
            B.append(lis[:])
    else:
        for i in xrange(len(A)):
            b = []
            b.append(A[i][maxSize - 1])
            B.append(b)
            A[i] = A[i][:maxSize - 1]
    vars = [[USED_VAR + str(i + 1)] for i in xrange(maxSize if maxSize == 1 else maxSize - 1)]

    return ((A, vars), B)


def read(path, textArea):
    data = None
    with open(path, 'r') as file:
        data = file.read()
    textArea.setText(QtCore.QString(data))
    # return data


def write(path, matrix):
    with open(path, 'w') as file:
        for row in matrix:
            string = ''
            for num in row:
                string += ', ' + str(num)
            file.write(string[2:] + '\n')


def parseFloats(equations):
    parsedFloats = []
    for lis in equations:
        newLis = []
        for num in lis:
            newLis.append(float(num))
        parsedFloats.append(newLis)
    return parsedFloats

def matrixToVector(matrix):
    A = []
    for row in matrix:
        assert len(row) == 1
        A.append(row[0])
    return A

def vectorToMatrix(vec):
    matrix = []
    for i in vec:
        matrix.append([i])
    return matrix