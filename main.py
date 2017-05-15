import importlib
import matplotlib.pyplot as plt
import numpy as np
from PyQt4 import QtGui, QtCore, uic
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from sympy import *
from sympy.core.sympify import SympifyError

from methods_options import Ui_Dialog
from resultset import ResultSet
from util import sliceEquations, parseFloats, matrixToVector

plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

qtCreatorFile = "window.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class NewNavigationToolbar(NavigationToolbar):
    toolitems = [t for t in NavigationToolbar.toolitems if
                 t[0] in ('Home', 'Pan', 'Zoom', 'Save')]


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    solveButtonTrigger = QtCore.pyqtSignal()
    methodsCheckMap = None
    Dialog = None
    dialogUI = None
    rootPlot = None
    text = None
    isValidEquation = False
    methodsCheckMapAlias = {}
    tempResultSets = []
    tempTables = []
    tempFloatA = []
    tempFloatB = []
    tempVars = []
    initialGaussSeidel = []
    figs = []

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.figs = [(Figure(), [self.rootPlot, self.mplvl3, self.mplwindow3])]
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

        self.methodsCheckMap = {self.dialogUI.gaussEliminationCheckBox: [],
                                self.dialogUI.gaussJordanCheckBox: [],
                                self.dialogUI.luDecompositionCheckBox: [],
                                self.dialogUI.gaussSeidelCheckBox: [self.dialogUI.gaussSeidelInitialGuessField]}
        self.solveButtonTrigger.connect(self.handleSolveButton)
        self.cloneOptionsMapInfo()
        self.initOptionsHandlers()
        self.variablesComboBox.currentIndexChanged.connect(self.updateTables)

    @QtCore.pyqtSlot()
    def solveEquations(self):
        self.clearAll()
        ((A, vars), B) = sliceEquations(str(self.matrixInputArea.toPlainText()))
        self.tempFloatA = parseFloats(A)
        self.tempFloatB = parseFloats(B)
        self.tempVars = vars
        for (key, val) in self.methodsCheckMapAlias.items():
            if val[0]:
                method = str(key.objectName())
                self.drawResultSet(
                    getattr(importlib.import_module('methods.' + method), method)(self.tempFloatA, self.tempFloatB,
                                                                                  self.initialGaussSeidel,
                                                                                  variables=matrixToVector(vars)))
        self.variablesComboBox.addItems([vars[i][0] for i in xrange(len(vars))])

        # self.plotAll()

    @QtCore.pyqtSlot()
    def handleMethodsButton(self):
        if self.Dialog.exec_():
            self.cloneOptionsMapInfo()
            self.solveButtonTrigger.emit()
        else:
            self.pasteToOptionsMapInfo()

    @QtCore.pyqtSlot(int)
    def handleResultTabChanging(self, index):
        for tab in self.tempTables:
            tab.clearSelection()
        try:
            vars = []
            for i in xrange(len(self.tempVars)):
                subVar = []
                for j in xrange(len(self.tempVars[i])):
                    subVar.append(self.tempVars[i][j] + '=' + str(self.tempResultSets[index].getSolution()[i][j]))
                vars.append(subVar)
            # print latex(Eq(
            #     MatMul(Matrix(self.tempFloatA),
            #            Matrix(self.tempResultSets[index].getSolution()), evaluate=False),
            #     Matrix(self.tempFloatB), evaluate=False), mode='inline')
            self.text.set_text(latex(Eq(
                MatMul(Matrix(self.tempFloatA),
                       Matrix(self.tempResultSets[index].getSolution()), evaluate=False),
                Matrix(self.tempFloatB), evaluate=False), mode='inline'))
        except (SympifyError, ValueError) as e:
            print e
        self.figure.canvas.draw()

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
        ((A, vars), B) = sliceEquations(str(self.matrixInputArea.toPlainText()))
        try:
            self.text.set_text(latex(Eq(
                MatMul(Matrix(A),
                       Matrix(vars), evaluate=False),
                Matrix(B), evaluate=False), mode='inline'))
        except (SympifyError, ValueError) as e:
            print e
        self.figure.canvas.draw()
        self.solveButtonTrigger.emit()

    @QtCore.pyqtSlot()
    def handleSolveButton(self):
        chosenMethod = False
        validInputs = False
        ((A, vars), B) = sliceEquations(str(self.matrixInputArea.toPlainText()))
        for (state, val) in self.methodsCheckMapAlias.values():
            if state:
                chosenMethod = True
                try:
                    parseFloats(A)
                    parseFloats(B)
                    lis = val[0].split(',')
                    for i in xrange(len(lis)):
                        if not lis[i]:
                            lis[i] = 0.0
                        else:
                            lis[i] = float(lis[i])
                    self.initialGaussSeidel = lis[:]
                    validInputs = True and (len(lis) == len(vars)) and (len(vars) <= len(A))
                except:
                    validInputs = False
                break

        self.solveButton.setEnabled(validInputs and chosenMethod)

    @QtCore.pyqtSlot(int)
    def updateTables(self, index):
        item = str(self.variablesComboBox.itemText(index))
        for i in xrange(len(self.tempResultSets)):
            table = self.tempResultSets[i].getTables()[item]
            qTable = self.tempTables[i]
            qTable.parentWidget().findChild(QtGui.QLineEdit, "Precision").setText(
                str(self.tempResultSets[i].getPrecisions()[item]))
            qTable.setColumnCount(len(table.getHeader()))
            qTable.setRowCount(len(table.getData()))
            qTable.setHorizontalHeaderLabels(table.getHeader())
            for row in xrange(len(table.getData())):
                for column in xrange(len(table.getHeader())):
                    qTable.setItem(row, column,
                                   QtGui.QTableWidgetItem(str(('%g' % table.getData()[row][column]) if type(
                                       table.getData()[row][column]) is float else table.getData()[row][column])))

    def clearAll(self):
        count = self.resultsTabWidget.count()
        for i in xrange(count):
            self.resultsTabWidget.widget(i).deleteLater()
        self.tempTables[:] = []
        self.tempResultSets[:] = []
        self.text.set_text('')
        self.variablesComboBox.clear()
        self.clearPlots()

    def clearPlots(self):
        self.rootPlot.cla()
        self.rootPlot.grid(true)
        self.rootPlot.autoscale(true, tight=false)

    def cloneOptionsMapInfo(self):
        for (key, val) in self.methodsCheckMap.items():
            vals = []
            for va in val:
                vals.append(str(va.text()))
            self.methodsCheckMapAlias[key] = (key.isChecked(), vals)

    def pasteToOptionsMapInfo(self):
        for (key, val) in self.methodsCheckMapAlias.items():
            key.setChecked(val[0])
            for i in range(len(val[1])):
                self.methodsCheckMap[key][i].setText(val[1][i])

    def initOptionsHandlers(self):
        for (key, val) in self.methodsCheckMap.items():
            key.stateChanged.connect(self.assignReadOnlyHandler)
            key.stateChanged.connect(self.checkForValidInputs)
            for va in val:
                va.textChanged.connect(self.checkForValidInputs)

    def assignReadOnlyHandler(self, state):
        checkBox = self.Dialog.sender()
        for val in self.methodsCheckMap[checkBox]:
            val.setReadOnly(True) if not checkBox.isChecked() else val.setReadOnly(False)

    def checkForValidInputs(self, text):
        buttonState = False
        for (key, vals) in self.methodsCheckMap.items():
            if key.isChecked():
                tempState = True
                for val in vals:
                    if not val.text():
                        tempState = False
                        break
                if not tempState:
                    buttonState = False
                    break
                else:
                    buttonState = True
        self.dialogUI.buttonBox.button(QtGui.QDialogButtonBox.Ok).setEnabled(buttonState)

    def init_Figure(self):
        self.figure = plt.figure()
        self.figure.patch.set_facecolor('white')
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NewNavigationToolbar(self.canvas, self.mplwindow1, coordinates=False)
        self.text = plt.text(0, 0.5, 'WELCOME', fontsize=20)
        plt.axis('off')
        self.figure.text(0, 0.5, "", fontsize=30)

        self.mplvl1.addWidget(self.canvas)
        self.mplvl1.addWidget(self.toolbar)
        self.toolbar._actions['pan'].trigger()
        self.toolbar._actions['pan'].setVisible(False)
        self.toolbar._actions['zoom'].setVisible(False)
        self.init_Drawing_Figures()

    def init_Drawing_Figures(self):
        i = 0
        for (fig, ls) in self.figs:
            ls[0] = fig.add_subplot(111)
            ls[0].grid(true)
            canvas = FigureCanvas(fig)
            canvas.setObjectName("canvas" + str(i))
            ls[1].addWidget(canvas)
            toolbar = NavigationToolbar(canvas,
                                        ls[2], coordinates=True)
            ls[1].addWidget(toolbar)
            ls[0].autoscale(true, tight=false)
            i += 1

        self.rootPlot = self.figs[0][1][0]

    def drawResultSet(self, resultSet):
        assert type(resultSet) is ResultSet, "resultSet is not of type ResultSet!: " + str(type(resultSet))
        self.tempResultSets.append(resultSet)
        qWidget = self.drawTable(resultSet.getName())
        self.drawTime(resultSet.getExecutionTime(), qWidget.findChild(QtGui.QLineEdit, "Time"))
        # self.plotRoot(resultSet.getRoots())

    def drawTable(self, identifier):
        qWidget = self.initTableWidget()
        self.resultsTabWidget.addTab(qWidget, QtCore.QString(identifier))
        qTable = self.resultsTabWidget.findChild(QtGui.QTableWidget, "Table")
        self.tempTables.append(qTable)
        qTable.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        qTable.setSelectionBehavior(QtGui.QTableWidget.SelectRows)
        qTable.setSelectionMode(QtGui.QTableWidget.SingleSelection)
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

    def drawTime(self, time, timeField):
        assert type(time) is float or int, "time is not of type float nor int!: " + str(type(time))
        assert type(timeField) is QtGui.QLineEdit, "timeField is not of type QtGui.QLineEdit!: " + str(
            type(timeField))
        timeField.setText(str(('%g' % time)))

    def plotRoot(self, roots):
        root = []
        its = []
        print roots
        for (i, r) in roots:
            root.append(r)
            its.append(i)
        self.plt3.plot(its, root, c=np.random.rand(3, 1))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
