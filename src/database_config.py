import sys, os;
from PyQt5.QtWidgets import QDialog;
from PyQt5 import uic;
from PyQt5.QtCore import QFile, QIODevice, QTextStream;

class DBConfig(QDialog):
    def __init__(self):
        super().__init__();
        self.setupUi();

    def setupUi(self):
        uic.loadUi("src/ui/dbconfig.ui", self);
        #uic.loadUi(os.path.dirname(os.path.realpath(sys.argv[0])) + "/ui/dbconfig.ui", self);

        stylesheet = QFile("assets/qss/dialog.qss");
        stylesheet.open(QIODevice.ReadWrite | QIODevice.Text);
        self.setStyleSheet(QTextStream(stylesheet).readAll());

        self.port.setMinimum(1);
        self.port.setMaximum(65536);

        f = QFile("config/database.config");
        if f.open(QIODevice.ReadWrite | QIODevice.Text):

            # FIX ME : START :
            name = f.readLine(255);
            username = f.readLine(255);
            password = f.readLine(255); # ValueError: invalid literal for int() with base 10: ''
            hostname = f.readLine(255);
            port = f.readLine(21);
            f.close();

            self.dbName.setText(str(name)[17:-3]);
            self.username.setText(str(username)[21:-3]);
            self.password.setText(str(password)[21:-3]); #V alueError: invalid literal for int() with base 10: ''
            self.hostname.setText(str(hostname)[21:-3]);
            self.port.setValue(int(str(port)[17:-3]));
            # FIX ME : END

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
