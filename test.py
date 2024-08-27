from ajango.server.worker import Worker
import re

# test = Worker()
def dict_plactice():
    kk={"w":10, "e":100}
    kk.update({"w": 5000})
    kk["know"] = 9900
    kk["you"] = 1010

    for i, k in kk.items():
        print(f"res: {i}  {k}")

def re_plactice():
    url_pattern = "user/<ccc_id>/profile"
    # re_pattern = re.sub(r"z(.+?)l", r"(?P<\1>[^/]+)", url_pattern)
    re_pattern = re.sub(r"<(.+?)>", r"(?P<\1>[^/]+)", url_pattern)
    print(re_pattern)


if __name__ == "__main__":
    re_plactice()
    # dict_plactice()