So, why yet another tool for this?

Requirements:
* Can test in up-to-date versions of all major browsers
* Can test on up-to-date versions of all major OSes
* Can test in IE9 (because Bootstrap v4 will support IE9+)
* Don't want to have to setup/maintain our own cluster of VMs running all the necessary OSes (and all the versions of Windows)
* Workflow for management of reference/baseline/norm screenshots

Nice-to-haves:
* Any necessary third-party services being low-cost or free, since this is for an open-source project (namely, Bootstrap)
* Ability to adjust viewport/screen size for testing of ["responsive"](http://en.wikipedia.org/wiki/Responsive_web_design) features
* GitHub integration

Non-requirements:
* Testing interactions with JavaScript widgets
  * A nice-to-have, but not worth it if it overcomplicates things or requires compromises on the main Requirements

---

Prior art (and boy, is there a lot of it!)

* [SiteEffect](http://siteeffect.io/)
  * No public source code is yet available; [GitHub repo](https://github.com/ti2m/siteeffect) is a stub
* [Bugsnag's unnamed Selenium-based tool](https://bugsnag.com/blog/implementing-a-visual-css-testing-framework)
  * Not currently publicly available at all
* [Huxley](https://github.com/facebookarchive/huxley)
  * Has been abandoned by Facebook; is no longer maintained
  * Was geared towards testing interactions with JavaScript widgets, as opposed to testing of static webpages
* [Hardy](http://hardy.io)
  * Offers "CSS property X of element Y has value Z" testing, rather than screenshot comparison
  * Writing/updating this type of test seems prohibitively tedious
* [DalekJS](http://dalekjs.com)
  * Seems geared more towards functional testing
  * Doesn't seem to have any integrated workflow for management of reference/baseline/norm screenshots
* [CSS Critic](https://github.com/cburgmer/csscritic)
  * Supports Firefox and PhantomJS
  * Has a review workflow
* [Needle](https://github.com/bfirsh/needle)
  * Somewhat promising. Offers unit tests with screenshot equality assertions.
  * Supports remote Selenium.
  * Supports setting viewport size.
  * Has some tooling around setting reference/baseline/norm screenshots
    * Not clear whether it supports updating a single reference screenshot at a time, rather than everything at once.
    * Reference/baseline/norm screenshot update workflow doesn't seem quite suited to Bootstrap's particular situation
  * Visual diffs require [Perceptual Image Diff](http://sourceforge.net/p/pdiff/code/HEAD/tree/) tool whose maintenance status is unclear
* [Browsershots](http://browsershots.org)
  * Uses virtual cluster of volunteers' computers to take screenshots in various browsers/OSes
  * Throughput/capacity level is unclear, and we'd be asking for a \*lot\* of screenshots
  * No workflow or higher-level tooling, but it exposes an API which might allow building such workflow tooling
* [CrossBrowserTesting.com](http://crossbrowsertesting.com)
  * Hosted solution with integrated review workflow
  * Pay per minute of test
* [Depicted / dpxdt](https://github.com/bslatkin/dpxdt)
  * PhantomJS-based, *but* also offers "Diff My Images" option to import images taken from other tools
  * Offers web-based test result viewer and reference/baseline/norm management workflow
  * No explicit cross-browser support in its data model
* [PhantomJS](http://phantomjs.org)-related tools
  * Included for completeness, but these fail our cross-browser + cross-OS requirements
  * [CasperJS](http://casperjs.org)
    * Wrapper for PhantomJS & SlimerJS
    * No higher level tooling around screenshots, just a "take a screenshot" API
  * [SlimerJS](http://slimerjs.org)
    * Firefox/Gecko equivalent of PhantomJS
  * [TrifleJS](https://github.com/sdesalas/trifleJS)
    * Internet Explorer equivalent of PhantomJS
  * [PhantomCSS](https://github.com/Huddle/PhantomCSS)
    * CasperJS-based CSS regression testing
  * [Wraith](https://github.com/bbc-news/wraith)
    * CasperJS-based CSS regression testing
  * [BackstopJS](http://garris.github.io/BackstopJS/)
    * CasperJS-based CSS regression testing of "responsive" webpages
    * Includes web app to review test results (and manage reference/baseline/norm screenshots?) 
  * [grunt-photobox](https://github.com/stefanjudis/grunt-photobox)
    * PhantomJS-based screenshot-taker and web-based visual diff review tool
