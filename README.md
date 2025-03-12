# Elgin Park Secondary Website (EPS Website)

![1.00](https://elginparksecondary.com/elgin_logo.png)

**A preview of the site is available**: https://eps-website-elssgin-twonfi.pages.dev

Once this thing is done, twonfi can help putting this on CF Pages.

***

Welcome to the **EPS Website** repository! This repository contains the official source code for the Elgin Park Secondary website, at [ElginParkSecondary.com](https://www.elginparksecondary.com), proudly developed and maintained by the **EPS Computer Programming Club**.

***

## Overview

The **EPS Website** is the digital platform for Elgin Park School, designed to provide students, staff, and the community with easy access to information and resources.

***

## Changes

### elSSGin (Elgin Park Static Site Generator)
_(pronunciation: else-jin)_

Before elSSGin, the website code was WET (everything was repeated,
and if one minor thing had to be changed, everything had to be changed.)
elSSGin implements a data-file-based static site generation system, with all courses, clubs, and forms stored in
YAML data files with JSON Schemas.

elSSGin also uses templates, which means that future design changes can be made in one place (the current UI ported
to elSSGin looks rather old).

elSSGin is not perfect. See the TODO section below.

Take a look at `/CONTRIBUTING.md` for instructions about working with elSSGin.
If you need more help with elSSGin, contact twonfi (who developed elSSGin).

### Club list
ElginParkSecondary.com now has a club list, using elSSGin YAML data files. 

Currently, the club list supports club sponsor teachers, meeting rooms and times, a club logo, an Instagram account, and
a club description.

More features (larger photos and videos) will be implemented when the first edit request is submitted 
(to make sure that people even know about the club list).

Entire club _websites_ might be considered in the future, but it's not going to happen anytime soon
(clubs are too attached to Instagram, and websites are likely "boring" for them, versus the dopamine-filled Instagram.)

### Built-in Orca News (Appazur)
The district uses Appazur to provide school apps, such as Orca News for Elgin Park,
where daily announcements are posted.
ElginParkSecondary.com provides a web-based client for Orca News, so that there's "one website, all of EPS."

Some parents without phones might not even realize that
[Appazur already provides a web-based client](https://elginpark.appazur.com), so ElginParkSecondary.com's Orca News
feature on the same site as course information, usable on public computers, makes the Orca News app more accessible.

Plus, it has a "better" (objectively subjective) interface.
Unlike Appazur's _own_ Appazur web client, ElginParkSecondary.com's Appazur client tries to mimic the feel of the
mobile app (lazy-loaded thumbnail images), while taking advantage of the larger screen size.
Also, unlike Appazur's _own_ web calendar, only in agenda view, ElginParkSecondary.com's calendar is an actual table
calendar, powered by FullCalendar.
Lastly, unlike Appazur's _own_ mobile or web client, ElginParkSecondary.com's Orca News pages have dark mode, making it
easier on the eyes when checking at night (yes, there are a few late-night Orca News messages).

ElginParkSecondary.com can't use Appazur's API directly (CORS), so an Appazur-only CORS proxy
(for example, `https://www.elginparksecondary.com/orca-news/data?api=a`) powered by Cloudflare Workers is used.

Note that the Computer Programming Club is not affiliated with Appazur, but we do hope that this will make the Orca News
service more accessible.
Currently, the `Cache-Control` header is set to `no-cache`, but the club will analyze the frequencies of Orca News posts
to dynamically set `Cache-Control` (for example, different `max-age` at midnight vs. noon) to put less load on Appazur's
servers (although they are already putting a load on their servers by checking with every _official app_ open.)

It's also not an "alternative" to the _entire_ Appazur service; it's only an alternative to the Appazur _reader client_.
The club might set up an alternative data source (`on.elginparksecondary.com`), but it will likely be elSSGin-like, not
a complete system with a database and a backend,
but this is unlikely considering that Appazur is district-wide, not just used by Elgin Park.

### Responsive design
But what about people with phones as their only means of Internet access?
(Obviously going the opposite route as the Orca News feature.)
ElginParkSecondary.com is now usable on small screens, showing a JS-free "hamburger menu" in place of the standard
navbar, removing the background image, and other improvements for different screen sizes.

Unfortunately, the actual course selection system, MyEducation BC (MyEd),
using Follett Aspen (unfortunately proprietary), is still not mobile-friendly.
Instead, it shows a minimal version of the site, called Aspen Express, which doesn't even have the My Info section
(it only has features that our school doesn't even use, such as assignments.)
This is not COVID-19, and we use Teams for assignments.

***

## Technologies Used

* Cloudflare Pages
* elSSGin
  * Python
  * Jinja

***

## Contributors

Acknowledgement should be voluntary.
Feel free to add your name (or GitHub username) here.

If you do not want your GitHub account to be associated with your real name,
please message the private Microsoft Teams team.

***

This project is made possible thanks to the hard work and dedication of the following members of the
**Computer Programming Club**:

- Micah Ming Ren Hou
- John Li
- Richard Fang
- Oliver Kihoi Guo
- Andrew Schutte
