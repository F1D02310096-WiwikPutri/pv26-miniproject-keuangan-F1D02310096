from database.db import tambah_data, ambil_data, hapus_data, update_data
from PySide6.QtCore import Qt
from views.form_dialog import FormDialog

class Controller:
    def __init__(self, ui):
        self.ui = ui
        self.load_data()

        self.ui.btn_tambah.clicked.connect(self.tambah)
        self.ui.btn_hapus.clicked.connect(self.hapus)
        self.ui.btn_edit.clicked.connect(self.edit)

    def load_data(self):
        data = ambil_data()
        self.ui.tabel.setRowCount(0)

        for row_data in data:
            row = self.ui.tabel.rowCount()
            self.ui.tabel.insertRow(row)

            for col, val in enumerate(row_data):
                if val is None:
                    val = ""

                item = self.ui.item(str(val))

                if col == 3:
                    if val == "Pemasukan":
                        item.setForeground(Qt.darkGreen)
                    else:
                        item.setForeground(Qt.red)

                self.ui.tabel.setItem(row, col, item)

        from PySide6.QtWidgets import QHeaderView
        self.ui.tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def tambah(self):
        dialog = self.ui.open_dialog()
        if dialog.exec():
            data = dialog.get_data()
            if data:
                tambah_data(data)
                self.load_data()

    def hapus(self):
        row = self.ui.tabel.currentRow()
        if row == -1:
            return

        id_data = int(self.ui.tabel.item(row, 0).text())

        if self.ui.konfirmasi():
            hapus_data(id_data)
            self.load_data()

    def edit(self):
        row = self.ui.tabel.currentRow()
        if row == -1:
            return

        data = []
        for col in range(self.ui.tabel.columnCount()):
            item = self.ui.tabel.item(row, col)
            data.append(item.text() if item else "")

        dialog = FormDialog(data)

        if dialog.exec():
            new_data = dialog.get_data()
            if new_data:
                id_data = int(data[0])
                update_data(id_data, new_data)
                self.load_data()