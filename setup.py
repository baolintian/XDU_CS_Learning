#!/usr/bin/env python3

import os, subprocess
from setuptools import setup

subprocess.check_call('python3 ./auto/gen.py --root . --output auto'.split())

setup(
    name='xdu-cs-learning-cracker',
    description='frontend generator',
    install_requires=['sphinx-markdown-tables'],
)