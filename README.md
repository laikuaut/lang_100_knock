# nlp100

[言語処理100本ノック](http://www.cl.ecei.tohoku.ac.jp/nlp100/)をソースコードを書いてみる。

## 回答済み

00.文字列の逆順  
01.「パタトクカシーー」  
02.「パトカー」＋「タクシー」＝「パタトクカシーー」  
03.円周率  
04.元素記号  
05.n-gram  
06.集合  
07.テンプレートによる文生成  
08.暗号文  
09.Typoglycemia  
10.行数のカウント  
11.タブをスペースに置換  
12.1列目をcol1.txtに，2列目をcol2.txtに保存  
13.col1.txtとcol2.txtをマージ  
14.先頭からN行を出力  
15.末尾のN行を出力  
16.ファイルをN分割する  
17.１列目の文字列の異なり  
18.各行を3コラム目の数値の降順にソート  
19.各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる  
20.JSONデータの読み込み  
21.カテゴリ名を含む行を抽出  
22.カテゴリ名の抽出  
23.セクション構造  
24.ファイル参照の抽出  
25.テンプレートの抽出  
26.強調マークアップの除去  
27.内部リンクの除去  
28.MediaWikiマークアップの除去  
29.国旗画像のURLを取得する  

## 未回答

30.形態素解析結果の読み込み  
31.動詞  
32.動詞の原形  
33.サ変名詞  
34.「AのB」  
35.名詞の連接  
36.単語の出現頻度  
37.頻度上位10語  
38.ヒストグラム  
39.Zipfの法則  
40.係り受け解析結果の読み込み（形態素）  
41.係り受け解析結果の読み込み（文節・係り受け）  
42.係り元と係り先の文節の表示  
43.名詞を含む文節が動詞を含む文節に係るものを抽出  
44.係り受け木の可視化  
45.動詞の格パターンの抽出  
46.動詞の格フレーム情報の抽出  
47.機能動詞構文のマイニング  
48.名詞から根へのパスの抽出  
49.名詞間の係り受けパスの抽出  
50.文区切り  
51.単語の切り出し  
52.ステミング  
53.Tokenization  
54.品詞タグ付け  
55.固有表現抽出  
56.共参照解析  
57.係り受け解析  
58.タプルの抽出  
59.S式の解析  
60.KVSの構築  
61.KVSの検索  
62.KVS内の反復処理  
63.オブジェクトを値に格納したKVS  
64.MongoDBの構築  
65.MongoDBの検索  
66.検索件数の取得  
67.複数のドキュメントの取得  
68.ソート  
69.Webアプリケーションの作成  
70.データの入手・整形  
71.ストップワード  
72.素性抽出  
73.学習  
74.予測  
75.素性の重み  
76.ラベル付け  
77.正解率の計測  
78.5分割交差検定  
79.適合率-再現率グラフの描画  
80.コーパスの整形  
81.複合語からなる国名への対処  
82.文脈の抽出  
83.単語／文脈の頻度の計測  
84.単語文脈行列の作成  
85.主成分分析による次元圧縮  
86.単語ベクトルの表示  
87.単語の類似度  
88.類似度の高い単語10件  
89.加法構成性によるアナロジー  
90.word2vecによる学習  
91.アナロジーデータの準備  
92.アナロジーデータへの適用  
93.アナロジータスクの正解率の計算  
94.WordSimilarity-353での類似度計算  
95.WordSimilarity-353での評価  
96.国名に関するベクトルの抽出  
97.k-meansクラスタリング  
98.Ward法によるクラスタリング  
99.t-SNEによる可視化  

## 入力データ

```Bash
mkdir data
cd data
# hightemp.txt
wget http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt
wget http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz
gzip -d jawiki-country.json.gz
```

## テスト実行

```
python -m unittest test/test_nlp100.py
```

## その他

### Q029のためのライブラリ

Wikipedia APIを呼び出すために、requestsをインストールしておく。

```Bash
pip install requests
```

### mecabをインストール

4章データmecabを用いた形態素解析結果を使うため、インストールする。

#### 本体をインストール

```Bash
wget "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE" -O mecab-0.996.tar.gz
tar zxvf mecab-0.996.tar.gz
cd mecab-0.996/
./configure --prefix=${HOME}/install/
make
make install
```

#### 辞書をインストール

```Bash
wget "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM" -O mecab-ipadic-2.7.0-20070801.tar.gz
tar zxvf mecab-ipadic-2.7.0-20070801.tar.gz
cd mecab-ipadic-2.7.0-20070801/
./configure --prefix=${HOME}/install/mecab-ipadic-2.7.0/ --with-mecab-config=${HOME}/install/mecab-0.996/bin/mecab-config --with-charset=utf8
make
make install
```

#### 実行例

```Bash
~/install/mecab-0.996/bin/mecab
明日は晴れ
明日    名詞,副詞可能,*,*,*,*,明日,アシタ,アシタ
は      助詞,係助詞,*,*,*,*,は,ハ,ワ
晴れ    名詞,一般,*,*,*,*,晴れ,ハレ,ハレ
EOS
```

#### 4章用のデータ作成

```Bash
~/install/mecab-0.996/bin/mecab -o data/neko.txt.mecab < data/neko.txt
```
