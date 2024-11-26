import json
import os
import re
from datetime import datetime, timezone

import jinja2
import requests
from markupsafe import escape

try:
    with open('config.json') as file:
        config_json = file.read()
except FileNotFoundError:
    raise FileNotFoundError('config.json not found; use config_template.json')
else:
    config = json.loads(config_json)
    file_path = os.path.abspath(config['file_path'])


def write_file(path, content):
    with open(file_path + path, 'w', encoding='UTF-8') as f:
        f.write(content)
    print(f'Wrote {len(bytes(content, "UTF-8"))} bytes to {path} ')


# Initialize Jinja and set everything up
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('pods/'))
templates = {
    'messages': jinja_env.get_template('messages.html'),
}
