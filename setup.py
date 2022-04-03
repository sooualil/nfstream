"""
------------------------------------------------------------------------------------------------------------------------
setup.py
Copyright (C) 2019-22 - NFStream Developers
This file is part of NFStream, a Flexible Network Data Analysis Framework (https://www.nfstream.org/).
NFStream is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.
NFStream is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public License along with NFStream.
If not, see <http://www.gnu.org/licenses/>.
------------------------------------------------------------------------------------------------------------------------
"""

import sys
import os
import platform
from setuptools import setup

if (not sys.version_info[0] == 3) and (not sys.version_info[1] >= 6):
    sys.exit("Sorry, nfstream requires Python3.6+ versions.")

THIS_DIRECTORY = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(THIS_DIRECTORY, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = ['cffi>=1.15.0',
                    'psutil>=5.8.0',
                    'dpkt>=1.9.7']

# This is mandatory to fix both issues with numpy using Accelerate backend on macos and pandas issues with PyPy
if sys.platform == 'darwin':
    install_requires.append("numpy<=1.18.5")
else:
    install_requires.append("numpy>=1.19.5")

if platform.python_implementation() == 'PyPy':
    install_requires.append("pandas<=1.2.5")
else:
    install_requires.append("pandas>=1.1.5")

setup(
    name="nfstream",
    version='6.4.3',
    url='https://www.nfstream.org/',
    license='LGPLv3',
    description="A Flexible Network Data Analysis Framework",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Zied Aouini',
    author_email='aouinizied@gmail.com',
    packages=['nfstream', 'nfstream.plugins', 'nfstream.engine'],
    setup_requires=["cffi>=1.15.0"],
    cffi_modules=["nfstream/engine/engine_build.py:ffi_builder"],
    install_requires=install_requires,
    include_package_data=True,
    platforms=["Linux", "Mac OS-X", "Windows", "Unix"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    project_urls={
        'GitHub': 'https://github.com/nfstream/nfstream',
    }
)
