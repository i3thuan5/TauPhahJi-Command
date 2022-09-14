# Tau-Phah-Ji-Command

鬥拍字的指令直接包做一个套件

## Tau

```bash
pip install Tau-Phah-Ji-Command
```

## Īng

### Phiau Tsuân-Hàn Tsuân-Lô

```python
>>> from tauphahji_cmd import tàuphahjī
>>> tàuphahjī('A-tsik gau5 tsa2\nlâi-khì.')
{
  # Tsuân-pōo
  'kiatko': [
    {'漢字': '阿叔𠢕早', 'KIP': 'a-tsik gâu-tsá', '分詞': '阿-叔｜a-tsik 𠢕-早｜gâu-tsá'},
    {'漢字': '來去。', 'KIP': 'lâi-khì.', '分詞': '來-去｜lâi-khì 。｜.'}
  ],
  # Thâu-tsi̍t-kú
  '漢字': '阿叔𠢕早',
  'KIP': 'a-tsik gâu-tsá',
  '分詞': '阿-叔｜a-tsik 𠢕-早｜gâu-tsá'
}
```

### Phiau Sû-sìng

```python
>>> from tauphahji_cmd import sûsìng
>>> sûsìng('逐-家｜ta̍k-ke 做-伙｜tsò-hué 來｜lâi 𨑨-迌｜tshit-thô ！｜!')
['Nh', 'D', 'D', 'VC', 'PUNC']
```
