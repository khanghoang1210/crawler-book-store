import psycopg2

table_name = "book_to_scrape"
data_field = [
    ("id", "integer")
    ("poster_link", "text"),
    ("book_name", "text"),
    ("book_price", "text"),
    ("status", "text"),
    ("rating_star", "text")
]

connection = psycopg2.connect(
    host="introduction-01-intro-ap-southeast-1-dev-introduction-db.cpfm8ml2cxp2.ap-southeast-1.rds.amazonaws.com",
    database="postgres",
    user="postgres",
    password="postgres123"
)


def create_db(connection, table_name, data_field):
    cursor = connection.cursor()
    field_name_and_field_type = [f"{field[0]} {field[1]}" for field in data_field]

    result_field = ','.join(field_name_and_field_type)
    print(result_field)
    create_sql = f"""create table if not exists {table_name}(
        {result_field}
    );
    """
    cursor.execute(create_sql)
    connection.commit()
create_db(connection,table_name,data_field)