# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TopologyValidator
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
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "Topology Validator"


def description():
    return "Check data for topology errors (no gaps, no overlapping, ...)"


def version():
    return "Version 1.0"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "1.8"

def author():
    return "Viktorija Solovjova"

def email():
    return "viktorija.solovjova@gmail.com"

def classFactory(iface):
    # load TopologyValidator class from file TopologyValidator
    from topologyvalidator import TopologyValidator
    return TopologyValidator(iface)
