from dataclasses import dataclass, field
from typing import Optional, Union

@dataclass
class HTTPResponse:
    body: Union[bytes, str] = b""
    status_code: int = 200
    headers: dict = field(default_factory=dict)
    cookies: dict = field(default_factory=dict)
    content_type: Optional[str] = None  # デフォルトをhtmlにできないのはstaticの返しが特殊だからとのこと。static内で判別できるようにすれば治せる
