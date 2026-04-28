import sys
from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow
from database.db import buat_tabel

if __name__ == "__main__":
    app = QApplication(sys.argv)

    buat_tabel()

    with open("styles/style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())