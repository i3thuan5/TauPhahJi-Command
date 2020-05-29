import json
from urllib.parse import urlencode
from http.client import HTTPSConnection


def tàuphahjī(漢羅):
    conn = HTTPSConnection(
        "hokbu.ithuan.tw"
    )
    tshamsoo = urlencode({
        'taibun': 漢羅,
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
