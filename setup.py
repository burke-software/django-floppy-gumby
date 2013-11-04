from setuptools import setup, find_packages

setup(
    name = "django-floppy-gumby",
    version = "0.1",
    author = "David Burke",
    author_email = "david@burkesoftware.com",
    description = ("Gumby Framework forms for Django using floppy forms. A floppy and gumby project."),
    license = "BSD",
    keywords = "django gumby",
    url = "https://github.com/burke-software/django-floppy-gumby",
    packages=find_packages(),
    include_package_data=True,
    test_suite='setuptest.setuptest.SetupTestSuite',
    tests_require=(
        'django-setuptest',
    ),
    classifiers=[
        "Development Status :: 4 - Beta",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=['django', 'django-floppyforms']
)
