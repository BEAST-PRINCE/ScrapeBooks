# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class BookscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # field_names = adapter.get_field_names()
        # for field in field_names:
        #     if field == 'stars':
        #         value = adapter.get_value(field)
        #         adapter[field] = value[value.find(" ")+1:]
        
        value = adapter.get('stars')
        star_values = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
        adapter['stars'] = star_values[value[value.find(" ")+1:]]


        available_value = adapter.get('availablity')
        split_list = available_value.split("(")
        if len(split_list)<2:
            adapter['availablity'] = 0
        else:
            split_list = split_list[1].split(" ")
            adapter['availablity'] = int(split_list[0])
        

        review_value = adapter.get('no_of_reviews')
        adapter['no_of_reviews'] = int(review_value)


        return item



class SaveToMYSQLPipeline:
    def __init__(self):
        self.conn_obj = mysql.connector.connect(host='localhost', database='books', user='root', password='')
        self.cursor = self.conn_obj.cursor()
        self.cursor.execute("Create table if not exists books_data(id int Not Null auto_increment Primary Key, url varchar(255), title text, product_type varchar(30), price_excl_tax varchar(10), tax varchar(10), availablity int, no_of_reviews int, stars int, catagory varchar(20),price varchar(10), description text)")
    

    def process_item(self, item, spider):
        self.cursor.execute(f'INSERT INTO books_data(url, title, product_type, price_excl_tax, tax, availablity, no_of_reviews, stars, catagory, price, description) VALUES ("{item["url"]}", "{item["title"]}", "{item["product_type"]}", "{item["price_excl_tax"]}", "{item["tax"]}", {item["availablity"]}, {item["no_of_reviews"]}, {item["stars"]}, "{item["catagory"]}", "{item["price"]}", "{item["description"]}")')

        # self.cursor.execute(f'Insert into books_data(url, title, product_type, price_excl_tax, tax, availablity, no_of_reviews, stars, catagory, price, description) values("{item['url']}","{item['title']}","{item['product_type']}","{item['price_excl_tax']}","{item['tax']}",{item['availablity']},{item['no_of_reviews']},{item['stars']},"{item['catagory']}","{item['price']}","{item['description']}")')
        self.conn_obj.commit()
        return item
    

    def close_spider(self, spider):
        self.cursor.close()
        self.conn_obj.close()