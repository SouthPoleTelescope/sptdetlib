========
sptdetlib
========

This repository contains tools for controlling the South Pole Telescope readout
system, and performing initial data analysis for detector characterization.

Based on Simon Observatory's `sodetlib`_.

.. _`sodetlib`: https://github.com/simonsobs/sodetlib

Installation
------------

Instructions for setting up a SMuRF server can be found on the SPT-3g+ `wiki`_.

For offline analysis of sptdetlib data files, you can also install sptdetlib
by cloning this repo and running::

    $ python -m pip install -r requirements.txt
    $ python -m pip install .

.. _`wiki`: https://pole.uchicago.edu/spt4/index.php?title=SMuRF_Server_Setup_Instructions

Documentation
-------------

The sptdetlib documentation can be built using Sphinx. Once sptdetlib and its
dependencies are installed run::

    $ cd docs/
    $ make html

The SO-version sodetlib documentation is hosted on `Read the Docs`_.

.. _`Read the Docs`: https://sodetlib.readthedocs.io/en/latest/

Contributing
------------

Contributions are very welcome! Pull requests must be approved before being merged.

Licence
-------

This project is licensed under the BSD 2-Clause License - see the `LICENSE`_
file for details.

.. _`LICENSE`: LICENSE

