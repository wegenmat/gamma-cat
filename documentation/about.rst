.. include:: references.rst

About
=====

Brief
-----

This project was started in August 2015 and first presented as a poster
(see `gamma-cat poster at ADASS 2016`_) at the `ADASS 2016`_ conference.

This repo contains a `gammacat` Python package to work with the data.
It is BSD licensed (like Astropy, Gammapy).
This license only applies to the code, it has nothing to do with the data.

This is work in progress.
Feedback and contributions welcome!

Contact: use whatever you prefer:

* Email: gammapy@gmail.com
* Github issue tracker: https://github.com/gammapy/gamma-cat/issues
  (requires you to make a Github account, which is free and takes a minute)
* TODO: should we make a twitter or facebook account?

For now, we just collect TeV gamma-ray source information.
Later we might try to ingest and interconnect other catalogs
(e.g. Fermi-LAT GeV catalogs).

Why? There's already TeVCat!
----------------------------

Yes, there is `TeVCat`_ .

But TeVCat isn't really open.

You can view the info on their webpage, and copy & paste individual
numbers, but you can't download a catalog and use it for your research.

To quote http://tevcat.uchicago.edu/terms.html (accessed August 26, 2016):

.. pull-quote::

    | Users may not perform systematic downloads of TeVCat data for any purpose,
    | whether commercial or not, without the written permission of the
    | TeVCat team.  This includes scripted parsing of the website data,
    | webpage 'scraping', and the use of robots. If you need access to bulk
    | TeVCat data products, please contact the TeVCat team at tevcat@gmail.com

A second major problem with TeVCat is that there's no version history.
Updates and corrections happen, but only the maintainers know when
that happens and (presumably) what the older values were.

The goal here is to have a fully open TeV catalog that you can download
and use as you like (well, we still require attribution, see next section).

The data here is maintained as text (YAML and ECSV) files in a git repo on Github
following the model of `astrocats`_, so it's fully transparent
and we have version history.

The concrete motivation for Christoph Deil to start this catalog in
August 2016 was to have a TeV catalog for `gamma-sky.net`_,
as well as for checks of all sources in the H.E.S.S. Galactic plane
survey catalog against previous publications, and to have a TeV
source catalog available for the upcoming CTA science challenge.

Open and reproducible research for gamma-ray astronomy!

Terms of use
------------

All data collected here was originally generated by others.
If you intend to use this data in a publication,
we ask that you please cite the linked sources and/or
contact the sources of the data directly.

Collecting, cleaning and maintaining this catalog has taken a lot
of time. We require that you give attribution if you're using it.

For now, while we don't have a website / paper yet that can be
cited, please use this attribution:

.. pull-quote::

    | Data taken from |gamma-cat-repo|,
    | an open data collection and source catalog for gamma-ray astronomy.

Otherwise, you are free to use this data as you like.

Of course, we appreciate feedback can contributions
(additions and corrections)!

.. _contributors:

Contributors
------------

The following people have directly contributed to `gamma-cat`:

* Christoph Deil (`@cdeil <https://github.com/cdeil>`__)
* Axel Donath (`@adonath <https://github.com/adonath>`__)
* Matthias Wegen (`@wegenmat <https://github.com/wegenmat>`__)
* Arjun Voruganti (`@vorugantia <https://github.com/vorugantia>`__)
* Gernot Maier (`@GernotMaier <https://github.com/GernotMaier>`__)

Many others have contributed indirectly, e.g. given data or feedback via private communication.

Thank you!

.. _acknowledgements:

Acknowledgements
----------------

The following tools and services were used to produce this catalog:

* `SIMBAD`_
* `Astrophysics data system (ADS)`_
* `Astropy`_
* `Gammapy`_

* `TGeVCat`_ was used to look up info
  and we had good discussions and collaboration with the `TGeVCat` team.
* `TeVCat`_ was used to look up some info.
  (We did comply with their terms and conditions and didn't scrape their website to collect data for this catalog!)

Related resources
-----------------

Here are some related resources:

* Some of the data formats we use are defined or being defined at the
  `gamma-astro-data-formats`_ project.
* `gamma-sky.net`_ is a portal to the gamma-ray sky
* Fermi high-level data products (e.g. catalogs): |fermi-data|
* H.E.S.S. source catalog: |hess-cat|.
    * TSV (tab-separated value format) version: |hess-cat-tsv|
    * Copy on HEASARC with option to download in FITS or VOTable format: |hess-heasarc|
* HESS data collection for gamma-cat: |gamma-cat-hess-data|
* Collection of MAGIC data: |magic-fits|
* VERITAS data can be found by following the links here: |veritas-data|
* Another TeV source catalog is at `TeVCat`_ and with a new web interface at `TeVCat2`_.
* Another TeV source catalog is the `TeGeV Catalogue @ ASDC`_
* A `light curve archive @ DESY`_
* A collection and search interface for HESS spectra and lightcurves of blazars: |hess-obspm|
* A collection of Galactic TeV source info in FITS format by Andrea Giuliani and others from ASTRI is here: |astrisim-gsed|
