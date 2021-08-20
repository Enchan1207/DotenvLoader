#
# DotenvLoader 実体
#
import os, dotenv

def load_dotenv(path: str):
    # pathを絶対パスに変換しておく
    path = os.path.abspath(path)

    # 対象ディレクトリのファイル一覧を取得し
    if not os.path.isdir(path):
        path = os.path.dirname(path)
    dir_lists = os.listdir(path)

    # dotenvファイルを絞り込む
    dotenv_candidates = [os.path.relpath(f"{path}/{name}", start=path) for name in list(filter(
        lambda path: os.path.isfile(path), filter(lambda path: path.endswith(".env"), dir_lists)))]

    # 文字数の少ない順にソート (これによりどんな環境でも.envが先に読まれるようになる…はず)
    dotenv_candidates = sorted(dotenv_candidates, key=lambda name: len(name))

    # dotenvモジュールに投げる
    for path in dotenv_candidates:
        dotenv.load_dotenv(path, override=True)
