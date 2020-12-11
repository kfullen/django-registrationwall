PlexiWall
************************

|PyPI version|_ |Build status|_

.. |PyPI version| image::
   https://badge.fury.io/py/django-registrationwall.svg
.. _PyPI version: https://pypi.python.org/pypi/django-registrationwall

.. |Build status| image::
   https://travis-ci.org/richardcornish/django-registrationwall.svg?branch=master
.. _Build status: https://travis-ci.org/richardcornish/django-registrationwall

.. image:: https://raw.githubusercontent.com/richardcornish/django-registrationwall/master/docs/_static/img/regwall-detail.png

**PlexiWall** is a `Django <https://www.djangoproject.com/>`_ `mixin <https://docs.djangoproject.com/en/1.11/topics/class-based-views/mixins/>`_ `application <https://docs.djangoproject.com/en/1.11/intro/reusable-apps/>`_ that limits an `anonymous user <https://docs.djangoproject.com/en/1.11/ref/contrib/auth/#anonymoususer-object>`_'s access to content, after which the user is redirected to the `login URL <https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-LOGIN_URL>`_. The behavior is modeled after the common `paywall <https://en.wikipedia.org/wiki/Paywall>`_ scenario.

Fake news articles credit goes to The Onion.

* `Package distribution <https://pypi.python.org/pypi/django-registrationwall>`_
* `Code repository <https://github.com/richardcornish/django-registrationwall>`_
* `Documentation <https://django-registrationwall.readthedocs.io/>`_
* `Tests <https://travis-ci.org/richardcornish/django-registrationwall>`_

USAGE
=======

```
$ mkvirtualenv -p python3 demo
(demo)$ git clone [this_repo]
(demo)$ cd plexiwall/demo/
(demo)$ pip install -r requirements.txt
(demo)$ cd demo/
(demo)$ python manage.py migrate
(demo)$ python manage.py loaddata articles_article.json
(demo)$ python manage.py runserver
```

Open http://127.0.0.1:8000/articles/.
