import json
import os
import sys
import re
import shutil
from datetime import datetime, timezone

import jinja2

print(datetime.now(timezone.utc).isoformat(), sys.version)


def write_file(full_path, content):
    with open(full_path, 'w', encoding='UTF-8') as f:
        f.write(content)
    print('Wrote %d bytes to %s ' % (len(bytes(content, "UTF-8")), full_path))


jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates/'))
templates = {
    'departments': jinja_env.get_template('departments.html'),
    'clubs': jinja_env.get_template('clubs.html'),
    'messages': jinja_env.get_template('editable/orca-news/messages.html'),
    'edit-requests': jinja_env.get_template('editable/edit-requests.html')
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

# 404
write_file(
    file_path + '/404.html',
    jinja_env.get_template('editable/404.html').render()
)

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

# Edit requests
write_file('%s/edit-requests.html' % file_path,
    templates['edit-requests'].render())

# Orca News stubs
# Messages
write_file('%s/orca-news/messages.html' % file_path,
    templates['messages'].render())
