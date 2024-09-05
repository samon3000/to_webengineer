from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class Cookie:
    name: str
    value: str
    expires: Optional[datetime] = None
    max_age: Optional[int] = 0
    domain: str = ""
    path: str = ""
    secure: bool = False
    http_only: bool = False
