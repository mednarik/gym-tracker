from api import read, write
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("gym-tracker")
        
        rows = QVBoxLayout()
        
        for i in range(3):
            columns = QHBoxLayout()
            for j in range(3):
                columns.addWidget(QLineEdit())
            wgt = QWidget()
            wgt.setLayout(columns)
            rows.addWidget(wgt)
        
        
        
        container = QWidget()
        container.setLayout(rows)
        self.setCentralWidget(container)
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()