import psycopg2
import json

connection = psycopg2.connect(
    host="introduction-01-intro-ap-southeast-1-dev-introduction-db.cpfm8ml2cxp2.ap-southeast-1.rds.amazonaws.com",
    database="postgres",
    user="postgres",
    password="postgres123"
)

cursor = connection.cursor()
with open('./data/data.json', 'r',encoding='utf-8') as data_file:
            data = json.load(data_file)
            cursor.execute(""" create table if not exists book_store(
                poster_link text, book_name text, book_price text,
                status text, rating_star text) """)

            query_sql = """ insert into book_store
                select * from json_populate_recordset(NULL::book_store, %s) """
            cursor.execute(query_sql, (json.dumps(data),))
            connection.commit()