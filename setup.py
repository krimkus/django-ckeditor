import os
from setuptools import setup, find_packages

def find_package_data(**packages):
    package_data = {}
    for package_directory,top_dirs in packages.items():
        outfiles = []
        package_data[package_directory] = []
        for top_dir in top_dirs:
            for dirpath, dirnames, filenames in os.walk(os.path.join(package_directory,top_dir)):
                for filename in filenames:
                    path = os.path.join(dirpath, filename)[len(package_directory)+1:]
                    package_data[package_directory].append(path)
    return package_data


install_requires = []
try:
    import json
except ImportError, e:
    install_requires.append('simplejson')

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README')

description = 'A small Django application that makes it easy to use CKEditor for form textareas.'

if os.path.exists(README_PATH):
    long_description = open(README_PATH).read()
else:
    long_description = description


setup(
    name='django-ckeditor',
    version='0.9.5',
    install_requires=install_requires,
    description=description,
    long_description=long_description,
    author='Dumbwaiter Design',
    author_email='dev@dwaiter.com',
    url='http://bitbucket.org/dwaiter/django-ckeditor/',
    packages=find_packages(),
    package_data = find_package_data(ckeditor=['static', 'templates']),
    include_package_data=True,
)
