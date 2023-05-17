from PyQt6.QtWidgets import QApplication,QMainWindow
class Home(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
app=QApplication([])
window=Home()
window.show()
app.exec()
