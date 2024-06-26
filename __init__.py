# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PierwszaWtyczka
                                 A QGIS plugin
 Wtyczka liczy pola powierzchni i odleglosci miedzy nimi
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-06-03
        copyright            : (C) 2024 by JuliaSobczykJuliaDzierżanowska
        email                : 01179225@pw.edu.pl
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PierwszaWtyczka class from file PierwszaWtyczka.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .WtyczkaPierwsza import PierwszaWtyczka
    return PierwszaWtyczka(iface)
