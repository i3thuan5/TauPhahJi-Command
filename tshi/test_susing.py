from tauphahji_cmd import sûsìng
from unittest import TestCase


class SuSing(TestCase):
    def test_kio(self):
        kiatko = sûsìng('逐-家｜tak8-ke1 做-伙｜tso3-hue2 來｜lai5')
        self.assertEqual(kiatko[0], 'Nh')

    def test_調符(self):
        kiatko = sûsìng('逐-家｜ta̍k-ke 做-伙｜tsò-hué 來｜lâi')
        self.assertEqual(kiatko[0], 'Nh')
