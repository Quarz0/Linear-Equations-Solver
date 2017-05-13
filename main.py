import matplotlib.pyplot as plt
import sys
from PyQt4 import QtGui, QtCore, uic
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

from methods_options import Ui_Dialog
from resultset import ResultSet

plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

qtCreatorFile = "window.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class NewNavigationToolbar(NavigationToolbar):
    toolitems = [t for t in NavigationToolbar.toolitems if
                 t[0] in ('Home', 'Pan', 'Zoom', 'Save')]


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    tempResultSets = []
    tempTables = []

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.init_Figure()

        self.solveButton.setEnabled(False)
        self.solveButton.clicked.connect(self.solveEquations)
        self.resultsTabWidget.clear()
        self.resultsTabWidget.currentChanged.connect(self.handleResultTabChanging)
        self.methodsButton.clicked.connect(self.handleMethodsButton)

        self.textAreaRadio.toggled.connect(self.handleRadioButtons)
        self.textAreaRadio.toggle()
        number_group = QtGui.QButtonGroup(self)  # Number group
        number_group.addButton(self.textAreaRadio)
        number_group.addButton(self.fileRadio)

        self.loadFileButton.setDisabled(True)
        self.loadFileButton.clicked.connect(self.openLoadFileDialog)
        self.fileRadio.toggled.connect(self.handleRadioButtons)

        self.matrixInputArea.textChanged.connect(self.drawMatrix)

        self.Dialog = QtGui.QDialog()
        self.dialogUI = Ui_Dialog()
        self.dialogUI.setupUi(self.Dialog)

        self.solveButton.connect(self.handleSolveButton)

    @QtCore.pyqtSlot()
    def solveEquations(self):
        print "Solving"

    @QtCore.pyqtSlot()
    def handleMethodsButton(self):
        print "Handling Methods Button"

    @QtCore.pyqtSlot()
    def handleResultTabChanging(self):
        print "Handling results tab"

    @QtCore.pyqtSlot()
    def openLoadFileDialog(self):
        print "Opening Load file dialog"

    @QtCore.pyqtSlot()
    def handleRadioButtons(self):
        self.matrixInputArea.setReadOnly(
            True) if not self.textAreaRadio.isChecked() else self.matrixInputArea.setReadOnly(
            False)
        self.loadFileButton.setDisabled(True) if not self.fileRadio.isChecked() else self.loadFileButton.setDisabled(
            False)

    @QtCore.pyqtSlot()
    def drawMatrix(self):
        print "Drawing Matrix"

    @QtCore.pyqtSlot()
    def handleSolveButton(self):
        print "Handling Solve Button"

    def init_Figure(self):
        self.figure = plt.figure()
        self.figure.patch.set_facecolor('white')
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NewNavigationToolbar(self.canvas, self.mplwindow, coordinates=False)
        # plt.text(0, 0.5, latex(Eq(
        #     MatMul(Matrix([[322222222222222222222222.55555555222111144444555555, 2.000000000000000000000000000001]]),
        #            Matrix([['xadsdasdasdasdasdasdasdas'], ['ysadasdsadasdsadasdasdasds']]), evaluate=False),
        #     Matrix([[1, 2]]), evaluate=False), mode='inline'), fontsize=30)
        plt.axis('off')
        self.mplvl.addWidget(self.canvas)
        self.mplvl.addWidget(self.toolbar)
        self.toolbar._actions['pan'].trigger()
        self.toolbar._actions['pan'].setVisible(False)
        self.toolbar._actions['zoom'].setVisible(False)

    def drawResultSet(self, resultSet):
        assert type(resultSet) is ResultSet, "resultSet is not of type ResultSet!: " + str(type(resultSet))
        self.tempResultSets.append(resultSet)
        self.variablesComboBox.addItems(list(resultSet.getTables().keys()).sort())  # move to @Solve button
        qWidget = self.drawTable(resultSet.getIdentifier())
        self.updateTables()  # move to @Solve button
        self.drawTime(resultSet.getExecutionTime(), qWidget.findChild(QtGui.QLineEdit, "Time"))

        # self.drawSolution(resultSet.getSolution())
        # self.drawRoot(resultSet.getRoot(), qWidget.findChild(QtGui.QLineEdit, "Root"))
        # self.drawPrecision(resultSet.getPrecision(), qWidget.findChild(QtGui.QLineEdit, "Precision"))
        # self.plotError(resultSet.getErrors())
        # self.plotRoot(resultSet.getRoots())

    def drawTable(self, identifier):
        qWidget = self.initTableWidget()
        self.resultsTabWidget.addTab(qWidget, QtCore.QString(identifier))
        qTable = self.resultsTabWidget.findChild(QtGui.QTableWidget, "Table")
        self.tempTables.append(qTable)
        qTable.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        qTable.setSelectionBehavior(QtGui.QTableWidget.SelectRows)
        qTable.setSelectionMode(QtGui.QTableWidget.SingleSelection)
        qTable.itemSelectionChanged.connect(self.plotTempBoundaries)
        return qWidget

    def initTableWidget(self):
        qWidget = QtGui.QWidget()
        qVbox = QtGui.QVBoxLayout()
        qTable = QtGui.QTableWidget()
        qTable.setObjectName("Table")
        qWidget3 = QtGui.QWidget()
        hBox2 = QtGui.QHBoxLayout()
        hBox2.setMargin(0)
        precisionLabel = QtGui.QLabel()
        precisionLabel.setText("Precision")
        precisionField = QtGui.QLineEdit()
        precisionField.setObjectName("Precision")
        precisionField.setReadOnly(True)
        timeLabel = QtGui.QLabel()
        timeLabel.setText("Time")
        timeField = QtGui.QLineEdit()
        timeField.setObjectName("Time")
        timeField.setReadOnly(True)
        hBox2.addWidget(precisionLabel)
        hBox2.addWidget(precisionField)
        hBox2.addWidget(timeLabel)
        hBox2.addWidget(timeField)
        qWidget3.setLayout(hBox2)
        qVbox.addWidget(qTable)
        qVbox.addWidget(qWidget3)
        qWidget.setLayout(qVbox)
        return qWidget

        # def updateTables(self):


        # def drawSolution(self):
        #
        #
        # def drawTime(self):
        #
        #
        # def drawTables(self):


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
