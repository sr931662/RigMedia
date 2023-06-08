import asyncio
from scrapy.utils.project import get_project_settings
from bs4 import BeautifulSoup
import scrapy
import requests
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from Scripts.RigMedia.RigMediaScrape.RigMediaScrapper.RigMediaScrapper.items import RigmediaPostDataItem
from Scripts.RigMedia.RigMedia.utils import title_generator

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

class RedditpostSpider(scrapy.Spider):
    name = "redditpost"
    allowed_domains = ["reddit.com"]
    # title = 'https://www.livemint.com/news/world/microsoft-outlook-is-down-as-users-face-outage-issues-details-here-11685976540327.html'
    # title = 'https://amp.cnn.com/cnn/2023/05/17/india/india-karnataka-elections-bjp-congress-intl-hnk/index.html'

    def __init__(self, link):
        self.link = title_generator(link)


    def start_requests(self):
        # link = 'https://www.livemint.com/news/world/microsoft-outlook-is-down-as-users-face-outage-issues-details-here-11685976540327.html'
        start_urls = f"https://www.reddit.com/search/?q={self.link}&type=link"
        yield scrapy.Request(url=start_urls, callback=self.parse)

    def parse(self, response):
        items = RigmediaPostDataItem()
        # Extracting data from each post on the page
        for post in response.css("div._2dkUkgRYbhbpU_2O2Wc5am"):
            post_upload = post.css('div._3xeOZ4NlqvpwzbB5E8QC6r').xpath('span[2]/text()').extract()
            post_headline = post.css('._eYtD2XCVieq6emjKBH3m ::text').extract()
            post_upvotes = post.css('._2IpBiHtzKzIxk2fKI4UOv1 ').xpath('span[1]/text()').extract()
            post_comments = post.css('._2IpBiHtzKzIxk2fKI4UOv1 ').xpath('span[2]/text()').extract()
            post_rewards = post.css('._2IpBiHtzKzIxk2fKI4UOv1 ').xpath('span[3]/text()').extract()
            post_links = post.css('._2i5O0KNpb9tDq0bsNOZB_Q a::attr(href)').extract()

            post_page_links = []
            redditors = []
            for link in post_links:
                if not link.startswith('https://'):
                    post_page_links.append('https://reddit.com' + link)
                else:
                    post_page_links.append(link)
            for link in post_links:
                if link is not None:
                    redditors.append(link.split('/comments/'))
                else:
                    redditors.append('no link')

            # yield {
            #     'post_upload': post_upload,
            #     'post_headline': post_headline,
            #     'post_upvotes': post_upvotes,
            #     'post_comments': post_comments,
            #     'post_rewards': post_rewards,
            #     'post_page_links': post_page_links,
            #     'redditor': redditors[0]
            # }
            items['post_upload'] = post_upload
            items['post_headline'] = post_headline
            items['post_upvotes'] = post_upvotes
            items['post_comments'] = post_comments
            items['post_rewards'] = post_rewards
            items['post_page_links'] = post_page_links
            items['redditor'] = redditors[0]

            yield items


async def run_spider(link):
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(RedditpostSpider, link=link)
    process.start()

# asyncio.run(run_spider('https://www.bbc.com/news/technology-65809408'))

# run_spider('https://www.livemint.com/news/world/microsoft-outlook-is-down-as-users-face-outage-issues-details-here-11685976540327.html')
# run_spider('https://www.ndtv.com/india-news/made-it-very-clear-nitish-kumar-delays-mega-opposition-meet-names-congress-4095151')
# run_spider()

# runSpider("redditpost")
