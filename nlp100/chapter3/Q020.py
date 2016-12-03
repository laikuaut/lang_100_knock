# coding: utf-8

import json

def Q_020():
    """ 20. JSONデータの読み込み
    Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
    """
    with open('data/jawiki-country.json', 'r', encoding='utf-8') as rf, \
         open('data/Britain.txt', 'w') as wf:
        for line in rf:
            data = json.loads(line)
            if data['title'] == 'イギリス':
                print(data['text'], file=wf)
