from src.lib.database import DBManager;
from src.database_config import DBConfig;
from PyQt5.QtWidgets import QApplication;

class tablesRun():
    def __init__(self):
        dbc = DBConfig();
        dbm = DBManager(dbc.getHostname(), dbc.getName(), dbc.getUsername(), dbc.getPassword(), dbc.getPort());
        dbm.connect();

        SQL = (""
        +"CREATE TABLE USERS( "
        +"id integer(7) PRIMARY KEY NOT NULL AUTO_INCREMENT, "
        +"username varchar(20) UNIQUE, "
        +"password varchar(20) NOT NULL, "
        +"role varchar(12) NOT NULL, "
        +"name varchar(40), "
        +"firstSurname varchar(40), "
        +"secondSurname varchar(40), "
        +"email varchar(40), "
        +"phone varchar(32), "
        +"address varchar(40) "
        +"); "

        +"CREATE TABLE admins ( "
        +"admins_id integer(7) PRIMARY KEY NOT NULL, "
        +"FOREIGN KEY (admins_id) REFERENCES users(id) "
        +"); "

        +"CREATE TABLE teachers ( "
        +"teacher_id integer(7) PRIMARY KEY NOT NULL, "
        +"maestria varchar(40), "
        +"FOREIGN KEY (teacher_id) REFERENCES users(id) "
        +"); "

        +"CREATE TABLE students ( "
        +"students_id integer(7) NOT NULL, "
        +"teacher_id integer(7)  NOT NULL, "
        +"carrera varchar(40), "
        +"FOREIGN KEY (teacher_id) REFERENCES users(id), "
        +"FOREIGN KEY (students_id) REFERENCES users(id) "
        +"); "

        +"CREATE TABLE schedule ( "
        +"id integer(2) PRIMARY KEY NOT NULL AUTO_INCREMENT, "
        +"monday varchar(64), "
        +"tuesday varchar(64), "
        +"wednesday varchar(64), "
        +"thursday varchar(64), "
        +"friday varchar(64), "
        +"saturday varchar(64), "
        +"sunday varchar(64) "
        +"); ");

        dbm.query(SQL);

        dbm.insert("users", (
            ("username", "Owner"),
            ("password", "Renwo"),
            ("role", "Admin"),
            ("name", "Owner"),
            ("firstSurname", ""),
            ("secondSurname", ""),
            ("email", "Owner@email.com"),
            ("phone", "5555555555"),
            ("address", "Owner Residence s.t.")
        ));

        for i in range(0, 14):
            dbm.insert("schedule", (
                ("monday", ""),
                ("tuesday", ""),
                ("wednesday", ""),
                ("thursday", ""),
                ("friday", ""),
                ("saturday", ""),
                ("sunday", "")
            ));
