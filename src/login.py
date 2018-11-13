import sys, os;
from PyQt5.QtWidgets import QDialog;
from PyQt5 import uic;
from PyQt5.QtCore import QFile, QIODevice, QTextStream;
from src.lib.database import DBManager;

class Login(QDialog):
    userData = False;

    def __init__(self):
        super().__init__();
        self.setupUi();

    def setupUi(self):
        uic.loadUi("src/ui/login.ui", self);

        stylesheet = QFile("assets/qss/login.qss");
        stylesheet.open(QIODevice.ReadWrite | QIODevice.Text);
        self.setStyleSheet(QTextStream(stylesheet).readAll());

        self.accept.clicked.connect(self.isLogged);
        self.cancel.clicked.connect(self.close);

    def isLogged(self):
        db = DBManager("127.0.0.1", "cm_test", "root", "", 3306); # Agregar funciones get para configuracion de base de datos.
        db.connect();

        if db.isValid("usuarios", "username", self.user.text()) and db.isValid("usuarios", "password", self.password.text()):
            self.userData = db.selectAllWhere("usuarios", "username = '" + self.user.text() + "'", 4);
            self.close();
            return True;
        else:
            return False;

    def getRole(self):
        return self.userData[3];
