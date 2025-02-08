import os
import sys
import re
import shutil
from datetime import datetime, timezone

import json5 as json
import jinja2

debug_info = datetime.now(timezone.utc).isoformat(), sys.version

print(debug_info)

# Add noindex if run with --dev-build
if '--dev-build' in sys.argv:
    dev_build = True
    print('Building with --dev-build: noindex and debug information added.')
else:
    dev_build = False


def write_file(full_path, content):
    with open(full_path, 'w', encoding='UTF-8') as f:
        f.write(content)
    print('Wrote %d bytes to %s ' % (len(bytes(content, "UTF-8")), full_path))


jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates/'))

departments = []
for dept_list_entry in os.scandir('pods/departments'):
    if os.path.isfile(dept_list_entry):
        with open(dept_list_entry.path, 'r') as file:
            dept = json.loads(file.read())

        departments.append({
            'name': dept['name'],
            'id': re.sub('.json5?$', '', dept_list_entry.name)
        })

specialized_programs = []
for specialized_program_path in os.scandir(
        'pods/specialized'):
    with open(specialized_program_path.path, 'r') as file:
        specialized_program = json.loads(file.read())

    specialized_programs.append({
        'name': specialized_program['name'],
        'id': re.sub('.json5?$', '', specialized_program_path.name)
    })

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
        departments=departments, specialized_programs=specialized_programs,
        dev_build=dev_build, debug_info=debug_info,
        last_update=datetime.now(timezone.utc).strftime('%A, %B %-d, %Y'
                                                        ' at %-I:%M:%S %p'),
        **params
    )

site_path = '../site'

# Delete existing files so that deleted data doesn't resurface
for directory in ['departments', 'specialized', 'orca-news']:
    for file in os.scandir(os.path.abspath('../site/' + directory)):
        path = os.path.join(directory, file.path)
        if os.path.isdir(os.path.abspath(path)):
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

def dept_pages(pods: list[dict], file_dir: str) -> None:
    for entry in pods:
        pod_path = os.path.abspath('pods/%s/%s.json5'
                                    % (file_dir, entry['id']))

        with open(pod_path, 'r') as pod_file:
            pod_data = json.loads(pod_file.read())

        write_file(
            os.path.abspath(
                '%s/%s/' % (site_path, file_dir) + re.sub(".json5?$",
                    ".html", os.path.basename(pod_path))),
            bob(jinja_env.get_template('departments.html'), {
                'dept': pod_data,
                'dept_id': entry['id']
            })
        )
# Departments
dept_pages(departments, 'departments')
# Specialized programs
dept_pages(specialized_programs, 'specialized')


# Clubs
with open('pods/clubs.json5', 'r') as file:
    clubs = json.loads(file.read())

html_text = bob(jinja_env.get_template('clubs.html'), {'clubs': clubs})
write_file(os.path.abspath('%s/clubs.html') % site_path, html_text)

# Forms
with open('pods/forms.json5', 'r') as file:
    forms = json.loads(file.read())

html_text = bob(jinja_env.get_template('forms.html'), {'forms': forms})
write_file(os.path.abspath('%s/forms.html') % site_path, html_text)

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
# Calendar
write_file('%s/orca-news/calendar.html' % site_path,
    bob(jinja_env.get_template('orca-news/calendar.html')))

if os.path.isdir(os.path.abspath('%s/elSSGin/pods' % site_path)):
    shutil.rmtree(os.path.abspath('%s/elSSGin/pods' % site_path))
    print('Deleted old pods in site')
shutil.copytree('pods', os.path.abspath('%s/elSSGin/pods' % site_path))
print('Copied pods to site')
