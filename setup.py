try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import djangocms_oscar

version = djangocms_oscar.__version__

setup(
    name = 'djangocms_oscar',
    packages = ['djangocms_oscar'],
    include_package_data = True,
    version = version,
    description = 'djangocms oscar integration',
    author = 'creimers',
    author_email = 'christoph@superservice-international.com',
    license='MIT License',
    url = 'https://github.com/creimers/djangocms-oscar',
    keywords = ['djangocms', 'django', 'oscar',], 
    install_requires = ['django-cms>=3.0'],
    classifiers = [
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
)
