# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_topologyvalidator.ui'
#
# Created: Sun Jan 20 14:52:39 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TopologyValidator(object):
    def setupUi(self, TopologyValidator):
        TopologyValidator.setObjectName(_fromUtf8("TopologyValidator"))
        TopologyValidator.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(TopologyValidator)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(TopologyValidator)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TopologyValidator.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TopologyValidator.reject)
        QtCore.QMetaObject.connectSlotsByName(TopologyValidator)

    def retranslateUi(self, TopologyValidator):
        TopologyValidator.setWindowTitle(QtGui.QApplication.translate("TopologyValidator", "TopologyValidator", None, QtGui.QApplication.UnicodeUTF8))

