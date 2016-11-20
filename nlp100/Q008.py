# coding: utf-8

def Q_008(in_str):
    """ 08. 暗号文
    与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
        ・英小文字ならば(219 - 文字コード)の文字に置換
        ・その他の文字はそのまま出力
    この関数を用い，英語のメッセージを暗号化せよ．
    """

    return cipher(in_str)

def cipher(data):

    # 普通に書いた場合
#    out_data = ''
#    for char in data:
#        if char.islower():
#            out_data += chr(219 - ord(char))
#        else:
#            out_data += char

    # 1行でも書ける
    return ''.join([c if not c.islower() else chr(219 - ord(c)) for c in data])

