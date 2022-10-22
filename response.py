class HttpResponse:

    EOL = "\r\n"

    def __init__(self, value: str):

        lines = value.split("\r\n")
        print(lines)
        for line in lines:
            col = line.split(" ")
            # index = value.find("HTTP/1.1")
            # code = value[index:]
            if line != "" and line.startswith("HTTP"):
                self.code = int(col[1]) # 200
                self.message = col[2] # OK
                print("COL", col, "endcode")

            if "Host:" in line:
                before, sep, after = line.partition("Host: ")
                self.setHeaders(after)
                print("endline")

        self.callSelf()

        print("\n@@@@@@@@@@@@@@ endinit @@@@@@@@@@@@@ \n")

    def callSelf(self):
        self.content_length = None
        self.body = b""
        # self.code = 200
        # self.message = "OK"
    
    def setHeaders(self, after):
        self.headers = {
            "Host": after
        }

if __name__ == "__main__":
    print("Not an executable program.")
