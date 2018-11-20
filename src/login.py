import sys, os;
from PyQt5.QtWidgets import QDialog;
from PyQt5 import uic;
from PyQt5.QtCore import QFile, QIODevice, QTextStream;
from src.lib.database import DBManager;
from src.database_config import DBConfig;
from src.create_tables import tablesRun;

class Login(QDialog):
    userData = None;

    def __init__(self):
        super().__init__();
        self.checkFirstLogin();
        self.setupUi();

    def setupUi(self):
        uic.loadUi("src/ui/login.ui", self);

        stylesheet = QFile("assets/qss/login.qss");
        stylesheet.open(QIODevice.ReadWrite | QIODevice.Text);
        self.setStyleSheet(QTextStream(stylesheet).readAll());

        self.accept.clicked.connect(self.isLogged);
        self.cancel.clicked.connect(self.close);

    def isLogged(self):
        dbconfig = DBConfig();
        db = DBManager(dbconfig.getHostname(), dbconfig.getName(), dbconfig.getUsername(), dbconfig.getPassword(), dbconfig.getPort());
        db.connect();

        if db.isValid("users", "username", self.user.text()) and db.isValid("users", "password", self.password.text()):
            self.userData = db.selectAllWhere("users", "username = '" + self.user.text() + "'", 9);
            self.close();
            return True;
        else:
            return False;

    def getId(self): return self.userData[0];
    def getFullName(self): return str(self.userData[4]) + " " + str(self.userData[5]) + " " + str(self.userData[6]);
    def getRole(self): return self.userData[3];

    def checkFirstLogin(self):
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

            dbconfig = DBConfig();
            dbconfig.exec_();

            createTables = tablesRun();
