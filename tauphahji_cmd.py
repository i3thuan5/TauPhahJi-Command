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


def liânKù(多元書寫, 欲連的key):
    if 欲連的key == '漢字':
        return liânHànjī(多元書寫)
    elif 欲連的key == '臺羅':
        return liânTâilô(多元書寫)


def liânHànjī(多元書寫):
    return ''.join([i['漢字'].replace('.', '。') for i in 多元書寫])


def liânTâilô(多元書寫):
    return '. '.join([i['臺羅'] for i in 多元書寫])
