# Tau-Phah-Ji-Command
鬥拍字的指令直接包做一个套件

## Tau
因為新版本猶未deploy到PyPI，暫時先用zip。
```bash
pip install https://github.com/i3thuan5/TauPhahJi-Command/archive/refs/heads/master.zip
```

## Ing
```python
>>> from tauphahji_cmd import tàuphahjī
>>> tàuphahjī('gau5 tsa2\nlâi-khì.')
{
  ## Tsuân-pōo
  'kiatko': [
    {'漢字': '𠢕早', 'KIP': 'gâu-tsá', '分詞': '𠢕-早｜gâu-tsá'},
    {'漢字': '來去。', 'KIP': 'lâi-khì.', '分詞': '來-去｜lâi-khì 。｜.'}
  ],
  ## Thâu-tsi̍t-kú
  '漢字': '𠢕早',
  'KIP': 'gâu-tsá',
  '分詞': '𠢕-早｜gâu-tsá'
}
```
