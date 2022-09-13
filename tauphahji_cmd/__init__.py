import json
from urllib.parse import quote
from urllib.parse import urlencode
from http.client import HTTPSConnection


def tàuphahjī(漢羅, **tshamsoo):
    conn = HTTPSConnection(
        "hokbu.ithuan.tw"
    )
    tshamsoo = urlencode({
        'taibun': 漢羅,
        **tshamsoo,
    })
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"
    }
    conn.request(
        "POST",
        "/tau",
        tshamsoo,
        headers,
    )

    responseStr = conn.getresponse().read().decode('utf-8')
    conn.close()
    return json.loads(responseStr)


def sûsìng(hunsu):
    conn = HTTPSConnection(
        'susing.ithuan.tw',
    )
    conn.request(
        "GET",
        "/{}".format(quote(hunsu)),
    )
    responseStr = conn.getresponse().read().decode('utf-8')
    conn.close()
    responsejson = json.loads(responseStr)
    詞性陣列 = [x[1] for x in responsejson]
    return 詞性陣列
