#!/usr/bin/env python3

from setuptools import find_packages, setup

setup(
    name='linca',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'linca = linca:main',
        ],
    },

    author='Allen Li',
    author_email='darkfeline@felesatra.moe',
    description='',
    license='',
    url='',
)
