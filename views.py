import textwrap
import urllib.parse
from datetime import datetime
from pprint import pformat

from ajango.http.request import HTTPRequest
from ajango.http.response import HTTPResponse
from templates.render import render


def now(request: HTTPRequest) -> HTTPResponse:

    context = {"now": datetime.now()}
    body = render("now.html", context)
    content_type = "text/html; charset=UTF-8"
    status_code = 200
    
    return HTTPResponse(body = body, content_type = content_type, status_code = status_code)
  
def show_request(request: HTTPRequest) -> HTTPResponse:
# def show_request(
#     method: str,
#     path: str,
#     http_version: str,
#     request_header: dict,
#     request_body: bytes,
# ) -> Tuple[byts, Optional[str], str]:
    html = f"""\
        <!doctype html>
        <html lang="ja">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>NueServer</title>
        <link rel="stylesheet" href="https://unpkg.com/modern-css-reset/dist/reset.min.css" />
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
        <link rel="stylesheet" href="css/index.css">
        </head>
        <body>
        <div class="text-bg-secondary p-2 mb-3" style="">
            <h1 class="card-header">Request</h1>
        </div>
        <h2>Request Line:</h2>
        <p>
            {request.method} {request.path} {request.http_version}
        </p>
        <h2>Headers:</h2>
        <pre>{pformat(request.headers)}</pre>
        <h2>Body:</h2>
        <pre>{request.body.decode("utf-8", "ignore")}</pre>

        </body>
        </html>
    """
    body = textwrap.dedent(html).encode()
    content_type = "text/html; charset=UTF-8"
    status_code = 200
    
    return HTTPResponse(body = body, content_type = content_type, status_code = status_code)

def parameters(request: HTTPRequest) -> HTTPResponse:
#     method: str,
#     request_body: bytes,
# ) -> Tuple[bytes, Optional[str], str]:
    if request.method == "GET":
        body = b"<html><body><h1>405 Method Not Allowed</h1></body></html>"
        content_type = "text/html; charset=UTF-8"
        status_code = 405

    elif request.method == "POST":
        # URLエンコードされた文字列を辞書へパースする
        post_params = urllib.parse.parse_qs(request.body.decode())
        html = f"""\
            <html>
            <body>
                <h1>Parameters:</h1>
                <pre>{pformat(post_params)}</pre>
            </body>
            </html>
        """
        body = textwrap.dedent(html).encode()
        content_type = "text/html; charset=UTF-8"
        status_code = 200
    
    return HTTPResponse(body = body, content_type = content_type, status_code = status_code)

def user_profile(request: HTTPRequest) -> HTTPResponse:
    user_id = request.params["user_id"]
    html = f"""\
        <html>
        <body>
            <h1>プロフィール</h1>
            <p>ID: {user_id}</p>
        </body>
        </html>
    """
    body = textwrap.dedent(html).encode()
    content_type = "text/html; charset=UTF-8"
    status_code = 200

    return HTTPResponse(body=body, content_type=content_type, status_code=status_code)