import sys, os;
from PyQt5.QtWidgets import QMainWindow;
from PyQt5 import uic;
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

            if   login.getRole() == "Alumno":    self.views.setCurrentIndex(0);
            elif login.getRole() == "Profesor": self.views.setCurrentIndex(1);
            elif login.getRole() == "Admin":   self.views.setCurrentIndex(2);

            self.showFullScreen();
            self.dbConfigAction.triggered.connect(self.dbConfigDialog);
        else:
            self.close();

    def dbConfigDialog(self):
        dbconfig = DBConfig();
        dbconfig.exec_();
