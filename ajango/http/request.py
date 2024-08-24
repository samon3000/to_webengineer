from dataclasses import dataclass, field

@dataclass
class HTTPRequest:
    path: str
    method: str
    http_version: str
    body: bytes
    headers: dict = field(default_factory=dict)

    # def __init__(
    #         self, path: str = "", method: str = "", http_version: str = "", headers: dict = None, body: bytes = b""
    # ):
    #     if headers is None:
    #         headers = {}

    #     self.path = path
    #     self.method = method
    #     self.http_vertion = http_version
    #     self.headers = headers
    #     self.body = body