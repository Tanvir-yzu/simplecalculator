# setup.py

from setuptools import setup, find_packages

setup(
    name='simplecalculator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={},
    description='A simple calculator package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your@email.com',
    url='https://github.com/yourusername/simplecalculator',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
