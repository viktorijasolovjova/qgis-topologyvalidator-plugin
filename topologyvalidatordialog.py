# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TopologyValidatorDialog
                                 A QGIS plugin
 Check data for topology errors (no gaps, no overlapping, ...)
                             -------------------
        begin                : 2013-01-20
        copyright            : (C) 2013 by Viktorija Solovjova
        email                : viktorija.solovjova@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_topologyvalidator import Ui_TopologyValidator
# create the dialog for zoom to point


class TopologyValidatorDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_TopologyValidator()
        self.ui.setupUi(self)
