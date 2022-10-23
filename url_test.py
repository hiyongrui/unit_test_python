from __future__ import annotations
import unittest
from url import Url

class UrlTest(unittest.TestCase):
    def assertEqualUrl(
        self,
        url : Url,
        scheme : str,
        path : (str | None) = None,
        domain_name : (str | None) = None,
        query : (str | None) = None,
        fragment : (str | None) = None,
        port : (int | None) = None,
        user : (str | None) = None,
        password : (str | None) = None
    ):
        self.assertEqual(url.scheme, scheme)
        self.assertEqual(url.user, user)
        self.assertEqual(url.password, password)
        self.assertEqual(url.domain_name, domain_name)
        self.assertEqual(url.port, port)
        self.assertEqual(url.path, path)
        self.assertEqual(url.query, query)
        self.assertEqual(url.fragment, fragment)

    """
    The `Url` class should properly analyze simple addresses.
    """
    def test_http_simple(self):
        self.assertEqualUrl(
            Url("http://example.com"),
            "http", "/", "example.com", port = 80
        )

    # """
    # The `Url` class should properly analyze complex addresses.
    # """
    # def test_http_extended(self):
    #     self.assertEqualUrl(
    #         Url("http://example.com/x?yy#zzz"),
    #         "http", "/x", "example.com", "yy", "zzz", port = 80
    #     )

    # """
    # The `Url` class should properly work with any scheme.
    # """
    # def test_https_scheme(self):
    #     self.assertEqualUrl(
    #         Url("https://example.com"),
    #         "https", "/", "example.com", port = 443
    #     )

    # """
    # The `Url` class should properly work with any port.
    # """
    # def test_http_port(self):
    #     self.assertEqualUrl(
    #         Url("http://example.com:81"),
    #         "http", "/", "example.com", port = 81
    #     )

    # """
    # The `Url` class should properly work with any port.
    # """
    # def test_http_path(self):
    #     self.assertEqualUrl(
    #         Url("http://example.com/test/"),
    #         "http", "/test/", "example.com", port = 80
    #     )

    # """
    # The `Url` class should properly work with paths using any filename.
    # """
    # def test_http_filename(self):
    #     self.assertEqualUrl(
    #         Url("http://example.com/test/filename"),
    #         "http", "/test/filename", "example.com", port = 80
    #     )

    # """
    # The `Url` class should properly work with query strings.
    # """
    # def test_http_query(self):
    #     self.assertEqualUrl(
    #         Url("http://example.com?a=b"),
    #         "http", "/", "example.com", "a=b", port = 80
    #     )

    # """
    # The `Url` class should properly work with fragments.
    # """
    # def test_http_fragment(self):
    #     self.assertEqualUrl(
    #         Url("http://example.com#f1"),
    #         "http", "/", "example.com", fragment = "f1", port = 80
    #     )

    # """
    # The `Url` class should properly work with user and password information.
    # """
    # def test_http_userinfo(self):
    #     self.assertEqualUrl(
    #         Url("http://me:secret@example.com#f1"),
    #         "http", "/", "example.com", fragment = "f1", port = 80, user = "me", password = "secret"
    #     )

    # """
    # The `Url` class should properly work with `file` protocol urls.
    # """
    # def test_file_protocol(self):
    #     self.assertEqualUrl(
    #         Url("file:///C:/Users/UserName/index.html"),
    #         "file", "/C:/Users/UserName/index.html"
    #     )

    # """
    # The `Url` class should properly work with `mail` protocol urls.
    # """
    # def test_mail_protocol(self):
    #     self.assertEqualUrl(
    #         Url("mailto:swlodkowski@smu.edu.sg"),
    #         "mailto", domain_name = "smu.edu.sg", user = "swlodkowski"
    #     )

    # """
    # The `Url` class should properly work with `mail` protocol urls with a query.
    # """
    # def test_mail_protocol_query(self):
    #     self.assertEqualUrl(
    #         Url("mailto:swlodkowski@smu.edu.sg?subject=SE101"),
    #         "mailto", domain_name = "smu.edu.sg", query = "subject=SE101", user = "swlodkowski"
    #     )

    # """
    # The `Url` class should properly work with `usenet` protocol urls.
    # """
    # def test_usenet_protocol(self):
    #     self.assertEqualUrl(
    #         Url("news:example"),
    #         "news", None, "example"
    #     )

    # """
    # The `Url` class should properly work with `ftp` protocol urls.
    # """
    # def test_ftp_protocol(self):
    #     self.assertEqualUrl(
    #         Url("ftp://user:password@example.com:987/path"),
    #         "ftp", "/path", domain_name = "example.com", user = "user", password = "password", port = 987
    #     )

    # """
    # The `Url` class should properly serialize back to a valid address.
    # """
    # def test_to_string(self):
    #     address = "http://user:password@example.com:123/x/y/z?a=b#s"
    #     url = Url(address)
    #     self.assertEqualUrl(url, "http", "/x/y/z", "example.com", "a=b#s", "s", 123, "user", "password")
    #     self.assertEqual(
    #         str(url), address
    #     )

    # """
    # The `Url` class should not serialize an address with invalid slashes.
    # """
    # def test_to_string_missing_slash(self):
    #     with self.assertRaises(Exception) as context:
    #         url = Url("invalid_url")
    #     self.assertEqual(str(context.exception), "Invalid URL - no scheme specified.")

    # """
    # The `Url` class should not serialize an empty address.
    # """
    # def test_empty(self):
    #     with self.assertRaises(Exception) as context:
    #         url = Url("")
    #     self.assertEqual(str(context.exception), "Invalid URL - no scheme specified.")

if __name__ == "__main__":
    unittest.main()
