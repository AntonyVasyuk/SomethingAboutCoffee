import sqlite3
import sys

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication

from main_ui import Ui_UI


class ShowCoffee(QMainWindow, Ui_UI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        self.update()

    def update(self) -> None:
        result = self.cur.execute(f"""
        SELECT id, (SELECT name FROM species WHERE id = sort), cook, consistence, flour, price, value FROM coffee
        ORDER BY id
        """).fetchall()

        labs = [tit[0] for tit in self.cur.description]
        labs[1] = "Sort"
        self.tableWidget.setColumnCount(len(labs))
        self.tableWidget.setHorizontalHeaderLabels(labs)
        self.tableWidget.setRowCount(len(result))
        for i, row in enumerate(result):
            for j in range(len(row)):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(row[j])))


if __name__ == '__main__':
    # print(CURR)
    app = QApplication(sys.argv)
    ex = ShowCoffee()
    ex.show()

    sys.exit(app.exec_())
