import json
from urllib.parse import quote
from http.client import HTTPSConnection


def tàuphahjī(漢羅):
    conn = HTTPSConnection(
        "xn--lhrz38b.xn--v0qr21b.xn--kpry57d"
    )
    conn.request(
        "GET",
        "/{}?{}={}&{}={}".format(
            quote('標漢字音標'),
            quote('查詢腔口'),
            quote('台語'),
            quote('查詢語句'),
            quote(漢羅),
        )
    )
    return json.loads(conn.getresponse().read())['分詞']