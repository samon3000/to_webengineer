from dataclasses import dataclass
from typing import Optional

@dataclass
class HTTPResponse:
    status_code: int
    body: bytes
    content_type: Optional[str]