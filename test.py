import re
import os
from datetime import datetime
import random

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

def random_practice():
    however = ["※ 但し、株主の利益を除く。", "※ 但し、公共の福祉に反しない限り。"]
    random_num = random.randint(0,8) % len(however)
    return however[random_num]

def compare_random():
    sub_regular = [0]*5
    sub_remainder = [0]*5
    test_times = 50000
    for i in range(test_times):
        first = random.randint(0,4)
        sub_regular[first] += 1
        second = random.randint(0,39) % 5
        sub_remainder[second] += 1
    # sub_regular = [99980, 100000, 100000, 100000, 100020]
    # print(sum(sub_regular))
    # print(sum(sub_remainder))
    print(".")
    return [sub_regular, var_score(sub_regular), sub_remainder, var_score(sub_remainder)]

def var_score(score):
    # 平均
    mean_score = sum(score) / len(score)
    # 偏差平方和
    dev_score = 0
    for i in score:
        dev_score += (i - mean_score)**2
    # 分散
    var_score = dev_score / len(score)

    return var_score

def multi_compare():
    var_regulars = []
    var_rimainders = []
    for i in range(10):
        res = compare_random()
        var_regulars.append(res[1])
        var_rimainders.append(res[3])
    mean_var_regular = sum(var_regulars) / len(var_regulars)
    mean_var_rimainder = sum(var_rimainders) / len(var_rimainders)
    res = {}
    res.update({"mean_var_regular": mean_var_regular, "mean_var_rimainder": mean_var_rimainder})

    return res

def multi_print(left=20, right= 15, **res:dict):
    for name, value in res.items():
        if value != str:
            value = "{:.2f}".format(value)
        print(f"{name.ljust(left)}{value}")





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

    # re_match_practice()

    # print(random_practice())
    # g = compare_random()
    # print(f"regular: {g[0]}\nvar: {g[1]}\nremainder: {g[2]}\nvar: {g[3]}")

    g = multi_compare()
    multi_print(**g)
    # print(f"\nregular: {g[0]}\nremainder: {g[1]}")
