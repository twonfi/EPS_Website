# the elgin park Static Site Generator (elSSGin)
elSSGin (else-jin) is ElginParkSecondary.com's new platform, powered by Python and templates to reduce the files needed
to edit to make global changes, and allowing simple content changes with JSON files (pods).

## Building
First, `cd` to the elSSGin directory (elSSGin uses a lot of relative paths, so you can't run this anywhere).

Then, choose a build command:
* `python __main__.py`
  * Production
* `python __main__.py --dev-build`
  * Development
  * Prevents the site from being indexed by search engines
  * Adds build time and Python version to footer of every page

In PyCharm, you can run build commands by choosing a config in the top-right corner:
* Build elSSGin site
  * Production build
* Build elSSGin site (--dev-build)
  * Development build

### `nonpm`
we now use cdnjs don't worry about npm anymore