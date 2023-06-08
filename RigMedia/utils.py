from bs4 import BeautifulSoup
import requests

def title_generator(link):
    url = link
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title element from the HTML
    title_element = soup.find('title')

    # Get the text of the title
    title = title_element.text if title_element else None
    return title