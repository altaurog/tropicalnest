Python Skeleton
================

Installation
-------------

* Use an up-to-date python3 (currently 3.6.1)
* Setup a virtualenv.  To install virtualenv in bash::

    wget https://github.com/altaurog/venvinstaller/raw/master/venvinstaller.sh
    bash venvinstaller.sh
    source ~/.bashrc  # or start a new shell
    mkvirtualenv -p python3.6 myproject

* Clone this repo
* Adjust dependencies in requirements.txt
* Install dependencies::

    pip install -r requirements.txt -r dev-requirements.txt

* Adjust package metadata in ``setup.py``

  Requirements are specified in both ``requirements.txt`` and
  ``setup.py``.  The ones in ``setup.py`` will be automatically installed if
  they aren't already when you ``pip install`` this package.  Technically
  it isn't necessary to have them in both places but they often turn out to
  be useful in different context, plus you can make specific version
  requirements stricter in ``requirements.txt`` than in ``setup.py``, which
  is useful for development with well-known set of package versions and
  then testing or distributing with a wider set of dependency versions.

* Update upstream remote and push
* Install package in develop mode::

    pip install -e .

* Profit!

The Stack
---------

* `Falcon <https://falconframework.org/>`_ - minimalist framework for
  building rest apis

* `Marshmallow <https://marshmallow.readthedocs.io/>`_ - serialization

* `Sqlalchemy <https://www.sqlalchemy.org/>`_ - SQL engine.  (Also has an
  ORM, but preferred to use the core engine directly without ORM.)

* `Gunicorn <https://pypi.python.org/pypi/gunicorn>`_ - preforking HTTP/WSGI server

* `gevent <http://www.gevent.org/>`_ - use this as concurrent worker for
  Gunicorn.

* boto or `boto3 <https://github.com/boto/boto3>`_ - interface to AWS rest API.

* `requests <http://docs.python-requests.org/en/latest/>`_ - HTTP requests
  library.

* `psycopg2 <http://initd.org/psycopg/>`_ - postgresql client

* `py.test <http://pytest.org/latest/>`_ - testing framework

* `tox <https://tox.readthedocs.io/>`_ - automate tests in multiple
  environments.

* code `coverage <https://pypi.python.org/pypi/coverage>`_

* `docutils <http://docutils.sourceforge.net/>`_ - tools for writing
  documentation and working with reStructuredText markup.

* `Sphinx <http://www.sphinx-doc.org/en/latest/>`_ - documentation
  generation, based on docutils

For more, see `Awesome Python <https://github.com/vinta/awesome-python>`_.
