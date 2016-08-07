from setuptools import setup, find_packages
from codecs import open
from os import path
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='nighthawk',
    version='2016.0',
    description='a powerful science and cryptography library',
    long_description='a powerful science and cryptography library',
    author='al3xv3gas',
    author_email='alexvegasdesign@gmail.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='science and cryptography',
    packages=find_packages(),
    install_requires=['nighthawk', 'pip'],
    entry_points={
        'console_scripts': [
            'nighthawk=nighthawk:main',
        ],
    },
)
