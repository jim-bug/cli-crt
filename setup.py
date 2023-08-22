from setuptools import find_packages, setup

setup(
    name='Creator Coding-Files',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['crt=src.crt:main']
    }

)
