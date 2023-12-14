import psycopg2

# ex. 1
DATABASE = 'database1488'
USER = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '55566'

connection = psycopg2.connect(
    database=DATABASE,
    user=USER,
    host=HOST,
    password=PASSWORD,
    port=PORT,
)

cursor = connection.cursor()

# ex. 2
cursor.execute(
    """CREATE TABLE IF NOT EXISTS goods(
        id SERIAL PRIMARY KEY,
        title VARCHAR (150) NOT NULL,
        price INTEGER NOT NULL,
        warranty_period_days INTEGER
    );"""
)

# ex. 3
# cursor.execute(
#     """INSERT INTO goods(title, price, warranty_period_days) VALUES('Banana', 15, 13);"""
# )

connection.commit()
cursor.close()
connection.close()

# ex. 4
# cursor.execute('select * from goods where price > 50;')
# result = cursor.fetchall()
# print(result)

# ex. 5
# cursor.execute('select * from goods where warranty_period_days = 20;')
# result = cursor.fetchall()
# print(result)

# ex. 6
# cursor.execute("select * from goods where title ilike '%without sugar';")
# result = cursor.fetchall()
# print(result)

# ex. 7
# cursor.execute("select id, title from goods order by id limit 3;")
# result = cursor.fetchall()
# print(result)

# ex. 8
# cursor.execute("select id, title from goods order by id limit 3 offset 3;")
# result = cursor.fetchall()
# print(result)
