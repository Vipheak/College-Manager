import hashlib
import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery;
import mysql.connector;
from src.database_config import DBConfig;

def make_pw_hash(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_pw_hash (password, hash):
    if make_pw_hash(password) == hash:
        return True

    return False

print("contrasenia: " + password);
pwHah=make_pw_hash(password);
print("Hash: " + str(pwHash));

if check_pw_hash(password, pwHash):
        print("El hash es correcto");
       else:
        print("El hash es incorrecto");



