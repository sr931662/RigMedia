# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# Extracted data -> Temporary container (items) -> Storing in database

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class RigmediascrapperPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect(r'C:\Users\shivam\PycharmProjects\RigMediaProject\Scripts\RigMedia\RigMediaScrape'
                                    r'\Scraped_data.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute('''DROP TABLE IF EXISTS RigMediaScrape_RedditPostDataItem''')
        self.curr.execute("""create table RigMediaScrape_RedditPostDataItem (id integer primary key AUTOINCREMENT,
                        post_upload text,
                        post_headline text,
                        post_upvotes text,
                        post_comments text,
                        post_rewards text,
                        post_page_links text,
                        redditor text)""")
        # self.conn.commit()

    def process_item(self, item, spider):
        # self.RedditComment_storeDB(item)
        self.RedditPost_storeDB(item)
        # print("Pipeline :" + item['title'][0])
        return item

    def RedditPost_storeDB(self, item):
        self.curr.execute('''insert into RigMediaScrape_RedditPostDataItem (post_upload, post_headline, post_upvotes,
         post_comments, post_rewards, post_page_links, redditor) values (?, ?, ?, ?, ?, ?, ?)''',
                          (item['post_upload'][0],
                           item['post_headline'][0],
                           item['post_upvotes'][0],
                           item['post_comments'][0],
                           item['post_rewards'][0],
                           item['post_page_links'][0],
                           item['redditor'][0]))
        self.conn.commit()
        # self.conn.close()
