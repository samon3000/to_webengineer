import urllib.parse
from datetime import datetime
from pprint import pformat
import random


from ajango.http.request import HTTPRequest
from ajango.http.response import HTTPResponse
from templates.render import render


def now(request: HTTPRequest) -> HTTPResponse:

    context = {"now": datetime.now()}
    body = render("now.html", context)
    
    return HTTPResponse(body = body)
  
def show_request(request: HTTPRequest) -> HTTPResponse:
    
    context = {
        "request": request,
        "headers": pformat(request.headers),
        "body": request.body.decode("utf-8", "ignore"),
        }
    body = render("show_request.html", context)

    return HTTPResponse(body = body)


def parameters(request: HTTPRequest) -> HTTPResponse:
    
    if request.method == "GET":
        body = b"<html><body><h1>405 Method Not Allowed</h1></body></html>"

        return HTTPResponse(body=body, status_code=405)

    elif request.method == "POST":
        # URLエンコードされた文字列を辞書へパースする
        context = {"params": urllib.parse.parse_qs(request.body.decode())}
        body = render("parameters.html", context)

        return HTTPResponse(body=body)


def user_profile(request: HTTPRequest) -> HTTPResponse:

    context = {"user_id": request.params["user_id"]}
    body = render("user_profile.html", context)

    return HTTPResponse(body=body)

def safe(request: HTTPRequest) -> HTTPResponse:

    however =["※ 但し、株主の利益を除く。", "但し、公共の福祉に反しない限り。"]

    context = {"however": however[random.randint(0,1)]}
    body = render("safe.html", context)

    return HTTPResponse(body=body)

def set_cookie(request: HTTPRequest) -> HTTPResponse:
    return HTTPResponse(cookies={"username": "Kato"})

def login(request: HTTPRequest) -> HTTPResponse:
    if request.method == "GET":
        body = render("login.html", {})
        return HTTPResponse(body=body)
    elif request.method == "POST":
        post_params = urllib.parse.parse_qs(request.body.decode())
        username = post_params["username"][0]
        email = post_params["email"][0]

        return HTTPResponse(
            headers={'Location': "/welcome"}, cookies={"username": username, "email": email}, status_code=302
        )

def welcome(request: HTTPRequest) -> HTTPResponse:
    
    # print(request.cookies)
    if "username" not in request.cookies:
        return HTTPResponse(status_code=302, headers={"Location": "/login"})

    username = request.cookies["username"]
    email = request.cookies["email"]    
    body = render("welcome.html", {"username": username, "email": email})

    return HTTPResponse(body=body)