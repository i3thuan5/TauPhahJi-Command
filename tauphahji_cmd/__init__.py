import json
from urllib.parse import quote
from urllib.parse import urlencode
from http.client import HTTPSConnection

from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


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
        "/{}".format(quote(_tsuan_sooji(hunsu))),
    )
    responseStr = conn.getresponse().read().decode('utf-8')
    conn.close()
    responsejson = json.loads(responseStr)
    詞性陣列 = [x[1] for x in responsejson]
    return 詞性陣列


def _tsuan_sooji(hunsu):
    return (
        拆文分析器
        .分詞句物件(hunsu)
        .轉音(臺灣閩南語羅馬字拼音).看分詞()
    )
