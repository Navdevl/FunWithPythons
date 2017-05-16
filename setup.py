# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='Final',
    version='0.0.1',
    packages=find_packages(exclude=['tests']),
    entry_points = {
        'console_scripts': [
            'magic = alohomora.cli:magic',
            'longest = alohomora.cli:longest',
        ]
    },
    install_requires=(['click','pytest']),
    url='',
    license='Still Nothing',
    author='Naveen',
    author_email='naveendurai19@gmail.com',
    description='Trying to impress Skcript :P'
)
