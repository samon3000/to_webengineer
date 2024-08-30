import os 

# 実行ファイルのあるディレクトリ
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(BASE_DIR, "static")

TEMPLATES_ROOT = os.path.join(BASE_DIR, "templates")