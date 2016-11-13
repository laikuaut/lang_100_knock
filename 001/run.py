#!/usr/bin/env python
# config: utf-8

## 01. 「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

# メイン処理
def main():

    # 入力文字
    input_str = 'パタトクカシーー'

    # 文字列の1,3,5,7文字目を取得
    output_str = input_str[0::2]

    # 結果確認用に表示
    print('input = {}'.format(input_str))
    print('output = {}'.format(output_str))

# 実行
if __name__ == '__main__':
    main()
