from PySide6.QtWidgets import *
from PySide6.QtCore import QDate

class FormDialog(QDialog):
    def __init__(self, data=None):
        super().__init__()

        self.setWindowTitle("Tambah / Edit Data")
        self.data_lama = data

        layout = QVBoxLayout()

        self.tanggal = QDateEdit()
        self.tanggal.setDisplayFormat("dd/MM/yyyy")

        self.jenis = QComboBox()
        self.jenis.addItems(["Pemasukan","Pengeluaran"])

        self.kategori = QComboBox()
        self.update_kategori()
        self.jenis.currentTextChanged.connect(self.update_kategori)

        self.nominal = QLineEdit()
        self.catatan = QTextEdit()

        self.btn_simpan = QPushButton("Simpan")
        self.btn_simpan.clicked.connect(self.accept)

        layout.addWidget(self.tanggal)
        layout.addWidget(self.jenis)
        layout.addWidget(self.kategori)
        layout.addWidget(self.nominal)
        layout.addWidget(self.catatan)
        layout.addWidget(self.btn_simpan)

        self.setLayout(layout)

        if data:
            self.tanggal.setDate(QDate.fromString(data[1], "dd/MM/yyyy"))
            self.jenis.setCurrentText(data[3])
            self.update_kategori()
            self.kategori.setCurrentText(data[2])
            self.nominal.setText(str(data[4]))
            self.catatan.setText(data[5])

    def update_kategori(self):
        self.kategori.clear()
        if self.jenis.currentText() == "Pemasukan":
            self.kategori.addItems(["Gaji","Bonus","Freelance","Lainnya"])
        else:
            self.kategori.addItems(["Makan","Transport","Belanja","Hiburan","Tagihan","Kesehatan","Lainnya"])

    def get_data(self):
        if self.nominal.text() == "":
            QMessageBox.warning(self, "Error", "Nominal harus diisi!")
            return None

        return (
            self.tanggal.text(),
            self.kategori.currentText(),
            self.jenis.currentText(),
            int(self.nominal.text()),
            self.catatan.toPlainText()
        )