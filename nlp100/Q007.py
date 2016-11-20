# config: utf-8

def Q_007():
    """ 07. テンプレートによる文生成
    引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
    さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
    """

    return template_sent(12, '気温', 22.4)

def template_sent(x, y, z):
    """ テンプレート文を出力
    x,y,zを可変部分として、"x時のyはz"という文を出力する
    """
    return '{0}時の{1}は{2}'.format(x,y,z)
