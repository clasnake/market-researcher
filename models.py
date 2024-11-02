class Company:
    """ TODO: Add more fields """
    def __init__(self, name: str, description: str, funding_info: dict = None, media_mentions: dict = None, rankings: dict = None):
        self.name = name
        self.description = description
        self.funding_info = funding_info
        self.media_mentions = media_mentions
        self.rankings = rankings

    def __str__(self):
        return f"Company(name={self.name}, \
                description={self.description}, \
                funding_info={self.funding_info}, \
                media_mentions={self.media_mentions}, \
                rankings={self.rankings})"

