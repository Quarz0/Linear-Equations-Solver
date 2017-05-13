# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'methods_options.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(349, 363)
        Dialog.setMinimumSize(QtCore.QSize(349, 363))
        Dialog.setMaximumSize(QtCore.QSize(349, 363))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 320, 291, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 332, 291))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_2 = QtGui.QWidget(self.widget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, 0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gaussEliminationCheckBox = QtGui.QCheckBox(self.widget_2)
        self.gaussEliminationCheckBox.setObjectName(_fromUtf8("gaussEliminationCheckBox"))
        self.verticalLayout_2.addWidget(self.gaussEliminationCheckBox)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtGui.QWidget(self.widget)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setContentsMargins(-1, 20, -1, 0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gaussJordanCheckBox = QtGui.QCheckBox(self.widget_4)
        self.gaussJordanCheckBox.setObjectName(_fromUtf8("gaussJordanCheckBox"))
        self.verticalLayout_3.addWidget(self.gaussJordanCheckBox)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_5 = QtGui.QWidget(self.widget)
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setContentsMargins(-1, 20, -1, 0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.luDecompositionCheckBox = QtGui.QCheckBox(self.widget_5)
        self.luDecompositionCheckBox.setObjectName(_fromUtf8("luDecompositionCheckBox"))
        self.verticalLayout_4.addWidget(self.luDecompositionCheckBox)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_9 = QtGui.QWidget(self.widget)
        self.widget_9.setObjectName(_fromUtf8("widget_9"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget_9)
        self.verticalLayout_5.setContentsMargins(-1, 20, -1, 0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.gaussSeidelCheckBox = QtGui.QCheckBox(self.widget_9)
        self.gaussSeidelCheckBox.setObjectName(_fromUtf8("gaussSeidelCheckBox"))
        self.verticalLayout_5.addWidget(self.gaussSeidelCheckBox)
        self.verticalLayout.addWidget(self.widget_9)
        self.widget_8 = QtGui.QWidget(self.widget)
        self.widget_8.setObjectName(_fromUtf8("widget_8"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_8)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_6 = QtGui.QLabel(self.widget_8)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        self.gaussSeidelInitialGuessField = QtGui.QLineEdit(self.widget_8)
        self.gaussSeidelInitialGuessField.setObjectName(_fromUtf8("gaussSeidelInitialGuessField"))
        self.horizontalLayout_4.addWidget(self.gaussSeidelInitialGuessField)
        self.verticalLayout.addWidget(self.widget_8)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.gaussEliminationCheckBox.setText(_translate("Dialog", "Gauss-Elimination", None))
        self.gaussJordanCheckBox.setText(_translate("Dialog", "Gauss-Jordan", None))
        self.luDecompositionCheckBox.setText(_translate("Dialog", "LU Decomposition", None))
        self.gaussSeidelCheckBox.setText(_translate("Dialog", "Gauss-Seidel", None))
        self.label_6.setText(_translate("Dialog", "Initial Guess:", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
