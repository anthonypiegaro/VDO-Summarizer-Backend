import re

from .invalid_url_exception import InvalidYouTubeURLException

def get_id(url):
    regex = r"(?:youtube\.com\/\S*(?:(?:\/e(?:mbed))?\/|watch\?(?:\S*?&?v\=))|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    
    match = re.search(regex, url)
    
    if not match:
        raise InvalidYouTubeURLException(url, "No video ID found in URL")
    
    return match.group(1)