import sqlite3

def main():
    print('connect..')
    db = sqlite3.connect('db-api.db')
    cur = db.cursor()
    print('create')