from typing import Callable, Optional

from ajango.http.request import HTTPRequest
from ajango.http.response import HTTPResponse
from ajango.views.static import static
from urls import url_patterns

class URLResolver:
    def resolve(self, request: HTTPRequest) -> Callable[[HTTPRequest],HTTPResponse]:
        for url_pattern in url_patterns:
            match = url_pattern.match(request.path)
            if match:

                request.params.update(match.groupdict())
                return url_pattern.view

        return static