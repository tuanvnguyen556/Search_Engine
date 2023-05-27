class Remove_fragments:
    unique_urls = set()
    @classmethod
    def remove_fragment(cls, given_url: str) -> str:
        unique_url = given_url[given_url.find('#'):]
        if unique_url not in cls.unique_urls:
            cls.unique_urls.add(unique_url)
            return unique_url
        else:
            return ''
            