# config: utf-8

import subprocess

def exe_cmd(cmd):
    '''
    :param cmd: str 実行コマンド
    :rtype generator
    :return: 標準出力ジェネレータ
    '''

    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    with proc.stdout as f_stdout:
        for line in f_stdout:
            if line:
                yield line.strip()
            else:
                if proc.poll() is not None:
                    yield proc.poll()
