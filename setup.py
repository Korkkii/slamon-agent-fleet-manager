#!/usr/bin/env python

from setuptools import setup
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
    long_description='The implementation of SLAMon agent on Python 3.4. The agent connects to an Agent Fleet Manager, \
and executes tasks retrieved.\nAimed to be used on Unix platforms. The agent can be used either from a python script \
or via command line script.\nRead more from the repository for examples and instructions.',
    packages=[
        'slamon_afm',
        'slamon_afm.routes',
    ],
    install_requires=[
        'bottle>=0.12.8, <1.0',
        'sqlalchemy>=1.0.6, <2.0'
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
