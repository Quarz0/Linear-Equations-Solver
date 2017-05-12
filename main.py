import matplotlib.pyplot as plt
import sys
from PyQt4 import QtGui, uic
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

qtCreatorFile = "window.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class NewNavigationToolbar(NavigationToolbar):
    toolitems = [t for t in NavigationToolbar.toolitems if
                 t[0] in ('Home', 'Pan', 'Zoom', 'Save')]


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.init_Figure()

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


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
