from lib.database import DBManager;
from database_config import DBConfig;
from PyQt5.QtWidgets import QApplication;

class tablesRun():
    def __init__(self):
        dbc = DBConfig();
        dbm = DBManager(dbc.getHostname(), dbc.getName(), dbc.getUsername(), dbc.getPassword(), dbc.getPort());
        dbm.connect();

        # SQL

        CREATE TABLE users (
          id
          username
          password
          name
          firstSurname
          secondSurname
          email
          phone
          address
          role
        );

        CREATE TABLE admins (

        );

        CREATE TABLE teachers (

        );

        CREATE TABLE students (

        );

        # SQL

import sys;
a = QApplication(sys.argv);
run = tablesRun();
