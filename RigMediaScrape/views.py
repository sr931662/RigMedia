import json
import asyncio
import threading

from django.shortcuts import render
from scrapy.crawler import CrawlerProcess
from Scripts.RigMedia.RigMedia.utils import title_generator

# from .RigMediaScrapper.RigMediaScrapper.spiders import quotes_spider
# scraper = quotes_spider
from .models import RedditPostDataItem
import sqlite3

from .RigMediaScrapper.RigMediaScrapper.spiders.quotes_spider import run_spider
# Create your views here.


def home(request):
    return render(request, 'home.html')


import asyncio

# ...
async def runSpider(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        # title = title_generator(link)  # Get the title using the title_generator function

        await asyncio.gather(run_spider(link))  # Run the spider asynchronously

    return render(request, 'home.html')



def reddit_data(request):
    RedditPostdata = RedditPostDataItem.objects.all()
    return render(request, 'home.html', {'RedditPost': RedditPostdata})


# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(runSpider())
