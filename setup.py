#!/usr/bin/env python

from setuptools import find_packages, setup
# TODO: Fix for AFM
setup(
    name='slamon-afm',
    version='0.9.0',
    description='SLAMon Agent Fleet Manager that controls deployed agents by given them tasks. '
                'Part of the Coordinator that can be polled for task results.',
    url='https://github.com/SLAMon/slamon-agent-fleet-manager',
    author='SLAMon',
    author_email='slamon.organization@gmail.com',
    license='Apache License v2.0',
    platforms=['Python 3.3+'],
    long_description='',
    packages=find_packages(),
    install_requires=[
        'bottle>=0.12.8, <1.0',
        'sqlalchemy>=1.0.6, <2.0',
        'jsonschema>=2.5.1, <3.0',
        'python_dateutil>= 2.4.2, <3.0'
    ],
    entry_points={
        # TODO: Create AFM console script
        'console_scripts': [
            'slamon-agent = slamon_agent.agent:main'
        ]
    },
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: System :: Monitoring'
    ]
)
