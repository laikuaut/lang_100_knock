# config: utf-8

def Q_008_1(in_str):
    """ 08. 暗号文
    与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
        ・英小文字ならば(219 - 文字コード)の文字に置換
        ・その他の文字はそのまま出力
    この関数を用い，英語のメッセージを暗号化・復号化せよ．
    """

    data = encode(in_str)
    return data

def Q_008_2(in_str):
    """ 08. 暗号文
    与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
        ・英小文字ならば(219 - 文字コード)の文字に置換
        ・その他の文字はそのまま出力
    この関数を用い，英語のメッセージを暗号化・復号化せよ．
    """

    data = decode(in_str)
    return data


def encode(data):
    out_data = ''
    for char in data:
        if char.islower():
            out_data += chr(219 - ord(char))
        else:
            out_data += char
    return out_data

def decode(data):
    out_data = ''
    for char in data:
        if chr(219 - ord(char)).islower():
            out_data += chr(219 - ord(char))
        else:
            out_data += char
    return out_data
