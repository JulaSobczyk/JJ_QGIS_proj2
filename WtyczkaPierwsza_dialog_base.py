# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WtyczkaPierwsza_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PierwszaWtyczkaDialogBase(object):
    def setupUi(self, PierwszaWtyczkaDialogBase):
        PierwszaWtyczkaDialogBase.setObjectName("PierwszaWtyczkaDialogBase")
        PierwszaWtyczkaDialogBase.resize(796, 453)
        self.mMapLayerComboBox = QgsMapLayerComboBox(PierwszaWtyczkaDialogBase)
        self.mMapLayerComboBox.setGeometry(QtCore.QRect(360, 20, 251, 31))
        self.mMapLayerComboBox.setObjectName("mMapLayerComboBox")
        self.label_wyb_warstwe = QtWidgets.QLabel(PierwszaWtyczkaDialogBase)
        self.label_wyb_warstwe.setGeometry(QtCore.QRect(10, 10, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_wyb_warstwe.setFont(font)
        self.label_wyb_warstwe.setObjectName("label_wyb_warstwe")
        self.label_przewyzszenie = QtWidgets.QLabel(PierwszaWtyczkaDialogBase)
        self.label_przewyzszenie.setGeometry(QtCore.QRect(10, 50, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_przewyzszenie.setFont(font)
        self.label_przewyzszenie.setObjectName("label_przewyzszenie")
        self.pushButton_oblicz_dh = QtWidgets.QPushButton(PierwszaWtyczkaDialogBase)
        self.pushButton_oblicz_dh.setGeometry(QtCore.QRect(30, 300, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_oblicz_dh.setFont(font)
        self.pushButton_oblicz_dh.setObjectName("pushButton_oblicz_dh")
        self.label_wynik_przewyz = QtWidgets.QLabel(PierwszaWtyczkaDialogBase)
        self.label_wynik_przewyz.setGeometry(QtCore.QRect(300, 60, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_wynik_przewyz.setFont(font)
        self.label_wynik_przewyz.setText("")
        self.label_wynik_przewyz.setObjectName("label_wynik_przewyz")
        self.pushButton_oblicz_pol_pow = QtWidgets.QPushButton(PierwszaWtyczkaDialogBase)
        self.pushButton_oblicz_pol_pow.setGeometry(QtCore.QRect(30, 370, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_oblicz_pol_pow.setFont(font)
        self.pushButton_oblicz_pol_pow.setObjectName("pushButton_oblicz_pol_pow")
        self.label_pol_pow = QtWidgets.QLabel(PierwszaWtyczkaDialogBase)
        self.label_pol_pow.setGeometry(QtCore.QRect(10, 110, 457, 36))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_pol_pow.setFont(font)
        self.label_pol_pow.setObjectName("label_pol_pow")
        self.label_wynik_pol_pow = QtWidgets.QLabel(PierwszaWtyczkaDialogBase)
        self.label_wynik_pol_pow.setGeometry(QtCore.QRect(490, 110, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_wynik_pol_pow.setFont(font)
        self.label_wynik_pol_pow.setText("")
        self.label_wynik_pol_pow.setObjectName("label_wynik_pol_pow")
        self.pushButton_czysc_konsole = QtWidgets.QPushButton(PierwszaWtyczkaDialogBase)
        self.pushButton_czysc_konsole.setGeometry(QtCore.QRect(510, 370, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_czysc_konsole.setFont(font)
        self.pushButton_czysc_konsole.setObjectName("pushButton_czysc_konsole")
        self.pushButton_tworz_poligon = QtWidgets.QPushButton(PierwszaWtyczkaDialogBase)
        self.pushButton_tworz_poligon.setGeometry(QtCore.QRect(450, 300, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_tworz_poligon.setFont(font)
        self.pushButton_tworz_poligon.setObjectName("pushButton_tworz_poligon")
        self.comboBox = QtWidgets.QComboBox(PierwszaWtyczkaDialogBase)
        self.comboBox.setGeometry(QtCore.QRect(600, 160, 61, 41))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox.setMaxVisibleItems(5)
        self.comboBox.setObjectName("comboBox")
        self.label_wyb_pol_pow_polig = QtWidgets.QLabel(PierwszaWtyczkaDialogBase)
        self.label_wyb_pol_pow_polig.setGeometry(QtCore.QRect(10, 150, 571, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_wyb_pol_pow_polig.setFont(font)
        self.label_wyb_pol_pow_polig.setObjectName("label_wyb_pol_pow_polig")
        self.label_pol_polig = QtWidgets.QLabel(PierwszaWtyczkaDialogBase)
        self.label_pol_polig.setGeometry(QtCore.QRect(10, 200, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_pol_polig.setFont(font)
        self.label_pol_polig.setObjectName("label_pol_polig")
        self.label_wynik_pol_polig = QtWidgets.QLabel(PierwszaWtyczkaDialogBase)
        self.label_wynik_pol_polig.setGeometry(QtCore.QRect(380, 210, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_wynik_pol_polig.setFont(font)
        self.label_wynik_pol_polig.setText("")
        self.label_wynik_pol_polig.setObjectName("label_wynik_pol_polig")

        self.retranslateUi(PierwszaWtyczkaDialogBase)
        QtCore.QMetaObject.connectSlotsByName(PierwszaWtyczkaDialogBase)

    def retranslateUi(self, PierwszaWtyczkaDialogBase):
        _translate = QtCore.QCoreApplication.translate
        PierwszaWtyczkaDialogBase.setWindowTitle(_translate("PierwszaWtyczkaDialogBase", "Lenght and Area counter"))
        self.label_wyb_warstwe.setText(_translate("PierwszaWtyczkaDialogBase", "Wybierz warstwe"))
        self.label_przewyzszenie.setText(_translate("PierwszaWtyczkaDialogBase", "Przewyższenie"))
        self.pushButton_oblicz_dh.setText(_translate("PierwszaWtyczkaDialogBase", " Oblicz przewyższenie między punktami"))
        self.pushButton_oblicz_pol_pow.setText(_translate("PierwszaWtyczkaDialogBase", "Oblicz pole powierzchni wybranych puktów"))
        self.label_pol_pow.setText(_translate("PierwszaWtyczkaDialogBase", "Pole powierzchni między punktami"))
        self.pushButton_czysc_konsole.setText(_translate("PierwszaWtyczkaDialogBase", "Wyczyść konsolę"))
        self.pushButton_tworz_poligon.setText(_translate("PierwszaWtyczkaDialogBase", "Utwórz poligon z wybranych punktów"))
        self.label_wyb_pol_pow_polig.setText(_translate("PierwszaWtyczkaDialogBase", "Wybierz jednostkę pola powierzchni poligonu"))
        self.label_pol_polig.setText(_translate("PierwszaWtyczkaDialogBase", "Pole powierzchni poligonu"))
from qgsmaplayercombobox import QgsMapLayerComboBox


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PierwszaWtyczkaDialogBase = QtWidgets.QDialog()
    ui = Ui_PierwszaWtyczkaDialogBase()
    ui.setupUi(PierwszaWtyczkaDialogBase)
    PierwszaWtyczkaDialogBase.show()
    sys.exit(app.exec_())
