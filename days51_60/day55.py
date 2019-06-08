'''
Implement a URL shortener with the following methods:

    shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
    restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?
'''

import random
import string

class db:
    def __init__(self):
        self.urls = dict()

    def shorten(self, url):
        if url not in self.urls.items():
            letters = string.ascii_letters
            str = ''.join(random.choice(letters) for i in range(6))
            self.urls[str] = url

    def restore(self, short):
        for s in self.urls.keys():
            if s == short:
                return self.urls[s]
        return None
