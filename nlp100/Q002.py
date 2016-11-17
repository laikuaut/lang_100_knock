# config: utf-8

def Q_002():
    """ 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
    「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
    """

    # 文字列
    str1 = 'パトカー'
    str2 = 'タクシー'

    # 交互に連結
    result = ''
    for char1, char2 in zip(str1, str2):
        result += char1 + char2

    return result
