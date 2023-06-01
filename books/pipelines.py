# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2


class BooksPipeline:    

    def __init__(self):

        table_name = "book_to_scrape"
        data_field = [
            ("poster_link", "text"),
            ("book_name", "text"),
            ("book_price", "text"),
            ("status", "text"),
            ("rating_star", "text")
        ]

        self.connection = psycopg2.connect(
            host="introduction-01-intro-ap-southeast-1-dev-introduction-db.cpfm8ml2cxp2.ap-southeast-1.rds.amazonaws.com",
            database="postgres",
            user="postgres",
            password="postgres123"
        )
        self.cursor = self.connection.cursor()
        field_name_and_field_type = [
            f"{field[0]} {field[1]}" for field in data_field]

        result_field = ','.join(field_name_and_field_type)
        print(result_field)
        create_sql = f"""create table if not exists {table_name}(
            {result_field}
        );
        """
        self.cursor.execute(create_sql)
        self.connection.commit()

    def process_item(self, item, spider):
            self.insert_database(item)
            return item

    def insert_database(self,items):
        table_name = "book_to_scrape"
        data_field = [
           # ("id", "integer")
            ("poster_link", "text"),
            ("book_name", "text"),
            ("book_price", "text"),
            ("status", "text"),
            ("rating_star", "text")
        ]
        field_name = [f"{field[0]}" for field in data_field]
        result_field = ','.join(field_name)
        self.cursor.execute(""" insert into book_to_scrape (poster_link, book_name, book_price, status, rating_star) values (%s,%s,%s,%s,%s)""", (
            items["poster_link"],
            items["book_name"],
            items["book_price"],
            items["status"],
            items["rating_star"]
        ))
        # data_insert = [f"""'{item['poster_link']}', '{item['book_name']}', '{item['book_price']}', '{item['status']}','{item['rating_star']}' """ 
        #                for item in items]

        # result_data = ','.join(data_insert)
        # insert_sql = f"""insert into {table_name}({result_field})
        #             values
        #             {result_data};
        #             """
        #self.cursor.execute(insert_sql)
        self.connection.commit()
