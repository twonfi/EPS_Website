import json
import os
import sys
import re
import shutil
from datetime import datetime, timezone

import jinja2
import requests
from markupsafe import escape

print(datetime.now(timezone.utc).isoformat(), sys.version)


def write_file(full_path, content):
    with open(full_path, 'w', encoding='UTF-8') as f:
        f.write(content)
    print('Wrote %d bytes to %s ' % (len(bytes(content, "UTF-8")), full_path))


jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates/'))
templates = {
    'departments': jinja_env.get_template('departments.html'),
    'clubs': jinja_env.get_template('clubs.html'),
    'messages': jinja_env.get_template('orca-news/messages.html'),
}

file_path = '../site'

# Delete existing files, so that deleted data doesn't resurface
for directory in ['departments']:
    for file in os.scandir(os.path.abspath('../site/' + directory)):
        path = os.path.join(directory, file.path)
        if os.path.isfile(path) and file.path[-1] != '_':
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
print('Deleted old files')

# Departments
for dept_filename in os.scandir('pods/departments'):
    with open(dept_filename.path, 'r') as file:
        dept = json.loads(file.read())

    html_text = templates['departments'].render(
        dept=dept,
        last_update=datetime.now(timezone.utc).strftime('%A, %B %-d, %Y'
                                                        ' at %-I:%M:%S %p'),
    )
    write_file(os.path.abspath('%s/departments/' % file_path + re.sub(".json$",
        ".html", os.path.basename(dept_filename.path))), html_text)

# Clubs
with open('pods/clubs.json', 'r') as file:
    clubs = json.loads(file.read())

html_text = templates['clubs'].render(
    clubs=clubs,
    last_update=datetime.now(timezone.utc).strftime('%A, %B %-d, %Y'
                                                    ' at %-I:%M:%S %p'),
)
write_file(os.path.abspath('%s/clubs.html') % file_path, html_text)


# Orca News
def api(endpoint: str, method: str = 'GET', return_json: bool = True) \
        -> dict | str:
    r_text = requests.request(
        method, f'https://elginpark.appazur.com/api/{endpoint}', headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                          ' AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/131.0.0.0 Safari/537.36'
        }).text
    if return_json:
        return json.loads(r_text)
    else:
        return r_text

# Messages
messages = api('msg')

write_file('%s/orca-news/messages.json' % file_path, json.dumps(messages))
messages = api('msg')

write_file('%s/orca-news/messages.json' % file_path, json.dumps(messages))

for message in messages:
    # noinspection PyTypeChecker
    message['text_with_br'] = re.sub('\r?\n', '<br>',
        message['text'])
    # noinspection PyTypeChecker
    message['text'] = str(escape(message['text']))
for message in messages:
    # noinspection PyTypeChecker
    message['text_with_br'] = re.sub('\r?\n', '<br>',
        message['text'])
    # noinspection PyTypeChecker
    message['text'] = str(escape(message['text']))

html_text = templates['messages'].render(
    messages=messages,
    last_update=datetime.now(timezone.utc).strftime('%A, %B %-d, %Y'
                                                    ' at %-I:%M:%S %p'),
)
write_file('%s/orca-news/messages.html' % file_path, html_text)

# Calendar
calendar = api('a')
write_file('%s/orca-news/calendar.json' % file_path, json.dumps(calendar))
