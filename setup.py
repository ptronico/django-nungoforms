import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-nungoforms',
    version='0.1.1',
    packages=[
        'nungoforms',
        'nungoforms.migrations',
        'nungoforms.templatetags',
    ],
    include_package_data=True,
    license='MIT',
    description='Nungoforms is a very simple Django app to super-DRY your templates.',
    long_description=README,
    url='https://github.com/ptronico/django-nungoforms',
    download_url='https://github.com/ptronico/django-nungoforms/archive/0.1.tar.gz',
    author='Pedro Vasconcelos',
    author_email='ptronico@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)