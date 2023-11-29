class InvalidYouTubeURLException(Exception):
    """Exception raised for errors in the YouTube URL format."""

    def __init__(self, url, message="Invalid YouTube URL provided"):
        self.url = url
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.url}'