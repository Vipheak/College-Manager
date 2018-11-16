import sys, os;
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem;
from PyQt5 import uic;
from src.database_config import DBConfig;
from src.login import Login;
from src.lib.database import DBManager;

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__();
        self.setupUi();

    def setupUi(self):
        login = Login();
        login.exec_();

        if login.isLogged():
            if login.getRole() == "Alumno": uic.loadUi("src/ui/main.ui", self);
            elif login.getRole() == "Profesor": uic.loadUi("src/ui/main.ui", self);
            elif login.getRole() == "Admin":
                uic.loadUi("src/ui/Administrador.ui", self);
                self.userManagerBtn.clicked.connect(self.userManagerClicked);
                self.scheduleBtn.clicked.connect(self.scheduleClicked);

            self.showFullScreen();
            self.dbConfigAction.triggered.connect(self.dbConfigDialog);
        else:
            self.close();

    def dbConfigDialog(self):
        dbconfig = DBConfig();
        dbconfig.exec_();

    def userManagerClicked(self):
        self.views.setCurrentIndex(0);
        self.tableUsers.setColumnCount(4);
        self.tableUsers.setHorizontalHeaderLabels(["id", "usuario", "contraseña", "rol"]);

        dbc = DBConfig();
        db = DBManager(dbc.getHostname(), dbc.getName(), dbc.getUsername(), dbc.getPassword(), dbc.getPort());

        values = db.select("usuarios", 4);
        row = 0;

        for value in values:
            self.tableUsers.insertRow(row);
            id = QTableWidgetItem(value[0]); self.tableUsers.setItem(row, 0, id);
            username = QTableWidgetItem(value[1]); self.tableUsers.setItem(row, 1, username);
            password = QTableWidgetItem(value[2]); self.tableUsers.setItem(row, 2, password);
            role = QTableWidgetItem(value[3]); self.tableUsers.setItem(row, 3, role);
            row += 1;

    def addUser(self):
        pass

    def scheduleClicked(self): self.views.setCurrentIndex(1);
