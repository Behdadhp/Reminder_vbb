from urllib.request import urlopen
import json


# Class based
class RequestAPI:
    def url(self,link):
        self.link = link
        with urlopen(link) as response:
            source = response.read()
            destination = json.loads(source)
        return destination
