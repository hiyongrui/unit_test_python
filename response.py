class HttpResponse:

    EOL = "\r\n"
    validHTTP = ["HTTP/1.1", "HTTP/1.0"]
    def __init__(self, value: str, data: bytes = b"", headers: dict = {}, codeNum: int = 0, http: str = ""):
        if value == "":
            raise Exception("Invalid response - no end-of-line sequence.")
        self.callSelf()
        lines = value.split("\r\n")
        print(lines)

        for index, line in enumerate(lines):
            
            if data:
                print("theres data@@@@@")
                self.body = data
            if headers:
                self.setDump(value, headers, codeNum, http)
                break

            if index == 0:
                # self.code = int(line[1])
                code = line.split(" ")[1]
                self.http = line.split(" ")[0]
                print('code', line.split(" ")[0])
                if line.split(" ")[0] not in self.validHTTP:
                    print("LINE", line.split(" ")[0])
                    raise Exception("Invalid response - unsupported protocol type.")
                if not code.isnumeric():
                    raise Exception("Invalid response - an error code must be a number.")
                teapot = line.split(f"{code} ")[1]
                self.setCodeMessage(code, teapot)
                print(teapot)
                print("this line", line)

            # col = line.split(" ")
            # index = value.find("HTTP/1.1")
            # code = value[index:]
            # if line != "" and line.startswith("HTTP"):
            #     self.code = int(col[1]) # 200
            #     self.message = col[2] # OK
            #     print("COL", col, "endcode")
            else:
                if "Host" in line:
                    before, sep, after = line.partition(":")
                    self.setHeaders("Host", after.strip())
                    print("endline")

                elif "Content-length" in line:
                    if ":" not in line:
                        raise Exception("Invalid response - no colon separating a header from its value.")
                    checkLine = lines[index+1]
                    print("ca",checkLine)
                    if checkLine == "" and index == len(lines)-2:
                        print("Check"+checkLine+"END", index)
                        raise Exception("Invalid response - no end-of-line sequence after a header.")
                
                    before, sep, after = line.partition("Content-length: ")
                    self.setHeaders("Content-length", after)
                    self.content_length = int(after)
                
                elif "Special header" in line:
                    before, sep, after = line.partition(":")
                    self.setHeaders("Special header", after.strip())

                else:
                    if line != "" and index == len(lines)-1: #line not empty and is last line
                        print("noEOL", line)
                        print("this index", index)
                        self.body = line.encode("utf-8")
        # self.callSelf()

        print("\n@@@@@@@@@@@@@@ endinit @@@@@@@@@@@@@ \n")
        print(self.headers)
    def callSelf(self):
        self.content_length = None
        self.body = b""
        self.headers = {}
        # self.code = 200
        # self.message = "OK"
    
    def setHeaders(self, header, after):
        value = "Host" if header == 'Host' else "Content-length" if header == "Content-length" else "Special header"
        # self.headers.update({
        #     value: after
        # })
        self.headers[value] = after

    def setCodeMessage(self, code, message):
        self.code = int(code) # 200
        self.message = message # OK

    def dump(self):
        firstLine = f"{self.http} {self.code} {self.message}{self.EOL}"
        nextLines = ""
        for key, value in self.headers.items():
            nextLines += f"{key}: {value}{self.EOL}"
        dump = (firstLine + nextLines + self.EOL).encode("utf-8") + self.body
        return dump

    def setDump(self, value, headers, codeNum, http):
        self.http = http
        self.code = codeNum
        self.message = value
        self.headers = headers
        self.content_length = int(headers["Content-length"])

if __name__ == "__main__":
    print("Not an executable program.")
