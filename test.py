import re
import os
from datetime import datetime

import settings
from ajango.server.worker import Worker
from ajango.http.response import HTTPResponse



def dict_practice():
    kk={"w":10, "e":100}
    kk.update({"w": 5000})
    kk["know"] = 9900
    kk["you"] = 1010

    for i, k in kk.items():
        print(f"res: {i}  {k}")

def re_practice():
    url_pattern = "user/<ccc_id>/profile"
    # re_pattern = re.sub(r"z(.+?)l", r"(?P<\1>[^/]+)", url_pattern)
    re_pattern = re.sub(r"<(.+?)>", r"(?P<\1>[^/]+)", url_pattern)
    print(re_pattern)

def ttt():
    return "ttt"

def sss():
    return "sss"

def format_practice():
    tt=500
    yyy="plokij"
    kkk={"/now": 500}
    print(f"000: {tt}")
    print(f"001: {ttt()}")
    print("002: {}".format(tt))
    dict_to_kwargs = {"now": ttt(), "low": sss()} 
    print("003: {now}  {low}".format(**dict_to_kwargs))
    # print("003: {now}  {low}".format(**dict_to_kwargs))
    # print("003: {now}  {low}".format(now = ttt(), low = sss()))
    # print(article.format(now=datetime.now()))
    
    # print(render(settings.TEMPLATES_ROOT + "/now.html", {"now": datetime.now()}))

def re_match_practice():
    path = "/nowookji"
    pathnow = "/now"
    pattern = r"/now$"
    print(f"/nowookji  {re.match(pattern, path)}")
    print(f"/now  {re.match(pattern, pathnow)}")

def render(template_path: str, context: dict):
    with open(template_path) as f:
        template = f.read()

    return template.format(**context)  # ** は、kwargs(辞書型を受け取って、キーワード引数として使う) として受け取ってくださいね　という意味。

def kwargs_practice(a, b, **kwargs):
    print(a)
    print(b)
    # print(args)
    print(kwargs)

class TempResource():
    str = "good"
    int = 90
    list = ["cavendish", "banana"]
    dict = {"light": 500, "fulbright": 40, "ko": 30, "tko": 20}



def opentest():
    with open("./sandbox/to_webengineer/templates/now.html") as f:
        template = f.read()
        print(template)
    # print(os.getcwd())

def basedir():
    path = os.path.join(settings.TEMPLATES_DIR, "now.html")
    print(path)
    print(settings.BASE_DIR)
    print(type(settings.BASE_DIR))



if __name__ == "__main__":

    # temp_resource = TempResource()
    # kwargs_practice(temp_resource.str, temp_resource.int, **temp_resource.dict)

    # format_practice()
    # basedir()
    # opentest()
    # re_practice()
    # dict_practice()

    # test = HTTPResponse()
    # print(test.content_type)

    re_match_practice()

