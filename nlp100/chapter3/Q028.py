# coding: utf-8

import re

class BasisInfo(object):

    def __init__(self):
        # 基礎情報辞書
        self.info_data = {}

        # 基礎情報開始行判定用正規表現(regex for checking basis info start line.)
        self.__regex_start_basis_info = re.compile(r'{{基礎情報 ')

        # フィード判定用正規表現(regex for deciding feed line.)
        self.__regex_start_feed = re.compile(r'^\|')

        # 基礎情報終了行判定用正規表現(regex for checking basis info end line.)
        self.__regex_end_basis_info = re.compile(r'^}}$')

        # 斜体と強調
        self.__regex_italic_and_bold = re.compile(r"(?:'{5}|'{2,3})(.+?)(?:'{5}|'{2,3})")

        # 内部リンク判定用正規表現
        self.__regex_inner_link = re.compile(r'(.*)(\[\[)([^:]+?)(\]\])(.*)')

        # 参照ファイル名抜き出し
        self.__regex_image_file = re.compile(r'\[\[(?:File:|ファイル:)(.+?)\|.+\]\]')

        # langTemplate
        self.__regex_lang_template = re.compile(r'\{\{lang\|[a-z]{2}\|(.+?)\}\}')

        # マークアップ削除正規表現
        self.__regex_remove_markup = [
                re.compile(r'\*+'),
                re.compile(r'<ref.*?>[\n\w\W]+</ref>'),
                re.compile(r'<[a-z]+.*?/>'),
                ]

    def readFile(self, file_path):
        with open(file_path, 'r') as f:
            info_flag = False
            for line in f:
                if self.__regex_start_basis_info.match(line):
                    info_flag = True
                    break
            for line in f:
                if self.__regex_end_basis_info.match(line):
                    break
                if self.__regex_start_feed.match(line):
                    key, value = line.rstrip().lstrip('|').split(' = ')
                    self.info_data[key] = self.__formatter(value) + "\n"
                else:
                    self.info_data[key] += self.__formatter(line.rstrip()) + "\n"
        for k, v in self.info_data.items():
            self.info_data[k] = self.__remove_markup(self.info_data[k])

    def __formatter(self, line):
        line = self.__emphasis_remove(line)
        line = self.__inner_link_remove(line)
        line = self.__extract_image_file_name(line)
        line = self.__extract_lang_template(line)
        return line

    def __emphasis_remove(self, line):
        while self.__regex_italic_and_bold.search(line):
            line = self.__regex_italic_and_bold.sub('\g<1>', line)
        return line

    def __extract_image_file_name(self,line):
        while self.__regex_image_file.search(line):
            line = self.__regex_image_file.sub('\g<1>', line)
        return line

    def __extract_lang_template(self,line):
        while self.__regex_lang_template.search(line):
            line = self.__regex_lang_template.sub('\g<1>', line)
        return line

    def __inner_link_remove(self, line):
        # 内部リンクを含んている間処理を継続
        while True:
            # 内部リンク判定
            matchObj = self.__regex_inner_link.search(line)
            if matchObj is None:
                break
            # グループ群取得
            groups = matchObj.groups()
            # 内部リンクの文字列部分を取得
            inner_string = groups[2]
            # 表示文字部分を取得(エスケープ等の考慮なし)
            inner_data = inner_string.split('|')
            inner_string = inner_data[1] if len(inner_data) > 1 else inner_data[0]

            # 整形済みの内部リンクを元の行へ反映( '[['前の文字列 + 内部リンク文字列 + ']]'後の文字列)
            line = groups[0] + inner_string + groups[4]
        return line

    def __remove_markup(self, value):
        for regex in self.__regex_remove_markup:
            while regex.search(value):
                value = regex.sub('', value)
        return value

def Q_028():
    """ 28. MediaWikiマークアップの除去
    27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
    注釈リンク : <ref>...</ref>全削除
    タグ : <br />など全削除
    ファイル参照 : [ファイル:]ファイル名に置換
    外部リンク : [http:// ]全削除
    リスト : *全削除
    言語テンプレート : {{lang|..|...}内容に置換
    """

    basis_info = BasisInfo()
    basis_info.readFile('data/Britain.txt')

    return basis_info.info_data



