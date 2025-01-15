import sys

from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog


class MyApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.exportButton.clicked.connect(self.export)
        self.ui.addButton.clicked.connect(self.addItem)
        self.ui.removeButton.clicked.connect(self.removeItem)

        self.show()

    def export(self):
        with open("export.txt", "w") as f:
            for i in range(self.ui.productList.count()):
                f.write(self.ui.productList.item(i).text() + "\n")
        f.close()

    def addItem(self):
        alert = self.validate()
        if alert is None:
            self.ui.productList.addItem(self.ui.nameEdit.text())
        else:
            alert.exec()

    def removeItem(self):
        if self.ui.productList.currentRow() == -1:
            return
        self.ui.productList.takeItem(self.ui.productList.currentRow())

    def validate(self):
        if self.ui.nameEdit.text() == '' or self.ui.amountEdit.text() == '':
            alert = QMessageBox()
            alert.setInformativeText("Nazwa i ilość nie mogą być puste")
            alert.setWindowTitle("Błąd")
            alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            return alert
        if self.ui.nameEdit.text().__len__() > 50:
            alert = QMessageBox()
            alert.setInformativeText("Nazwa jest za długa")
            alert.setWindowTitle("Błąd")
            alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            return alert
        return None


def main():
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
