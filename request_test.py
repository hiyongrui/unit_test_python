import unittest
from request import HttpRequest
from collections import OrderedDict

class HttpRequestTest(unittest.TestCase):
    def assertEqualRequest(self, request : HttpRequest, method : str, path : str, protocol : str, body : bytes = b"", content_length : (int | None) = None):
        self.assertEqual(request.method, method)
        self.assertEqual(request.path, path)
        self.assertEqual(request.protocol, protocol)
        if (content_length) or (request.content_length):
            self.assertEqual(request.content_length, content_length)
        self.assertEqual(request.body, body)

    """
    The `HttpRequest` class should expose an end-of-line sequence.
    """
    def test_eol(self):
        self.assertEqual(HttpRequest.EOL, "\r\n")

    """
    The `HttpRequest` class should properly process a request using any expected protocol.
    """
    def test_protocol(self):
        EOL = HttpRequest.EOL
        text = "GET / HTTP/1.0" + EOL +\
            EOL
        dump = text.encode("utf-8")
        request = HttpRequest(text)
        self.assertEqual(request.dump(), dump)
        self.assertEqualRequest(request, "GET", "/", "HTTP/1.0")
        self.assertIsNone(request.content_length)

    """
    The `HttpRequest` class should properly process a GET request.
    """
    def test_verb_get(self):
        EOL = HttpRequest.EOL
        text = "GET / HTTP/1.1" + EOL +\
            EOL
        dump = text.encode("utf-8")
        request = HttpRequest(text)
        self.assertEqual(request.dump(), dump)
        self.assertEqualRequest(request, "GET", "/", "HTTP/1.1")
        self.assertIsNone(request.content_length)

    """
    The `HttpRequest` class should properly process a DELETE request.
    """
    def test_verb_delete(self):
        EOL = HttpRequest.EOL
        text = "DELETE / HTTP/1.1" + EOL +\
            EOL
        dump = text.encode("utf-8")
        request = HttpRequest(text)
        self.assertEqual(request.dump(), dump)
        self.assertEqualRequest(request, "DELETE", "/", "HTTP/1.1")
        self.assertIsNone(request.content_length)

    """
    The `HttpRequest` class should properly process a PUT request.
    """
    def test_verb_put(self):
        EOL = HttpRequest.EOL
        text = "PUT / HTTP/1.1" + EOL +\
            EOL
        dump = text.encode("utf-8")
        request = HttpRequest(text)
        self.assertEqual(request.dump(), dump)
        self.assertEqualRequest(request, "PUT", "/", "HTTP/1.1")
        self.assertIsNone(request.content_length)

    """
    The `HttpRequest` class should properly process a POST request.
    """
    def test_verb_post(self):
        EOL = HttpRequest.EOL
        text = "POST / HTTP/1.1" + EOL +\
            EOL
        dump = text.encode("utf-8")
        request = HttpRequest(text)
        self.assertEqual(request.dump(), dump)
        self.assertEqualRequest(request, "POST", "/", "HTTP/1.1")
        self.assertIsNone(request.content_length)

    """
    The `HttpRequest` class should properly process a POST request with headers.
    """
    def test_post_header(self):
        EOL = HttpRequest.EOL
        text = "POST / HTTP/1.1" + EOL +\
            "User-agent: TestClient" + EOL +\
            EOL
        dump = text.encode("utf-8")
        request = HttpRequest(text)
        self.assertEqual(request.dump(), dump)
        self.assertEqualRequest(request, "POST", "/", "HTTP/1.1")
        self.assertEqual(request.headers["User-agent"], "TestClient")
        self.assertIsNone(request.content_length)

    """
    The `HttpRequest` class should not process a request without a method.
    """
    def test_malformed_method(self):
        EOL = HttpRequest.EOL
        text = "HTTP/1.1" + EOL +\
            "User-agent: TestClient" + EOL +\
            EOL
        with self.assertRaises(Exception) as context:
            request = HttpRequest(text)
        self.assertEqual(str(context.exception), "Invalid request - unspecified method.")

    """
    The `HttpRequest` class should not process a request without a path or a protocol type.
    """
    def test_malformed_path(self):
        EOL = HttpRequest.EOL
        text = "POST " + EOL +\
            "User-agent: TestClient" + EOL +\
            EOL
        with self.assertRaises(Exception) as context:
            request = HttpRequest(text)
        self.assertEqual(str(context.exception), "Invalid request - unspecified protocol type.")

    """
    The `HttpRequest` class should not process a request with an empty protocol type.
    """
    def test_malformed_type(self):
        EOL = HttpRequest.EOL
        text = "POST / " + EOL +\
            "User-agent: TestClient" + EOL +\
            EOL
        with self.assertRaises(Exception) as context:
            request = HttpRequest(text)
        self.assertEqual(str(context.exception), "Invalid request - unsupported protocol type.")

    """
    The `HttpRequest` class should not process a request with no additional EOL before the body.
    """
    def test_malformed_body(self):
        EOL = HttpRequest.EOL
        with self.assertRaises(Exception) as context:
            request = HttpRequest(
                "POST / HTTP/1.1" + EOL +\
                "Content-length: 3" + EOL
            )
        self.assertEqual(str(context.exception), "Invalid request - no end-of-line sequence after a header.")

    """
    The `HttpRequest` class should not process an empty request.
    """
    def test_empty(self):
        with self.assertRaises(Exception) as context:
            request = HttpRequest("")
        self.assertEqual(str(context.exception), "Invalid request - no end-of-line sequence.")

    """
    The `HttpRequest` class should properly serialize back to bytes from individual fields.
    """
    def test_data_to_bytes(self):
        EOL = HttpRequest.EOL
        text = "POST / HTTP/1.1" + EOL +\
            "User-agent: TestClient" +\
            "Content-length: 3" + EOL +\
            "Special header: 0" + EOL +\
            EOL
        body = b"abc"
        dump = text.encode("utf-8") + body
        headers = OrderedDict()
        headers["User-agent"] = "TestClient"
        headers["Content-length"] = "3"
        headers["Special header"] = "0"
        request = HttpRequest(
            "POST", body, "/", "HTTP/1.1", headers
        )
        self.assertEqual(request.dump(), dump)
        self.assertEqualRequest(request, "POST", "/", "HTTP/1.1", body, 3)
        self.assertEqual(request.content_length, 3)
        self.assertEqual(request.headers["User-agent"], "TestClient")
        self.assertEqual(request.headers["Content-length"], "3")
        self.assertEqual(request.headers["Special header"], "0")

    """
    The `HttpRequest` class should not process a request with a missing path.
    """
    def test_post_missing_path(self):
        EOL = HttpRequest.EOL
        text = "POST  HTTP/1.1" + EOL +\
            EOL +\
            EOL
        with self.assertRaises(Exception) as context:
            request = HttpRequest(text)
        self.assertEqual(str(context.exception), "Invalid request - unspecified path.")

    """
    The `HttpRequest` class should properly process a request with a body consisting of an end-of-line marker.
    """
    def test_post_with_data(self):
        EOL = HttpRequest.EOL
        text = "POST /file HTTP/1.1" + EOL +\
            EOL +\
            EOL
        dump = text.encode("utf-8")
        request = HttpRequest(text)
        self.assertEqualRequest(request, "POST", "/file", "HTTP/1.1", EOL.encode("utf8"))
        self.assertIsNone(request.content_length)

    """
    The `HttpRequest` class should properly serialize back to bytes from a request string.
    """
    def test_str_to_bytes(self):
        EOL = HttpRequest.EOL
        text = "POST / HTTP/1.1" + EOL +\
            "User-agent: TestClient" + EOL +\
            "Content-length: 3" + EOL +\
            "Special header: 0" + EOL +\
            EOL
        body = b"abc"
        dump = text.encode("utf-8") + body
        request = HttpRequest(text, body)
        self.assertEqual(request.dump(), dump)
        self.assertEqualRequest(request, "POST", "/", "HTTP/1.1", body, 3)
        self.assertEqual(request.content_length, 3)
        self.assertEqual(request.headers["User-agent"], "TestClient")
        self.assertEqual(request.headers["Content-length"], "3")
        self.assertEqual(request.headers["Special header"], "0")

if __name__ == "__main__":
    unittest.main()
