
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

setup(
    name='indidaDND',
    packages = ['indiaDND'],
    version='0.1.0',
    description='A python project to detect whether a given indian mobile number is DND(Do Not Disturb) mode or not',
    url='https://github.com/RoadToNaukri/indiaDndPython',
    author='RoadToNaukri.com',
    author_email='tech@roadtonaukri.com',
    license='MIT',
    classifiers=[

        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        
    ],
    keywords=['DND india','DND'],
    install_requires=['beautifulsoup4']
)