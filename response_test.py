from __future__ import annotations

import unittest
from response import HttpResponse
from collections import OrderedDict


class HttpResponseTest(unittest.TestCase):
    def assertEqualResponse(self, response : HttpResponse, code : int, message : str, body : bytes = b"", content_length : (int | None) = None):
        self.assertEqual(response.code, code)
        self.assertEqual(response.message, message)
        if (content_length) or (response.content_length):
            self.assertEqual(response.content_length, content_length)
        self.assertEqual(response.body, body)

    # """
    # The `HttpResponse` class should expose an end-of-line sequence.
    # """
    # def test_eol(self):
    #     self.assertEqual(HttpResponse.EOL, "\r\n")

    # """
    # The `HttpResponse` class should properly process a basic 200 response.
    # """
    # def test_200_no_data(self):
    #     EOL = HttpResponse.EOL
    #     response = HttpResponse(
    #         "HTTP/1.1 200 OK" + EOL +\
    #         EOL +\
    #         ""
    #     )
    #     self.assertEqualResponse(response, 200, "OK")
    #     self.assertIsNone(response.content_length)

    """
    The `HttpResponse` class should properly process a 200 response with additional headers.
    """
    def test_200_user_agent(self):
        EOL = HttpResponse.EOL
        response = HttpResponse(
            "HTTP/1.1 200 OK" + EOL +\
            "Host: TestServer" + EOL +\
            EOL +\
            ""
        )
        self.assertEqualResponse(response, 200, "OK")
        self.assertEqual(response.headers["Host"], "TestServer")
        self.assertIsNone(response.content_length)

    # """
    # The `HttpResponse` class should properly process a 200 response with data but no `Content-length` header.
    # """
    # def test_200_data_no_length(self):
    #     EOL = HttpResponse.EOL
    #     response = HttpResponse(
    #         "HTTP/1.1 200 OK" + EOL +\
    #         EOL +\
    #         "abc"
    #     )
    #     self.assertEqualResponse(response, 200, "OK", b"abc")
    #     self.assertIsNone(response.content_length)

    # """
    # The `HttpResponse` class should properly process a 200 response with data and `Content-length` header.
    # """
    # def test_200_data_length(self):
    #     EOL = HttpResponse.EOL
    #     response = HttpResponse(
    #         "HTTP/1.1 200 OK" + EOL +\
    #         "Content-length: 3" + EOL +\
    #         EOL +\
    #         "abc"
    #     )
    #     self.assertEqualResponse(response, 200, "OK", b"abc", 3)
    #     self.assertEqual(response.headers["Content-length"], "3")

    # """
    # The `HttpResponse` class should properly process a 418 response with data but no `Content-length` header.
    # """
    # def test_418_data(self):
    #     EOL = HttpResponse.EOL
    #     response = HttpResponse(
    #         "HTTP/1.1 418 I'm a teapot" + EOL +\
    #         EOL,
    #         b"data"
    #     )
    #     self.assertEqualResponse(response, 418, "I'm a teapot", b"data")
    #     self.assertIsNone(response.content_length)

    # """
    # The `HttpResponse` class should properly process a 418 response with data and the `Content-length` header.
    # """
    # def test_418_data_header(self):
    #     EOL = HttpResponse.EOL
    #     body = b"data"
    #     response = HttpResponse(
    #         "HTTP/1.1 418 I'm a teapot" + EOL +\
    #         "Content-len: 4" + EOL +\
    #         EOL,
    #         body
    #     )
    #     self.assertEqualResponse(response, 418, "I'm a teapot", body, 4)
    #     self.assertEqual(response.headers["Content-len"], "4")
    #     self.assertEqual(response.content_length, 4)

    # """
    # The `HttpResponse` class should properly process a 301 response with the `Location` header.
    # """
    # def test_301_header(self):
    #     EOL = HttpResponse.EOL
    #     response = HttpResponse(
    #         "HTTP/1.1 301 Moved Permanently" + EOL +\
    #         "Location: https://www.example.com/" + EOL +\
    #         EOL
    #     )
    #     self.assertEqualResponse(response, 301, "Moved Permanently")
    #     self.assertIsNone(response.content_length)

    # """
    # The `HttpResponse` class should not process a response with an unsupported protocol version.
    # """
    # def test_malformed_type(self):
    #     EOL = HttpResponse.EOL
    #     with self.assertRaises(Exception) as context:
    #         response = HttpResponse(
    #             "HTTP/? 302 Found" + EOL +\
    #             EOL,
    #             b"data"
    #         )
    #     self.assertEqual(str(context.exception), "Invalid response - unsupported protocol type.")

    # """
    # The `HttpResponse` class should not process a response with no supported response code.
    # """
    # def test_malformed_code(self):
    #     EOL = HttpResponse.EOL
    #     with self.assertRaises(Exception) as context:
    #         response = HttpResponse(
    #             "HTTP/1.1 ? Found" + EOL +\
    #             EOL,
    #             b"data"
    #         )
    #     self.assertEqual(str(context.exception), "Invalid response - an error code must be a number.")

    # """
    # The `HttpResponse` class should not process a response with a missing colon in a header.
    # """
    # def test_malformed_header(self):
    #     EOL = HttpResponse.EOL
    #     with self.assertRaises(Exception) as context:
    #         response = HttpResponse(
    #             "HTTP/1.1 200 OK" + EOL +\
    #             "Content-length 3" + EOL +\
    #             EOL +\
    #             "abc"
    #         )
    #     self.assertEqual(str(context.exception), "Invalid response - no colon separating a header from its value.")

    # """
    # The `HttpResponse` class should not process a response with no EOL after a header.
    # """
    # def test_malformed_body(self):
    #     EOL = HttpResponse.EOL
    #     with self.assertRaises(Exception) as context:
    #         response = HttpResponse(
    #             "HTTP/1.1 200 OK" + EOL +\
    #             "Content-length: 3" + EOL +\
    #             "abc"
    #         )
    #     self.assertEqual(str(context.exception), "Invalid response - no end-of-line sequence after a header.")

    # """
    # The `HttpResponse` class should not process a response with no additional EOL before the body.
    # """
    # def test_malformed_body(self):
    #     EOL = HttpResponse.EOL
    #     with self.assertRaises(Exception) as context:
    #         response = HttpResponse(
    #             "HTTP/1.1 200 OK" + EOL +\
    #             "Content-length: 3" + EOL
    #         )
    #     self.assertEqual(str(context.exception), "Invalid response - no end-of-line sequence after a header.")

    # """
    # The `HttpResponse` class should not process an empty response.
    # """
    # def test_empty(self):
    #     with self.assertRaises(Exception) as context:
    #         response = HttpResponse("")
    #     self.assertEqual(str(context.exception), "Invalid response - no end-of-line sequence.")

    # """
    # The `HttpResponse` class should properly process a response with an additional header where a key needs space trimming.
    # """
    # def test_header_key_spaces(self):
    #     EOL = HttpResponse.EOL
    #     response = HttpResponse(
    #         "HTTP/1.1 200 OK" + EOL +\
    #         "Host : TestServer" + EOL +\
    #         EOL
    #     )
    #     self.assertEqualResponse(response, 200, "OK")
    #     self.assertEqual(response.headers["Host"], "TestServer")
    #     self.assertIsNone(response.content_length)

    # """
    # The `HttpResponse` class should properly process a response with an additional header where a value needs space trimming.
    # """
    # def test_header_value_spaces(self):
    #     EOL = HttpResponse.EOL
    #     response = HttpResponse(
    #         "HTTP/1.1 200 OK" + EOL +\
    #         "Host: TestServer " + EOL +\
    #         EOL
    #     )
    #     self.assertEqualResponse(response, 200, "OK")
    #     self.assertEqual(response.headers["Host"], "TestServer")
    #     self.assertIsNone(response.content_length)

    # """
    # The `HttpResponse` class should properly process a response with multiple additional headers.
    # """
    # def test_header_value_spaces(self):
    #     EOL = HttpResponse.EOL
    #     response = HttpResponse(
    #         "HTTP/1.1 200 OK" + EOL +\
    #         "Host: TestServer" + EOL +\
    #         "Content-length: 0" + EOL +\
    #         "Special header: 0" + EOL +\
    #         EOL
    #     )
    #     self.assertEqualResponse(response, 200, "OK", content_length = 0)
    #     self.assertEqual(response.content_length, 0)
    #     self.assertEqual(response.headers["Content-length"], "0")
    #     self.assertEqual(response.headers["Host"], "TestServer")
    #     self.assertEqual(response.headers["Special header"], "0")

    # """
    # The `HttpResponse` class should properly serialize back to bytes from individual fields.
    # """
    # def test_data_to_bytes(self):
    #     EOL = HttpResponse.EOL
    #     text = "HTTP/1.1 200 OK" + EOL +\
    #         "Host: TestServer" + EOL +\
    #         "Content-length: 3" + EOL +\
    #         "Special header: 0" + EOL +\
    #         EOL
    #     body = b"abc"
    #     dump = text.encode("utf-8") + body
    #     headers = OrderedDict()
    #     headers["Host"] = "TestServer"
    #     headers["Content-length"] = "3"
    #     headers["Special header"] = "0"
    #     response = HttpResponse(
    #         "OK", body, headers, 200, "HTTP/1.1"
    #     )
    #     self.assertEqual(response.dump(), dump)
    #     self.assertEqualResponse(response, 200, "OK", body, 3)
    #     self.assertEqual(response.content_length, 3)
    #     self.assertEqual(response.headers["Host"], "TestServer")
    #     self.assertEqual(response.headers["Content-length"], "3")
    #     self.assertEqual(response.headers["Special header"], "0")

    # """
    # The `HttpResponse` class should properly serialize back to bytes from a response string.
    # """
    # def test_str_to_bytes(self):
    #     EOL = HttpResponse.EOL
    #     text = "HTTP/1.1 200 OK" + EOL +\
    #         "Host: TestServer" + EOL +\
    #         "Content-length: 3" + EOL +\
    #         "Special header: 0" + EOL +\
    #         EOL
    #     body = b"abc"
    #     dump = text.encode("utf-8") + body
    #     response = HttpResponse(text, body)
    #     self.assertEqual(response.dump(), dump)
    #     self.assertEqualResponse(response, 200, "OK", body, 3)
    #     self.assertEqual(response.content_length, 3)
    #     self.assertEqual(response.headers["Host"], "TestServer")
    #     self.assertEqual(response.headers["Content-length"], "3")
    #     self.assertEqual(response.headers["Special header"], "0")

if __name__ == "__main__":
    unittest.main()
