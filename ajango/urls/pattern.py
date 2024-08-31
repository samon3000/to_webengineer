import re
from re import Match
from typing import Callable, Optional

from ajango.http.request import HTTPRequest
from ajango.http.response import HTTPResponse

class URLPattern:
    pattern: str
    view: Callable[[HTTPRequest], HTTPResponse]

    def __init__(self, pattern: str, view: Callable[[HTTPRequest], HTTPResponse]):
        self.pattern = pattern
        self.view = view

    def match(self, path: str) -> Optional[Match]:
        # URLパターンを正規表現パターンに変換する
        # ex) '/user/<user_id>/profile' => '/user/(?P<user_id>[^/]+)/profile'
        # user_id をnameとするdictとして、"/"以外の文字列
        # そうでなければ　self.patternを入れる
        pattern = re.sub(r"<(.+?)>", r"(?P<\1>[^/]+)", self.pattern)
        # print(f"pattern: {pattern}")
        # print(re.match(pattern, path))
        return re.match(pattern, path)
