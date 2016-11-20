# coding: utf-8

import shlex
import subprocess

def exe_cmd(cmd):
    ''' コマンド実行関数
    リダイレクト時はファイルへの出力のため、ジェネレータなしでコマンド戻り値返却
    リダイレクトなしの場合は、1行単位の標準出力をジェネレータで返す。
    :param cmd: str 実行コマンド
    :rtype generator
    :return: 標準出力(1行単位) + コマンド戻り値
    :rtype int
    :return: コマンド戻り値
    '''

    cmd_list = shlex.split(cmd)
    if '>' in cmd_list or '>>' in cmd_list:
        # リダイレクト実行
        proc = subprocess.Popen(cmd, shell=True, universal_newlines=True)
        while proc.poll() is None: pass
        yield proc.poll()
    else:
        # リダイレクトなし実装
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        while proc.poll() is None: pass
        with proc.stdout as f_stdout:
            for line in f_stdout:
                if line:
                    yield line.strip()
                else:
                    yield proc.poll()
