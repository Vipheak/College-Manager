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

def capa_seguridad (key, hash):
    key: b
    cif == hash
    for index, val in enumerate (hash)
    c = ord(val) ^ ord(key[0])
    cif += str(chr(c))
    return cif
