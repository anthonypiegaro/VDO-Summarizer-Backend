import requests
from bs4 import BeautifulSoup
from .invalid_url_exception import InvalidYouTubeURLException

def get_video_title(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    title_element = soup.find("meta", property="og:title")

    if not title_element:
        raise InvalidYouTubeURLException(url, "No video title found in URL")
        
    video_title = title_element["content"]

    return video_title