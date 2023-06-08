# import os
# from bs4 import BeautifulSoup
# import scrapy
# import requests
# def title_generator(link):
#     # url = 'https://amp.cnn.com/cnn/2023/05/17/india/india-karnataka-elections-bjp-congress-intl-hnk/index.html'
#     url = link
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     # Extract the title element from the HTML
#     title_element = soup.find('title')
#
#     # Get the text of the title
#     title = title_element.text if title_element else None
#     return title
#
#
#
# class RedditpostSpider(scrapy.Spider):
#     name = "redditpost"
#     title = title_generator('https://amp.cnn.com/cnn/2023/05/17/india/india-karnataka-elections-bjp-congress-intl-hnk'
#                             '/index.html')
#     allowed_domains = ["reddit.com"]
#     # items = RigmediascrapperItem()
#     start_urls = [rf"https://www.reddit.com/search/?q={title}&type=link"]
#
#     def parse(self, response):
#         # Extracting data from each post on the page
#         for post in response.css("div._2dkUkgRYbhbpU_2O2Wc5am") or response.css('#content'):
#             post_upload = post.css('div._3xeOZ4NlqvpwzbB5E8QC6r').xpath('span[2]/text()').extract()
#             post_upvotes = post.css('._2IpBiHtzKzIxk2fKI4UOv1 ').xpath('span[1]/text()').extract()
#             post_comments = post.css('._2IpBiHtzKzIxk2fKI4UOv1 ').xpath('span[2]/text()').extract()
#             post_rewards = post.css('._2IpBiHtzKzIxk2fKI4UOv1 ').xpath('span[3]/text()').extract()
#             post_links = post.css('._2i5O0KNpb9tDq0bsNOZB_Q a::attr(href)').extract()
#
#             post_page_links = []
#             for link in post_links:
#                 if not link.startswith('https://'):
#                     post_page_links.append('https://reddit.com' + link)
#                 else:
#                     post_page_links.append(link)
#
#             yield {
#                 'post_upload': post_upload,
#                 'post_upvotes': post_upvotes,
#                 'post_comments': post_comments,
#                 'post_rewards': post_rewards,
#                 'post_page_links': post_page_links,
#             }
#
#
# # post_upload = response.css('._2dkUkgRYbhbpU_2O2Wc5am').css('div._3xeOZ4NlqvpwzbB5E8QC6r').xpath('span[2]/text()').extract()
# #         post_upvotes = response.css('._2dkUkgRYbhbpU_2O2Wc5am').css('._2IpBiHtzKzIxk2fKI4UOv1 ').xpath('span[1]/text()').extract()
# #         post_comments = response.css('._2dkUkgRYbhbpU_2O2Wc5am').css('._2IpBiHtzKzIxk2fKI4UOv1 ').xpath('span[2]/text()').extract()
# #         post_rewards = response.css('._2dkUkgRYbhbpU_2O2Wc5am').css('._2IpBiHtzKzIxk2fKI4UOv1 ').xpath('span[3]/text()').extract()
# #         post_links = response.css('._2i5O0KNpb9tDq0bsNOZB_Q a::attr(href)').extract()
# #         post_headline = response.css('._eYtD2XCVieq6emjKBH3m::text').extract()
# #
# #         pwc_upload = response.css('._2VF2J19pUIMSLJFky-7PEI::text').extract()
# #         cop_upload = response.css('._3yx4Dn0W3Yunucf5sVJeFU::text').extract()
# #         pwc_links = response.css('._2i5O0KNpb9tDq0bsNOZB_Q a::attr(href)').extract()
# #         pwc_headline = response.css('._eYtD2XCVieq6emjKBH3m::text').extract()
# #         comment_op = response.css('._1oQyIsiPHYt6nx7VOmd1sz')[ranger(0, 21, 1)].css('._3cjCphgls6DH-irkVaA0GM ::text').extract()
# #
# #         post_page_links = []
# #         for link in post_links:
# #             if not link.startswith('https://'):
# #                 post_page_links.append('https://reddit.com' + link)
# #             else:
# #                 post_page_links.append(link)
# #         comment_page_links = []
# #         for link in pwc_links:
# #             if not link.startswith('https://'):
# #                 comment_page_links.append('https://reddit.com' + link)
# #             else:
# #                 comment_page_links.append(link)
# # post_data = {'post upload time': post_upload,
# #                      'post upvotes': post_upvotes,
# #                      'post comments': post_comments,
# #                      'post rewards': post_rewards,
# #                      'post links': post_links,
# #                      'post ': post_headline
# #         }
# #         comment_data = {'commented post upload time': pwc_upload,
# #                         'comment on post upload time': cop_upload,
# #                         'comment on post': comment_op,
# #                         'commented post headline': pwc_headline,
# #                         'commented post links': pwc_links
# #         }
# #         yield post_data