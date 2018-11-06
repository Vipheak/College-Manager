import sys, os;
from PyQt5.QtWidgets import QApplication, QDialog;
from PyQt5 import uic;
from PyQt5.QtCore import QFile, QIODevice, QTextStream;
from src.lib.database import DBManager;

class Login(QDialog):
    def __init__(self):
        super().__init__();
        self.setupUi();

    def setupUi(self):
        uic.loadUi("src/ui/login.ui", self);

        stylesheet = QFile("assets/qss/login.qss");
        stylesheet.open(QIODevice.ReadWrite | QIODevice.Text);
        self.setStyleSheet(QTextStream(stylesheet).readAll());

        self.accept.clicked.connect(self.login);
        self.cancel.clicked.connect(self.close);

    def login(self):
        db = DBManager("127.0.0.1", "cm_test", "root", "", 3306); # Agregar funciones get para configuracion de base dedatos.
        db.connect();

        if db.isValid("usuarios", "username", self.user.text()) and db.isValid("usuarios", "password", self.password.text()):
            userData = db.selectAllWhere("usuarios", "username = '" + self.user.text() + "'", 4);

            if(userData[3] == "Admin"):
                from src.main import MainWindow;
                self.close();
            if(userData[3] == "Profesor"):
                pass
            if(userData[3] == "Alumno"):
                pass
        else:
            pass

# __init__
a = QApplication(sys.argv);
w = Login();
w.show();
a.exec_();
