from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QSpacerItem, QPushButton, QSizePolicy
from PyQt6.QtCore import Qt

username = "test"


class Home(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Personal Coach")
        self.tab_widget = QTabWidget()
        self.label_welcoming = QLabel(f"Hello {username}")
        self.label_welcoming.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # label_welcoming will be visible on all tabs
        self.home_tab = QWidget()
        self.home_tab_layout = QVBoxLayout()
        self.home_tab_layout.addWidget(self.label_welcoming)
        self.out_train_plan = QWidget()
        # out_train_plan needs to be filled with the relevant elements...
        self.home_tab_layout.addWidget(self.out_train_plan)
        self.home_btns = QWidget()
        self.home_btns_layout = QHBoxLayout()
        self.home_btns_layout.addItem(QSpacerItem(0, 0))
        self.home_btn_gen_plan = QPushButton("generate trainings plan")
        self.home_btns_layout.addWidget(self.home_btn_gen_plan)
        self.home_btns.setLayout(self.home_btns_layout)
        self.home_tab_layout.addWidget(self.home_btns)
        self.home_tab.setLayout(self.home_tab_layout)
        self.tab_widget.addTab(self.home_tab, "home")
        # other tabs
        self.setCentralWidget(self.tab_widget)
        self.home_btn_gen_plan.clicked.connect(self.generate_trainings_plan)

    def generate_trainings_plan(self, event):
        # action generate trainingsplan
        pass


app = QApplication([])
window = Home()
window.show()
app.exec()
