import sqlite3

def connect():
    con = sqlite3.connect('books.db')
    cur = con.cursor()
    return con, cur

def close(con):
    con.commit()
    con.close()

def create():
    con, cur = connect()
    cur.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, \
                title text, author text, year integer, isbn integer)')
    close(con)

def insert(title, author, year, isbn):
    con, cur = connect()
    cur.execute(f"INSERT INTO books VALUES(NULL,'{title}','{author}',\
                {year},{isbn})")
    close(con)

def viewAll():
    con, cur = connect()
    cur.execute('SELECT * FROM books')
    rows = cur.fetchall()
    close(con)
    return rows

def search(title="",author="",year="",isbn=""):
    con, cur = connect()
    cur.execute(f"SELECT * FROM books WHERE title= '{title}' OR \
                author='{author}' OR year='{year}' OR isbn='{isbn}'")
    rows = cur.fetchall()
    close(con)
    return rows

def update(id,title,author,year,isbn):
    con, cur = connect()
    cur.execute(f"UPDATE books SET title = '{title}', author ='{author}',\
                 year = {year}, isbn = {isbn} WHERE id = {id}")
    close(con)

def delete(id):
    con, cur = connect()
    cur.execute(f"DELETE FROM books WHERE id = {id}")
    close(con)

create()
# insert('A','B',10,1)
# insert('C','D',8,2)
# insert('E','F',6,3)
# insert('G','H',100,4)
# insert('I','J',20,5)
# print(viewAll())
# print(search(title='I'))
# update(6,'K','L',150,7)
# delete(10)
# print(viewAll())