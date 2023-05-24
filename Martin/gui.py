from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QSpacerItem, QPushButton
from PyQt6.QtCore import Qt

username = "test"


class Welcome_Label(QLabel):
    def __init__(self) -> None:
        super().__init__()
        self.setText(f"Hello {username}")
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)


class Home(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Personal Coach")
        self.tab_widget = QTabWidget()
        # home tab
        self.home_tab = QWidget()
        self.home_tab_layout = QVBoxLayout()
        # home welcome label
        self.home_welcoming = Welcome_Label()
        self.home_tab_layout.addWidget(self.home_welcoming)
        # home output trainings plan
        self.out_train_plan = QWidget()
        # out_train_plan needs to be filled with the relevant elements...
        self.home_tab_layout.addWidget(self.out_train_plan)
        # home buttons
        self.home_btns = QWidget()
        self.home_btns_layout = QHBoxLayout()
        self.home_btns_layout.addItem(QSpacerItem(0, 0))
        # button generate trainings plan
        self.home_btn_gen_plan = QPushButton("generate trainings plan")
        self.home_btns_layout.addWidget(self.home_btn_gen_plan)
        self.home_btns.setLayout(self.home_btns_layout)
        self.home_tab_layout.addWidget(self.home_btns)
        self.home_tab.setLayout(self.home_tab_layout)
        self.tab_widget.addTab(self.home_tab, "home")
        # session tab
        self.session_tab = QWidget()
        self.session_tab_layout = QVBoxLayout()
        # session welcome label
        self.session_welcoming = Welcome_Label()
        self.session_tab_layout.addWidget(self.session_welcoming)
        # session output last session
        self.out_last_session = QWidget()
        # out_last_session needs to be filled with the relevant elements...
        self.session_tab_layout.addWidget(self.out_last_session)
        # session buttons
        self.session_btns = QWidget()
        self.session_btns_layout = QHBoxLayout()
        self.session_btns_layout.addItem(QSpacerItem(0, 0))
        # button change last session
        self.session_btn_change = QPushButton("change last session")
        self.session_btns_layout.addWidget(self.session_btn_change)
        # button insert new session
        self.session_btn_insert = QPushButton("insert new session")
        self.session_btns_layout.addWidget(self.session_btn_insert)
        self.session_btns.setLayout(self.session_btns_layout)
        self.session_tab_layout.addWidget(self.session_btns)
        self.session_tab.setLayout(self.session_tab_layout)
        self.tab_widget.addTab(self.session_tab, "session")
        # params tab
        self.params_tab = QWidget()
        self.params_tab_layout = QVBoxLayout()
        # params welcome label
        self.params_welcoming = Welcome_Label()
        self.params_tab_layout.addWidget(self.params_welcoming)
        # params 2 columns
        self.params = QWidget()
        self.params_layout = QHBoxLayout()
        # params column body
        self.params_body = QWidget()
        self.params_body_layout = QVBoxLayout()
        self.out_body_params = QWidget()
        # out_body_params needs to be filled with the relevant elements...
        self.params_body_layout.addWidget(self.out_body_params)
        self.params_insert_body_params = QPushButton("insert body params")
        self.params_body_layout.addWidget(self.params_insert_body_params)
        self.params_body.setLayout(self.params_body_layout)
        self.params_layout.addWidget(self.params_body)
        self.params_goals = QWidget()
        self.params_goals_layout = QVBoxLayout()
        # missing contents params goals
        self.params_goals.setLayout(self.params_goals_layout)
        self.params_layout.addWidget(self.params_goals)
        self.params_tab_layout.addWidget(self.params)
        self.params_tab.setLayout(self.params_tab_layout)
        self.tab_widget.addTab(self.params_tab, "params")
        # other tabs
        ###
        # tab widget to central widget
        self.setCentralWidget(self.tab_widget)
        # add actions to widgets
        self.home_btn_gen_plan.clicked.connect(self.generate_trainings_plan)
        self.session_btn_change.clicked.connect(self.change_last_session)
        self.session_btn_insert.clicked.connect(self.insert_session)
        self.params_insert_body_params.clicked.connect(self.insert_body_params)

    def generate_trainings_plan(self):
        pass

    def change_last_session(self):
        pass

    def insert_session(self):
        pass

    def insert_body_params(self):
        pass


app = QApplication([])
window = Home()
window.show()
app.exec()
