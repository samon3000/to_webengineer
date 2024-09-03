import os

import settings

# 変数を埋め込んだhtmlを返す
def render(template_name: str, context: dict):
    template_path = os.path.join(settings.TEMPLATES_DIR, template_name)
    # print(template_path)
    with open(template_path) as f:
        template = f.read()
    
    return template.format(**context)