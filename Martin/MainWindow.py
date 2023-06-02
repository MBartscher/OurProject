from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QLabel,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QSpacerItem,
    QPushButton,
    QFrame,
    QDialog,
    QSizePolicy,
)
from PyQt6.QtCore import Qt
from dialog_insert_session import Ui_Dialog as Ui_Dialog_insert_session
from dialog_insert_unit import Ui_Dialog as Ui_Dialog_insert_unit

username = "test"
output_goals = "goal1\ngoal2\ngoal3\ngoal4"


class Button_Container(QWidget):
    def __init__(self):
        super().__init__()
        self.size_polizy = QSizePolicy()
        self.size_polizy.setHorizontalPolicy(QSizePolicy.Policy.Minimum)
        self.size_polizy.setVerticalPolicy(QSizePolicy.Policy.Fixed)
        self.setSizePolicy(self.size_polizy)


class Buttons(QPushButton):
    def __init__(self, text: str) -> None:
        super().__init__()
        self.size_polizy = QSizePolicy()
        self.size_polizy.setHorizontalPolicy(QSizePolicy.Policy.Fixed)
        self.size_polizy.setVerticalPolicy(QSizePolicy.Policy.Fixed)
        self.setSizePolicy(self.size_polizy)
        self.setText(text)


class Dialog_insert_unit(QDialog, Ui_Dialog_insert_unit):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.accepted.connect(self.accept)
        # self.rejected.connect(self.reject)

    def accept(self) -> None:
        super().accept()
        pass

    # def reject(self):
    #     super().reject()
    #     pass


class Dialog_insert_session(QDialog, Ui_Dialog_insert_session):
    def __init__(self, change: bool = False):
        super().__init__()
        self.setupUi(self)
        self.__change = change
        self.btn_insert_unit.clicked.connect(self.insert_unit)
        self.accepted.connect(self.accept)
        # self.rejected.connect(self.reject)

    def insert_unit(self):
        dialog_insert_unit = Dialog_insert_unit()
        dialog_insert_unit.exec()

    def accept(self):
        super().accepted()
        if self.__change:
            pass
        else:
            pass

    # def reject(self):
    #     super().reject()
    #     pass


class Welcome_Label(QLabel):
    def __init__(self) -> None:
        super().__init__()
        self.setText(f"Hello {username}")
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.size_policy = QSizePolicy()
        self.size_policy.setHorizontalPolicy(QSizePolicy.Policy.Minimum)
        self.size_policy.setVerticalPolicy(QSizePolicy.Policy.Fixed)
        self.setSizePolicy(self.size_policy)


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
        self.home_title_train_plan = QLabel("Trainingsplan")
        self.home_tab_layout.addWidget(self.home_title_train_plan)
        self.out_train_plan = QWidget()
        # out_train_plan needs to be filled with the relevant elements...
        self.home_tab_layout.addWidget(self.out_train_plan)
        # home buttons
        self.home_btns = Button_Container()
        self.home_btns_layout = QHBoxLayout()
        self.home_btns_layout.addItem(QSpacerItem(0, 0))
        # button generate trainings plan
        self.home_btn_gen_plan = Buttons("generate trainings plan")
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
        # session output last
        self.session_title_out_last = QLabel("last session")
        self.session_tab_layout.addWidget(self.session_title_out_last)
        self.out_last_session = QWidget()
        # out_last_session needs to be filled with the relevant elements...
        self.session_tab_layout.addWidget(self.out_last_session)
        # session buttons
        self.session_btns = Button_Container()
        self.session_btns_layout = QHBoxLayout()
        self.session_btns_layout.addItem(QSpacerItem(0, 0))
        # button change last session
        self.session_btn_change = Buttons("change last session")
        self.session_btns_layout.addWidget(self.session_btn_change)
        # button insert new session
        self.session_btn_insert = Buttons("insert new session")
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
        # params titles
        self.params_titles = QWidget()
        self.params_titles_layout = QHBoxLayout()
        self.params_title_body = QLabel("last body params")
        self.params_titles_layout.addWidget(self.params_title_body)
        self.params_title_goals = QLabel("selected goals")
        self.params_titles_layout.addWidget(self.params_title_goals)
        self.params_titles.setLayout(self.params_titles_layout)
        self.params_tab_layout.addWidget(self.params_titles)
        # params outputs
        self.params_outputs = QWidget()
        self.params_outputs_layout = QHBoxLayout()
        self.out_body_params = QWidget()
        self.params_outputs_layout.addWidget(self.out_body_params)
        self.out_goals = QLabel(output_goals)
        self.out_goals.setFrameShape(QFrame.Shape.Box)
        self.params_outputs_layout.addWidget(self.out_goals)
        self.params_outputs.setLayout(self.params_outputs_layout)
        self.params_tab_layout.addWidget(self.params_outputs)
        # params btns
        self.params_btns = Button_Container()
        self.params_btns_layout = QHBoxLayout()
        self.params_btn_insert_body = Buttons("insert body params")
        self.params_btns_layout.addWidget(self.params_btn_insert_body)
        self.params_btn_change_goals = Buttons("change goals")
        self.params_btns_layout.addWidget(self.params_btn_change_goals)
        self.params_btns.setLayout(self.params_btns_layout)
        self.params_tab_layout.addWidget(self.params_btns)
        self.params_tab.setLayout(self.params_tab_layout)
        self.tab_widget.addTab(self.params_tab, "params")
        # user tab
        self.user_tab = QWidget()
        self.user_tab_layout = QVBoxLayout()
        # user welcome label
        self.user_welcoming = Welcome_Label()
        self.user_tab_layout.addWidget(self.user_welcoming)
        # user buttons
        self.user_btns = Button_Container()
        self.user_btns_layout = QHBoxLayout()
        self.user_btn_change_user = Buttons("change user")
        self.user_btns_layout.addWidget(self.user_btn_change_user)
        self.user_btn_new_user = Buttons("new user")
        self.user_btns_layout.addWidget(self.user_btn_new_user)
        self.user_btn_delete_user = Buttons("delete user")
        self.user_btns_layout.addWidget(self.user_btn_delete_user)
        self.user_btns.setLayout(self.user_btns_layout)
        self.user_tab_layout.addWidget(self.user_btns)
        self.user_tab.setLayout(self.user_tab_layout)
        self.tab_widget.addTab(self.user_tab, "user")
        # tab widget to central widget
        self.setCentralWidget(self.tab_widget)
        # add actions to widgets
        self.home_btn_gen_plan.clicked.connect(self.generate_trainings_plan)
        self.session_btn_change.clicked.connect(self.change_last_session)
        self.session_btn_insert.clicked.connect(self.insert_session)
        self.params_btn_insert_body.clicked.connect(self.insert_body_params)
        self.params_btn_change_goals.clicked.connect(self.change_goals)
        self.user_btn_change_user.clicked.connect(self.change_user)
        self.user_btn_new_user.clicked.connect(self.new_user)
        self.user_btn_delete_user.clicked.connect(self.delete_user)

    def generate_trainings_plan(self):
        pass

    def change_last_session(self):
        dialog_insert_session = Dialog_insert_session(change=True)
        dialog_insert_session.setWindowTitle("change session")
        dialog_insert_session.exec()

    def insert_session(self):
        dialog_insert_session = Dialog_insert_session()
        dialog_insert_session.exec()

    def insert_body_params(self):
        pass

    def change_goals(self):
        pass

    def change_user(self):
        pass

    def new_user(self):
        pass

    def delete_user(self):
        pass


app = QApplication([])
window = Home()
window.show()
app.exec()
