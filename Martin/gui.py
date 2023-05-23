from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QSpacerItem, QPushButton, QSizePolicy
from PyQt6.QtCore import Qt

username = "test"

# class welcome_label?! -> creating object of it in tabs!


class Home(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Personal Coach")
        self.tab_widget = QTabWidget()
        # home tab
        self.home_tab = QWidget()
        self.home_tab_layout = QVBoxLayout()
        self.welcoming_at_user = QLabel(text=f"Hello {username}")
        self.welcoming_at_user.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.home_tab_layout.addWidget(self.welcoming_at_user)
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
        # session tab
        self.session_tab = QWidget()
        self.session_tab_layout = QVBoxLayout()
        self.welcoming_at_session = QLabel(text=f"Hello {username}")
        self.welcoming_at_session.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.session_tab_layout.addWidget(self.welcoming_at_session)
        self.out_last_session = QWidget()
        # out_last_session needs to be filled with the relevant elements...
        self.session_tab_layout.addWidget(self.out_last_session)
        self.session_btns = QWidget()
        self.session_btns_layout = QHBoxLayout()
        self.session_btns_layout.addItem(QSpacerItem(0, 0))
        self.session_btn_change = QPushButton("change last session")
        self.session_btns_layout.addWidget(self.session_btn_change)
        self.session_btn_insert = QPushButton("insert new session")
        self.session_btns_layout.addWidget(self.session_btn_insert)
        self.session_btns.setLayout(self.session_btns_layout)
        self.session_tab_layout.addWidget(self.session_btns)
        self.session_tab.setLayout(self.session_tab_layout)
        self.tab_widget.addTab(self.session_tab, "session")
        # other tabs
        self.setCentralWidget(self.tab_widget)
        self.home_btn_gen_plan.clicked.connect(self.generate_trainings_plan)
        self.session_btn_change.clicked.connect(self.change_last_session)
        self.session_btn_insert.clicked.connect(self.insert_session)

    def generate_trainings_plan(self):
        # action generate trainingsplan
        pass

    def change_last_session(self):
        # action change last session
        pass

    def insert_session(self):
        # action insert session
        pass


app = QApplication([])
window = Home()
window.show()
app.exec()
