import sys, os;
from PyQt5.QtWidgets import QDialog;
from PyQt5 import uic;
from PyQt5.QtCore import QFile, QIODevice, QTextStream;
#from src.lib.database import DBManager;

class DBConfig(QDialog):
    nameInConfig = "";
    usernameInConfig = "";
    passwordInConfig = "";
    hostnameInConfig = "";
    portInConfig = 0;

    def __init__(self):
        super().__init__();
        self.setupUi();

    def setupUi(self):
        uic.loadUi("src/ui/dbconfig.ui", self);

        stylesheet = QFile("assets/qss/dialog.qss");
        stylesheet.open(QIODevice.ReadWrite | QIODevice.Text);
        self.setStyleSheet(QTextStream(stylesheet).readAll());

        self.port.setMinimum(1);
        self.port.setMaximum(65536);

        f = QFile("config/database.config");
        if f.open(QIODevice.ReadWrite | QIODevice.Text):

            name = f.readLine(255);
            username = f.readLine(255);
            password = f.readLine(255);
            hostname = f.readLine(255);
            port = f.readLine(1000);
            f.close();

            self.nameInConfig = str(name)[17:-3]
            self.usernameInConfig = str(username)[21:-3]
            self.passwordInConfig = str(password)[21:-3]
            self.hostnameInConfig = str(hostname)[21:-3]
            self.portInConfig = int(str(port)[17:-1])

            self.dbName.setText(self.nameInConfig);
            self.username.setText(self.usernameInConfig);
            self.password.setText(self.passwordInConfig);
            self.hostname.setText(self.hostnameInConfig);
            self.port.setValue(self.portInConfig);

        self.accept.clicked.connect(self.configure);
        self.cancel.clicked.connect(self.close);

    def configure(self):
        data = "database_name: " + self.dbName.text();
        data += "\ndatabase_username: " + self.username.text();
        data += "\ndatabase_password: " + self.password.text();
        data += "\ndatabase_hostname: " + self.hostname.text();
        data += "\ndatabase_port: " + self.port.text();

        f = QFile("config/database.config");
        f.remove("config/database.config");

        if f.open(QIODevice.ReadWrite | QIODevice.Text):
            stream = QTextStream(f);
            stream << data;
            f.close();

        self.close();

    def getName(self): return self.nameInConfig;
    def getUsername(self): return self.usernameInConfig;
    def getPassword(self): return self.passwordInConfig;
    def getHostname(self): return self.hostnameInConfig;
    def getPort(self): return self.portInConfig;

    # @decorator
    def createTables():
        db = DBManager();
