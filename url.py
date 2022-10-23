from __future__ import annotations
class Url:

    def __init__(self, url: str):

        # self.url = url
        after = self.extract_scheme(url)
        self.setup()
        self.domain_name = after
        

    def extract_scheme(self, url: str):
        # scheme = url.split(":")[0]
        before, sep, after = url.partition("://")
        self.scheme = before
        if before == "http":
            self.port = 80
        else:
            self.port = 443
        print(before)
        print(sep)
        print(after)
        return after
    
    def setup(self):
        self.path = "/"
        self.user = None
        self.password = None
        self.query = None
        self.fragment = None

if __name__ == "__main__":
    print("Not an executable program.")