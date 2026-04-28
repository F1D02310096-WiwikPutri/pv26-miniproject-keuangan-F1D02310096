from PySide6.QtWidgets import *
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from controllers.controller import Controller
from views.form_dialog import FormDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikasi Keuangan")
        self.setGeometry(100, 100, 700, 450)

        widget = QWidget()
        self.setCentralWidget(widget)

        menubar = self.menuBar()
        menu_help = menubar.addMenu("Help")

        about_action = QAction("Tentang Aplikasi", self)
        about_action.triggered.connect(self.show_about)
        menu_help.addAction(about_action)

        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(15,15,15,15)

        self.label = QLabel("Nama: Wiwik Putri | NIM: F1D02310096")
        layout.addWidget(self.label)

        self.btn_tambah = QPushButton("Tambah")
        self.btn_tambah.setObjectName("btn_kuning")

        self.btn_hapus = QPushButton("Hapus")

        layout.addWidget(self.btn_tambah)
        layout.addWidget(self.btn_hapus)

        self.btn_edit = QPushButton("Edit")
        layout.addWidget(self.btn_edit)

        self.tabel = QTableWidget()
        self.tabel.setColumnCount(6)
        self.tabel.setHorizontalHeaderLabels(
            ["ID","Tanggal","Kategori","Jenis","Nominal","Catatan"]
        )
        self.tabel.setAlternatingRowColors(True)
        self.tabel.verticalHeader().setVisible(False)
        self.tabel.resizeColumnsToContents()

        layout.addWidget(self.tabel)

        widget.setLayout(layout)

        self.controller = Controller(self)

    def show_about(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Tentang Aplikasi")
        dialog.setFixedSize(300, 220)

        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        title = QLabel("💰 Aplikasi Keuangan")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 16px; font-weight: bold; color: #d63384;")

        desc = QLabel("Aplikasi ini digunakan untuk mencatat\npemasukan dan pengeluaran harian.")
        desc.setAlignment(Qt.AlignCenter)

        nama = QLabel("👤 Nama: Wiwik Putri")
        nim = QLabel("🎓 NIM: F1D02310096")

        btn_close = QPushButton("Tutup")
        btn_close.setObjectName("btn_kuning")
        btn_close.clicked.connect(dialog.accept)

        layout.addWidget(title)
        layout.addWidget(desc)
        layout.addWidget(nama)
        layout.addWidget(nim)
        layout.addStretch()
        layout.addWidget(btn_close)

        dialog.setLayout(layout)
        dialog.exec()

    def item(self, text):
        return QTableWidgetItem(text)

    def open_dialog(self):
        return FormDialog()

    def konfirmasi(self):
        return QMessageBox.question(self,"Konfirmasi","Hapus data?") == QMessageBox.Yes