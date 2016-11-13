#!/usr/bin/env python
# config: utf-8

## 00. 文字列の逆順
# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

# メイン処理
def main():

    # 入力文字列
    input_str = 'stressed'
    # 逆順の文字列取得
    output_str = input_str[::-1]

    # 結果確認用に表示
    print('input = {}'.format(input_str))
    print('output = {}'.format(output_str))

# 実行
if __name__ == '__main__':
    main()
