from dataclasses import dataclass
from typing import Optional, Union

@dataclass
class HTTPResponse:
    body: Union[bytes, str]
    status_code: int = 200
    content_type: Optional[str] = None  # デフォルトをhtmlにできないのはstaticの返しが特殊だからとのこと。static内で判別できるようにすれば治せる
    

    # def __init__(self, status_code: int=200):
    #     self.status_code = status_code