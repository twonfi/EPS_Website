import json
import os
import sys
import re
import shutil
from datetime import datetime, timezone

import jinja2

debug_info = datetime.now(timezone.utc).isoformat(), sys.version

print(debug_info)

# Add noindex if run with --dev-build
if len(sys.argv) > 1 and sys.argv[1] == '--dev-build':
    dev_build = True
    print('Building with --dev-build: noindex and debug information added.')
else:
    dev_build = False


def write_file(full_path, content):
    with open(full_path, 'w', encoding='UTF-8') as f:
        f.write(content)
    print('Wrote %d bytes to %s ' % (len(bytes(content, "UTF-8")), full_path))


jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates/'))

def bob(template: jinja2.Template, params: dict = None) -> str:
    """Bob the builder, actually a renderer.

    :param template: Template object
    :type template: jinja2.Template
    :param params: Parameters to pass to template
    :type params: dict
    :return: str
    """
    if params is None:
        params = {}
    return template.render(
        dev_build=dev_build, debug_info=debug_info,
        last_update=datetime.now(timezone.utc).strftime('%A, %B %-d, %Y'
                                                        ' at %-I:%M:%S %p'),
        **params
    )

site_path = '../site'

# Delete existing files, so that deleted data doesn't resurface
for directory in ['departments']:
    for file in os.scandir(os.path.abspath('../site/' + directory)):
        path = os.path.join(directory, file.path)
        if os.path.isfile(path) and file.path[-1] != '_':
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
print('Deleted old files')

# index
write_file('%s/index.html' % site_path,
    bob(jinja_env.get_template('index.html')))

# 404
write_file('%s/404.html' % site_path,
    bob(jinja_env.get_template('404.html')))

# Departments
for dept_filename in os.scandir('pods/departments'):
    with open(dept_filename.path, 'r') as file:
        dept = json.loads(file.read())

    html_text = bob(jinja_env.get_template('departments.html'), {
        'dept': dept,
    })
    write_file(os.path.abspath('%s/departments/' % site_path + re.sub(".json$",
        ".html", os.path.basename(dept_filename.path))), html_text)

# Clubs
with open('pods/clubs.json', 'r') as file:
    clubs = json.loads(file.read())

html_text = bob(jinja_env.get_template('clubs.html'), {'clubs': clubs})
write_file(os.path.abspath('%s/clubs.html') % site_path, html_text)

# Edit requests
write_file('%s/edit-requests.html' % site_path,
    bob(jinja_env.get_template('edit-requests.html')))

# Contact
write_file('%s/contact.html' % site_path,
    bob(jinja_env.get_template('contact.html')))

# Orca News stubs
# Messages
write_file('%s/orca-news/messages.html' % site_path,
    bob(jinja_env.get_template('orca-news/messages.html')))

if os.path.isdir(os.path.abspath('%s/elSSGin/pods' % site_path)):
    shutil.rmtree(os.path.abspath('%s/elSSGin/pods' % site_path))
    print('Deleted old pods in site')
shutil.copytree('pods', os.path.abspath('%s/elSSGin/pods' % site_path))
print('Copied pods to site')
