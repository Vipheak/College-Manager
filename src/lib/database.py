import sys;
from PyQt5.QtSql import QSqlDatabase;
import mysql.connector;

class Manager(QSqlDatabase):
    def __init__(self, hostname, name, username, password, port):
        self.db = super().addDatabase("QMYSQL");
        self.db.setHostName(hostname);
        self.db.setDatabaseName(name);
        self.db.setUserName(username);
        self.db.setPassword(password);
        self.db.setPort(port);
        self.ok = self.db.open();

    def isConnected(self): return self.ok;
