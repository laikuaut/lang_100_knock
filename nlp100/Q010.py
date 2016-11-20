# config: utf-8

from util import util

def Q_010():
    """ 10. 行数のカウント
    行数をカウントせよ．確認にはwcコマンドを用いよ．
    """

    ite = util.exe_cmd('wc -l data/hightemp.txt')
    return list(ite)
