# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RigmediaPostDataItem(scrapy.Item):
    id = scrapy.Field()
    post_upload = scrapy.Field()
    post_headline = scrapy.Field()
    post_upvotes = scrapy.Field()
    post_comments = scrapy.Field()
    post_rewards = scrapy.Field()
    post_page_links = scrapy.Field()
    redditor = scrapy.Field()

#
# class RigmediaCommentItem(scrapy.Item):
#     # define the fields for your item here like:
#     id = scrapy.Field()
#     pwc_upload = scrapy.Field()
#     cop_upload = scrapy.Field()
#     pwc_links = scrapy.Field()
#     pwc_headlines = scrapy.Field()
#     pwc_upvotes = scrapy.Field()
#     pwc_comments = scrapy.Field()
#     pwc_rewards = scrapy.Field()
#     cop_upvotes = scrapy.Field()
#     cop_rewards = scrapy.Field()
#     comment = scrapy.Field()
