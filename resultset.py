class ResultSet(object):
    def __init__(self, tables=None, solution=None, precisions=None, time=None, iters=None, roots=[]):
        self.tables = tables
        self.solution = solution
        self.precisions = precisions
        self.time = time
        self.numIters = iters
        self.roots = roots


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
        string = "Number of Iterations: " + str(self.numIters) + "\n"
        string += "Execution Time: " + str(self.time) + "\n"
        string += "Tables:\n"
        for i in xrange(len(self.tables)):
            string += str(self.tables[i]) + 'Precision: ' + str(self.precisions[i]) + '\n'
        return string
