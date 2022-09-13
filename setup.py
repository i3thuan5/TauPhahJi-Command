from distutils.core import setup

版本 = '0.1.0'

setup(
    name='Tau-Phah-Ji-Command',
    version=版本,
    author='薛丞宏',
    author_email='hong@ithuan.tw',
    url='https://github.com/i3thuan5/Tau-Phah-Ji-Command',
    py_modules=['tauphahji_cmd'],
    description='用指令叫鬥拍字',
    keywords=[
        '語料庫', '語言合成', '機器翻譯',
        'Taiwan', 'Natural Language', 'Corpus',
        'Text to Speech', 'TTS',
        'Machine Translateion',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
        "License :: OSI Approved :: MIT License",
    ],
    setup_requires=['wheel']
)
