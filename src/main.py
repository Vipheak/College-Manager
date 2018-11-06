import sys, os;
from PyQt5.QtWidgets import QApplication, QMainWindow;
from PyQt5 import uic;
from src.database_config import DBConfig;
from PyQt5.QtCore import QFile, QIODevice, QTextStream;

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__();
        self.setupUi();

    def setupUi(self):
        uic.loadUi("src/ui/main.ui", self);

        self.views.setCurrentIndex(0);

        f = QFile("config/global.config");
        if f.open(QIODevice.ReadWrite | QIODevice.Text):
            isFirstLogin = str(f.readLine())[18:-3] == "True";
            f.close();

        if isFirstLogin:
            f.remove("config/global.config");
            if f.open(QIODevice.ReadWrite | QIODevice.Text):

                stream = QTextStream(f);
                stream << "is_first_login: False";

                f.close();

            self.dbConfigDialog();

        self.dbConfigAction.triggered.connect(self.dbConfigDialog);

    def dbConfigDialog(self):
        dbconfig = DBConfig();
        dbconfig.exec_();

# __init__
a = QApplication(sys.argv);
w = MainWindow();
w.showFullScreen();
a.exec_();
