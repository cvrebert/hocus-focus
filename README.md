hocus-focus
===========

CSS regression test review tool for Bootstrap

## How it works
* [grunt-sauce-screenshots](https://github.com/cvrebert/grunt-sauce-screenshots) to take screenshots in various browsers
* [GraphicsMagick `compare`](http://www.graphicsmagick.org/compare.html) to compare the screenshots and output visual diffs; see [dpxdt](https://github.com/bslatkin/dpxdt) for usage
* [Flask](http://flask.pocoo.org/) web app to review diffs and approve intentional changes
* [Flask-OAuthlib](https://flask-oauthlib.readthedocs.org/) for GitHub-based login
* Some Python GitHub API library to post issues to the issue tracker when there are differences
