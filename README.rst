###############
Sections
###############

Base app for sections delivered by RevSquare. Tested with django 1.7.x

* Provide base models in `rs_sections.models`



*******
Install
*******

It is strongly recommanded to install this theme from GIT with
 PIP onto you project virtualenv.

.. code-block::  shell-session

    pip install git+ssh://git@revsquare-test.com/rs-sections.git


*****
Setup
*****


.. code-block::  python

    INSTALLED_APPS = (
        ...
        'rs_sections'
        ...
    )


*****
Tests
*****


.. code-block::  shell-session
    python manage.py test cms_base


*******************
Additional Packages
*******************


