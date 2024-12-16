# Contribution Guide
This is a how-to guide on working on the Elgin Park Secondary website.

* Directories starting with `/` means the root of the repository (e.g. `~/git/github.com/Bouney/EPS_Website`), not the
    root of your file system.

## Environment setup
### Wrangler
1. Get `node` and `npm`
2. Clone the repository (if you haven't already done so)
3. cd to `/`
4. Install Wrangler: `npm i wrangler`
5. `npx wrangler pages dev`

Make sure to only use Wrangler, which is pretty much a local Cloudflare Pages, so that Pages redirects and Workers work correctly.

### Python (elSSGin)
1. Install Python
2. `pip install -r elSSGin/requirements.txt`
3. Build the site
    - If you use PyCharm: run "Build elSSGin site" (select in top right corner)
    - If you use Visual Studio Code: run "Build elSSGin site" in Run & Debug
    - Everyone else: in `/elSSGin`: `python __main__.py`
    - The script builds the site to `/site`
    - Rebuild every time you update a pod

Make sure to use %s strings (`'hello %s' % var`); CF Pages runs a rather old version of Python.

The build script can also be run with `--dev-build`, which will prevent the site from being indexed
and add debugging information to the footer of every page. This can be run with the
"Build elSSGin site with --dev-build" config in PyCharm, or with `python __main__.py --dev-build`.

When in doubt, don't push it to main; use a new branch, and preview the page at
`https://{{ first 8 chars of commit hash }}.eps-website.pages.dev`

### IDE/editor setup
#### PyCharm
Use the project inspection settings; everything else should be automatic (run configs)

#### Visual Studio Code
Install the extensions marked as recommended in `.vscode/extensions.json` (a.k.a. workspace recommendations, recommended by other users in the workspace), and turn on any other workspace settings.

## Editing data
Department and club data is stored in `elSSGin/pods`; every JSON data file is called a "pod".

Before you edit, set the schemas (`elSSGin/pods/schemas`) in your IDE or editor. **Don't break the site. Don't edit without the schema.**

### Visual Studio Code JSON5 support
Pods use [JSON5](https://json5.org/), which does not have built-in support in VS Code. Install the recommended JSON5 extension in the editor setup section; other JSON5 extensions don't have schema validation.

## Handling edit requests
If you don't have access to the forms, ask in the Computer Programming Club team on Teams for access to form data

### Wait for requests
You'll be emailed when a new request is submitted

### Read the request
    - Requests sent through the staff & students form should be more trusted, as it requires SD36 login
    - First submitted, first handled
    - **Do not delete old requests. They are to be kept for tracking purposes.**

### Implement
    - Edit the files
    - Increase the edit request counter in `/EDIT_REQUESTS_HANDLED`
    - Use the following commit message:
        - Implement edit request #`{{ ID }}`
    - For privacy reasons, **do not include name, email, or any other info** other than request ID

### Respond
    - Staff & students form: download as Excel spreadsheet and find the email. If requester chose Teams, start a chat and enter the email address as the name.
    - Parents & visitors form: Email is in the form as a field
    - Use the [edit request templates in the wiki](https://github.com/Bouney/EPS_Website/wiki/Edit-request-templates)