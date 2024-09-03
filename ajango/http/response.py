from dataclasses import dataclass
from typing import Optional, Union

@dataclass
class HTTPResponse:
    body: Union[bytes, str]
    status_code: int = 200
    headers: dict = None
    content_type: Optional[str] = None  # デフォルトをhtmlにできないのはstaticの返しが特殊だからとのこと。static内で判別できるようにすれば治せる
