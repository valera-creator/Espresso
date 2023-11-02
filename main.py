import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.see.clicked.connect(self.load_table)

    def load_table(self):
        self.cor = sqlite3.connect('coffee.sqlite')
        self.cur = self.cor.cursor()
        self.tableWidget.verticalHeader().setVisible(False)

        self.data = self.cur.execute("Select * from coffee").fetchall()
        self.tableWidget.setColumnCount(len(self.data[0]))
        names = [description[0] for description in self.cur.description]
        self.tableWidget.setHorizontalHeaderLabels(names)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(self.data):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()


def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec())
