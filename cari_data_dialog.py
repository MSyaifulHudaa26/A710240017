# Form implementation generated from reading ui file 'cari_data_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CariDataDialogBase(object):
    def setupUi(self, CariDataDialogBase):
        CariDataDialogBase.setObjectName("CariDataDialogBase")
        CariDataDialogBase.resize(273, 96)
        self.verticalLayout = QtWidgets.QVBoxLayout(CariDataDialogBase)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=CariDataDialogBase)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=CariDataDialogBase)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(parent=CariDataDialogBase)
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.verticalLayout.addWidget(self.buttonBox_2)

        self.retranslateUi(CariDataDialogBase)
        QtCore.QMetaObject.connectSlotsByName(CariDataDialogBase)

    def retranslateUi(self, CariDataDialogBase):
        _translate = QtCore.QCoreApplication.translate
        CariDataDialogBase.setWindowTitle(_translate("CariDataDialogBase", "Cari Data"))
        self.label.setText(_translate("CariDataDialogBase", "Masukkan nama warga"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CariDataDialogBase = QtWidgets.QDialog()
    ui = Ui_CariDataDialogBase()
    ui.setupUi(CariDataDialogBase)
    CariDataDialogBase.show()
    sys.exit(app.exec())
