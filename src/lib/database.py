import sys;
from PyQt5.QtSql import QSqlDatabase, QSqlQuery;
import mysql.connector;

class DBManager(QSqlDatabase):
    db = None;
    ok = False;

    def __init__(self, hostname, name, username, password, port):
        super().__init__();
        self.hostname = hostname;
        self.name = name;
        self.username = username;
        self.password = password;
        self.port = port;

    def connect(self):
        self.db = super().addDatabase("QMYSQL");
        self.db.setHostName(self.hostname);
        self.db.setDatabaseName(self.name);
        self.db.setUserName(self.username);
        self.db.setPassword(self.password);
        self.db.setPort(self.port);
        self.ok = self.db.open();

    def insert(self, table, values):
        sql = "INSERT INTO " + table + "(";
        for value in values: sql += str(value[0]) + ", ";
        sql = sql[:-2]; sql += ") VALUES(:";
        for value in values: sql += str(value[0]) + ", :";
        sql =sql[:-3]; sql += ")";

        query = QSqlQuery();
        query.prepare(sql);
        for value in values: query.bindValue(":"+value[0], value[1]);
        query.exec_();

    def select(self, table, nrows):
        sql = "SELECT * FROM " + table;
        query = QSqlQuery(sql);
        list = [];

        while query.next():
            listaux = [];
            for i in range(nrows): listaux.append(query.value(i));
            list.append(tuple(listaux));

        return tuple(list);

    def selectAllWhere(self, table, condition, nrows):
        sql = "SELECT * FROM " + table + " WHERE " + condition;
        query = QSqlQuery(sql);
        list = [];
        query.next();

        for i in range(nrows):
            list.append(query.value(i));

        return tuple(list);

    def update(self, table, values, id):
        sql = "UPDATE " + table + " SET "
        for value in values: sql += str(value[0]) + " = :" +str(value[0]) + ", ";
        sql = sql[:-2]; sql += " WHERE id = :id"

        query = QSqlQuery();
        query.prepare(sql);
        for value in values: query.bindValue(":"+value[0], value[1]);
        query.bindValue(":id", id);
        query.exec_();

    def delete(self, table, id):
        sql = "DELETE FROM " +  table + " WHERE id = :id";
        query = QSqlQuery();
        query.prepare(sql);
        query.bindValue(":id", id);
        query.exec_();

    def isValid(self, table, rowName, value):
        sql = "SELECT " + rowName + " FROM " +  table + " WHERE " + rowName + " = :value";

        query = QSqlQuery();
        query.prepare(sql);
        query.bindValue(":value", value);
        query.exec_();
        query.next();

        return value == query.value(0);

    def close(self):
        self.db.close();
        self.ok = False;

    def isConnected(self): return self.ok;

#db = DBManager("127.0.0.1", "cm_test", "root", "", 3306);
#db.connect();
