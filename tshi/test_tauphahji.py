from tauphahji_cmd import tàuphahjī
from unittest import TestCase


class TauPhahJi(TestCase):
    def test_kio(self):
        kiatko = tàuphahjī('gau5 tsa2\nlâi-khì.')
        self.assertEqual(
            kiatko,
            {
              # Tsuân-pōo
              'kiatko': [
                {'漢字': '𠢕早', 'KIP': 'gâu-tsá', '分詞': '𠢕-早｜gâu-tsá'},
                {'漢字': '來去。', 'KIP': 'lâi-khì.', '分詞': '來-去｜lâi-khì 。｜.'}
              ],
              # Thâu-tsi̍t-kú
              '漢字': '𠢕早',
              'KIP': 'gâu-tsá',
              '分詞': '𠢕-早｜gâu-tsá'
            }
        )
