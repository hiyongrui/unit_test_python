from __future__ import annotations
class Url:

    def __init__(self, text: str):
        if text == "":
            raise Exception("Invalid URL - no scheme specified.")

        self.setup()
        self.text = text

        text = self.extract_scheme(text)
        text = self.extract_fragment(text)
        text = self.extract_query(text)
        text = self.extract_path(text)
        text = self.extract_userinfo(text)
        text = self.extract_port(text)
        
        print("FINAL TEXT", text)
        if text != "":
            self.domain_name = text

        self.add_smarts()
        
    def setup(self):
        self.user = None
        self.password = None
        self.domain_name = None
        self.port = None
        self.path = None
        self.query = None
        self.fragment = None


    def extract_scheme(self, url: str):
        # scheme = url.split(":")[0]
        before, sep, after = url.partition(":")
        self.scheme = before
        print(before)
        print(sep)
        print(after)
        if before == url:
            raise Exception("Invalid URL - no scheme specified.")
        if after.startswith("//"):
            after = after.replace("//", "")
        return after

    def extract_fragment(self, url: str):
        if "#" in url:
            before, sep, after = url.partition("#")
            self.fragment = after
            return before
        return url
    
    def extract_query(self, url: str):
        if "?" in url:
            before, sep, after = url.partition("?")
            self.query = after
            print("set query", after)
            print("return before query", before)
            return before
        return url

    def extract_path(self, url: str):
        if "/" in url:
            before, sep, after = url.partition("/")
            self.path = "/" + after
            return before
        return url

    def extract_userinfo(self, url: str):
        if "@" in url:
            before, sep, after = url.partition("@")
            self.user = before.split(":")[0]
            if ":" in before:
                self.password = before.split(":")[1]
            return after
        return url

    def extract_port(self, url: str):
        # http://example.com:81
        # http://me:secret@example.com#f1"
        # ftp://user:password@example.com:987/path
        # mailto:swlodkowski@smu.edu.sg
        if ":" in url:
            before, sep, after = url.partition(":")
            self.port = int(after)
            return before
        return url
    

    def add_smarts(self):
        print("add smart")
        if self.port == None:
            print("inside port 0")
            if self.scheme == "http":
                self.port = 80
            elif self.scheme == "https":
                self.port = 443
        if self.path == None and self.scheme != "mailto" and self.scheme != "news":
            self.path = "/"
    
    def __str__(self):
        # "http://user:password@example.com:123/x/y/z?a=b#s"
        return self.text

if __name__ == "__main__":
    print("Not an executable program.")