from api import read, write
from PyQt6.QtWidgets import * # type: ignore
import sys


class MainWindow(QMainWindow):
    def __init__(self, data: dict) -> None:
        super().__init__()
        self.setWindowTitle("gym-tracker")
        content = QVBoxLayout() #everything will be arranged in here

        
        #the buttons on the top
        top_buttons = QHBoxLayout()
        new_entry_button = QPushButton("New Entry")
        new_entry_button.clicked.connect(self.new_entry)
        top_buttons.addWidget(new_entry_button)
        #############################
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save)
        top_buttons.addWidget(save_button)
        content.addLayout(top_buttons)



        #make the rows for the data display
        self.rows = QVBoxLayout()
        for i in data:
            columns = QHBoxLayout()
            field = QLineEdit(i.replace("_", " ").title())
            columns.addWidget(field)
            for j in data[i]:
                field = QLineEdit(str(data[i][j]))
                columns.addWidget(field)
            wgt = QWidget()
            wgt.setLayout(columns)
            self.rows.addWidget(wgt)
        content.addLayout(self.rows)
        
    
        container = QWidget()
        container.setLayout(content)
        self.setCentralWidget(container)
    

    def new_entry(self):
        columns = QHBoxLayout()
        texts = ["Exercise", "Weight", "Repetitions"]
        for j in texts:
            field = QLineEdit()
            field.setPlaceholderText(j)
            columns.addWidget(field)
        wgt = QWidget()
        wgt.setLayout(columns)
        self.rows.addWidget(wgt)
    
    def save(self):
        pass

        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow(read("data.json"))
    window.show()

    app.exec()