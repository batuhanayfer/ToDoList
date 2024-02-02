import sys
from todo import Ui_MainWindow, QtWidgets
from PyQt5.QtCore import QDateTime, Qt
import datetime


class ToDoApp(Ui_MainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

        # Setup user interface
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.setupCurrentTime()

        # Initialize variables
        self.current_date_time = None
        self.minute = None
        self.hour = None
        self.day = None
        self.month = None
        self.year = None
        self.current_datetime = None

        # make local modifications
        self.ui.textEdit.keyPressEvent()

    def setupCurrentTime(self):
        self.current_datetime = datetime.datetime.now()
        self.year = self.current_datetime.year
        self.month = self.current_datetime.month
        self.day = self.current_datetime.day
        self.hour = self.current_datetime.hour
        self.minute = self.current_datetime.minute
        self.current_date_time = QDateTime(self.year, self.month, self.day, self.hour, self.minute)
        self.ui.dateTimeEdit.setDateTime(self.current_date_time)


app = QtWidgets.QApplication(sys.argv)
toDoAppUi = ToDoApp()

sys.exit(app.exec_())
