class ResultSet(object):
    def __init__(self, matrixA=None, matrixB=None, variables=None, name=None, tables=None, solution=None,
                 precisions=None, time=None, iters=None, roots=[]):
        self.matrixA = matrixA
        self.matrixB = matrixB
        self.variables = variables
        self.name = name
        self.tables = tables
        self.solution = solution
        self.precisions = precisions
        self.time = time
        self.numIters = iters
        self.roots = roots

    def getMatrixA(self):
        return self.matrixA

    def getMatrixB(self):
        return self.matrixB

    def getVariables(self):
        return self.variables

    def getName(self):
        return self.name

    def getSolution(self):
        return self.solution

    def getTables(self):
        return self.tables

    def getPrecisions(self):
        return self.precisions

    def getExecutionTime(self):
        return self.time

    def getNumberOfIterations(self):
        return self.numIters

    def getRoots(self):
        return self.roots

    def __str__(self):
        string = "Solution: " + str(self.solution)
        string += "Number of Iterations: " + str(self.numIters) + "\n"
        string += "Execution Time: " + str(self.time) + "\n"
        string += "Tables:\n"
        for var in self.tables.keys():
            string += str(self.tables[var]) + 'Precision: ' + str(self.precisions[var]) + '\n'
        return string
