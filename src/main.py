import sys, os;
from PyQt5.QtWidgets import QMainWindow;
from PyQt5 import uic;
from PyQt5.QtCore import QFile, QIODevice, QTextStream;
from src.database_config import DBConfig;
from src.login import Login;

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__();
        self.setupUi();

    def setupUi(self):
        login = Login();
        login.exec_();

        if login.isLogged():
            uic.loadUi("src/ui/main.ui", self);

            if   login.getRole() == "Admin":    self.views.setCurrentIndex(0);
            elif login.getRole() == "Profesor": self.views.setCurrentIndex(1);
            elif login.getRole() == "Alumno":   self.views.setCurrentIndex(2);

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

            self.showFullScreen();
            self.dbConfigAction.triggered.connect(self.dbConfigDialog);
        else:
            self.close();

    def dbConfigDialog(self):
        dbconfig = DBConfig();
        dbconfig.exec_();
