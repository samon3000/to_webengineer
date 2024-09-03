from dataclasses import dataclass
from typing import Optional, Union

@dataclass
class HTTPResponse:
    body: Union[bytes, str] = b""
    status_code: int = 200
    headers: dict = None
    cookies: dict = None
    content_type: Optional[str] = None  # デフォルトをhtmlにできないのはstaticの返しが特殊だからとのこと。static内で判別できるようにすれば治せる
