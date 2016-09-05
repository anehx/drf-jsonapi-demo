from setuptools import setup

setup(
    name = "drf-jsonapi-demo",
    version = "0.0.0",
    entry_points = {
        "console_scripts": [
        ]
    },
    install_requires = [
        "django==1.9",
        "djangorestframework==3.4.1",
        "djangorestframework-jsonapi==2.0.1",
        "django-filter==0.13",
        "django-crispy-forms==1.6.0",
        "pytest",
        "pytest-django",
        "pytest-cov",
        "factory-boy==2.7.0",
        "ipdb"
    ],
    author = "Jonas Metzener",
    author_email = "jonas.metzener@adfinis-sygroup.ch",
    description = "A simple API to demonstrate JSON API with Django and DRF",
    long_description = "",
    keywords = "demo,jsonapi,drf,django",
    url = "https://github.com/anehx/drf-jsonapi-demo",
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: "
        "GNU Affero General Public License v3",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5.1",
    ]
)
