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

                self.nID.setText(str(login.getId()));
                self.name.setText(login.getFullName());

                self.userManagerBtn.clicked.connect(self.userManagerClicked);
                self.scheduleBtn.clicked.connect(self.scheduleClicked);
                self.addUserBtn.clicked.connect(self.addUserClicked);
                self.acceptAddUser.clicked.connect(self.addUser);

            self.showFullScreen();
            self.dbConfigAction.triggered.connect(self.dbConfigDialog);
        else:
            self.close();

    def dbConfigDialog(self):
        dbconfig = DBConfig();
        dbconfig.exec_();

    def userManagerClicked(self):
        self.views.setCurrentIndex(0);
        self.tableUsers.setColumnCount(10);
        self.tableUsers.setHorizontalHeaderLabels([
            "id",
            "usuario",
            "contraseña",
            "rol", "nombre",
            "apellido paterno",
            "apellido materno",
            "email",
            "telefono",
            "direccion"
        ]);

        dbc = DBConfig();
        db = DBManager(dbc.getHostname(), dbc.getName(), dbc.getUsername(), dbc.getPassword(), dbc.getPort());

        values = db.select("users", 10);
        row = 0;

        for value in values:
            self.tableUsers.insertRow(row);

            id = QTableWidgetItem(str(value[0])); self.tableUsers.setItem(row, 0, id);
            username = QTableWidgetItem(value[1]); self.tableUsers.setItem(row, 1, username);
            password = QTableWidgetItem(value[2]); self.tableUsers.setItem(row, 2, password);
            role = QTableWidgetItem(value[3]); self.tableUsers.setItem(row, 3, role);
            name = QTableWidgetItem(value[4]); self.tableUsers.setItem(row, 4, name);
            firstSurname = QTableWidgetItem(value[5]); self.tableUsers.setItem(row, 5, firstSurname);
            secondSurname = QTableWidgetItem(value[6]); self.tableUsers.setItem(row, 6, secondSurname);
            email = QTableWidgetItem(value[7]); self.tableUsers.setItem(row, 7, email);
            phone = QTableWidgetItem(str(value[8])); self.tableUsers.setItem(row, 8, phone);
            address = QTableWidgetItem(value[9]); self.tableUsers.setItem(row, 9, address);

            row += 1;

    def addUserClicked(self): self.views.setCurrentIndex(2);

    def addUser(self):
        dbc = DBConfig();
        dbm = DBManager(dbc.getHostname(), dbc.getName(), dbc.getUsername(), dbc.getPassword(), dbc.getPort());

        if self.roleCB.currentIndex() == 0: role = "Student";
        if self.roleCB.currentIndex() == 1: role = "Teacher";
        if self.roleCB.currentIndex() == 2: role = "Admin";

        dbm.insert("users", (
            ("username", self.usernameLE.text()),
            ("password", self.passwordLE.text()),
            ("role", role),
            ("name", self.nameLE.text()),
            ("firstSurname", self.firstSurnameLE.text()),
            ("secondSurname", self.secondSurnameLE.text()),
            ("email", self.emailLE.text()),
            ("phone", self.phoneLE.text()),
            ("address", self.addressTE.toPlainText())
        ));

        self.views.setCurrentIndex(0);

    def scheduleClicked(self): self.views.setCurrentIndex(1);
