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
                self.updateUserBtn.clicked.connect(self.EditUser);
                self.deleteUserBtn.clicked.connect(self.DelUser);
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
            self.userManagerBtn.setEnabled(False);
            #self.close();

    def addUserClicked(self): 
    	self.views.setCurrentIndex(2);
    	while(self.tableUsers.rowCount() > 0):
    		self.tableUsers.removeRow(0);
    	self.userManagerBtn.setEnabled(True);

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
        #dbm.close();
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
        values = dbm.select("users", 10);
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
            self.userManagerBtn.setEnabled(False);

        self.views.setCurrentIndex(0);

  

    def scheduleClicked(self): 
    	self.userManagerBtn.setEnabled(True);
    	while (self.tableUsers.rowCount() > 0):
    		self.tableUsers.removeRow(0);

    	self.views.setCurrentIndex(1);
    	#vista para checar horarios es el Index 1
    #def UpdateUser(self):
    def EditUser(self):
    	dbc = DBConfig()
    	dbm = DBManager(dbc.getHostname(), dbc.getName(), dbc.getUsername(), dbc.getPassword(), dbc.getPort())

    	column = self.tableUsers.currentColumn()
    	row = self.tableUsers.currentRow()
    	id = self.tableUsers.item(row,0).text()
    	value = self.tableUsers.currentItem().text()


    	dbm.update("users",(
    		("username", self.tableUsers.item(row,1).text()),
            ("password", self.tableUsers.item(row,2).text()),
            ("role",self.tableUsers.item(row,3).text()),
            ("name", self.tableUsers.item(row,4).text()),
            ("firstSurname", self.tableUsers.item(row,5).text()),
            ("secondSurname", self.tableUsers.item(row,6).text()),
            ("email", self.tableUsers.item(row,7).text()),
            ("phone", self.tableUsers.item(row,8).text()),
            ("address", self.tableUsers.item(row,9).text())
            ),id);

    def DelUser(self):
    	dbc = DBConfig()
    	dbm = DBManager(dbc.getHostname(), dbc.getName(), dbc.getUsername(), dbc.getPassword(), dbc.getPort())
    	column = self.tableUsers.currentColumn()
    	row = self.tableUsers.currentRow()
    	id = self.tableUsers.item(row,0).text()
    	self.tableUsers.removeRow(row);
    	dbm.delete("users",id);