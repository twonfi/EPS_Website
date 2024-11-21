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
    api_url = f'https://{config["app"]}.appazur.com/api'
    file_path = os.path.abspath(config['file_path'])


def api(endpoint: str, method: str = 'GET', return_json: bool = True) \
        -> dict | str:
    r_text = requests.request(
        method, f'{api_url}/{endpoint}', headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                          ' AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/131.0.0.0 Safari/537.36'
        }).text
    if return_json:
        return json.loads(r_text)
    else:
        return r_text

def write_file(path, content):
    with open(path, 'w', encoding='UTF-8') as f:
        f.write(content)
    print(f'Wrote {len(bytes(content, "UTF-8"))} bytes to {path} ')


# Initialize Jinja and set everything up
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates/'))
templates = {
    'messages': jinja_env.get_template('messages.html'),
    # 'calendar': jinja_env.get_template('calendar.html'),
}

# Ready, set, go!

# Messages
if 'messages' in config['save']:
    messages = api('msg')

    if 'json' in config['save']['messages']:
        write_file(f'{file_path}/messages.json', str(messages))

    if 'html' in config['save']['messages']:
        for message in messages:
            # noinspection PyTypeChecker
            message['text_with_br'] = re.sub('\r?\n', '<br>',
                message['text'])
            # noinspection PyTypeChecker
            message['text'] = str(escape(message['text']))

        html_text = templates['messages'].render(
            messages=messages,
            app_name=config['app'],
            last_update=datetime.now(timezone.utc).strftime('%A, %B %-d, %Y'
                                                            ' at %-I:%M:%S %P'),
            footer=config['footer'],
        )
        write_file(f'{file_path}/messages.html', html_text)

# Calendar
if 'calendar' in config['save']:
    calendar = api('a')

    if 'json' in config['save']['calendar']:
        write_file(f'{file_path}/calendar.json', str(calendar))

    if 'html' in config['save']['calendar']:
        print('HTML calendar not yet supported')  # placeholder
        ...
