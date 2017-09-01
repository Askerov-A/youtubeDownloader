import sqlite3


def drop_table():
    with sqlite3.connect('requests.db') as connection:
        c = connection.cursor()
        c.execute("""DROP TABLE IF EXISTS requests;""")
    return True


def create_db():
    with sqlite3.connect('requests.db') as connection:
        c = connection.cursor()
        table = """CREATE TABLE requests(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            date_time INTEGER NOT NULL,
            user TEXT NOT NULL
        );
        """
        c.execute(table)
    return True


if __name__ == '__main__':
    drop_table()
    create_db()
