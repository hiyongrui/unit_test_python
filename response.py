class HttpResponse:

    EOL = "\r\n"

    def __init__(self, key : str, value = None):
        if (value):
            self.key = key
            self.value = value
        else:
            index = key.find("=")
            if (index < 1):
                raise Exception("Invalid pair.")
            self.key = key[:index]
            self.value = key[index + 1:]

if __name__ == "__main__":
    print("Not an executable program.")
