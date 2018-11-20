from lib.database import DBManager;
from database_config import DBConfig;
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
        +"phone integer(10), "
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
        +"); ");

        dbm.query(SQL);
