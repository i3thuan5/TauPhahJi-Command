import json
from urllib.parse import quote
from http.client import HTTPSConnection
import ssl
from pip._vendor.urllib3 import response


def tàuphahjī(漢羅):
    conn = HTTPSConnection(
        "xn--lhrz38b.xn--v0qr21b.xn--kpry57d", context=ssl._create_unverified_context()
    )
    conn.request(
        "GET",
        "/{}?{}={}&{}={}".format(
            quote('標漢字音標'),
            quote('查詢腔口'),
            quote('台語'),
            quote('查詢語句'),
            quote(漢羅),
        ),
    )

    responseStr = conn.getresponse().read().decode('utf-8')
    return json.loads(responseStr)
