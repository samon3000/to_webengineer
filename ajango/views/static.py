import os 
import traceback

import settings
from ajango.http.request import HTTPRequest
from ajango.http.response import HTTPResponse

def static(request: HTTPResponse) -> HTTPResponse:

    if request.path == "/":
        request.path = "/index.html"

    try:
        static_root = getattr(settings, "STATIC_ROOT")

        # pathの先頭の/を削除し、相対パスにしておく
        relative_path = request.path.lstrip("/")
        static_file_path = os.path.join(static_root, relative_path)

        with open(static_file_path, "rb") as f:
            response_body = f.read()
        
        content_type = None
        return HTTPResponse(body = response_body, content_type = content_type, status_code = 200)
    
    except OSError:
        # レスポンスを取得できなかった場合は、ログを出力して404を返す
        traceback.print_exc()
        response_body = b"<html><body><h1>404 Not Found</h1></body></html>"
        content_type = "text/html; charset=UTF-8"
        return HTTPResponse(body = response_body, status_code = 404)
        # return HTTPResponse(body = response_body, content_type = content_type, status_code = 404)