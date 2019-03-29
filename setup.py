# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="bfex",
    packages=['bfex'],
    version="0.2",
    description="Python wrapper for bitFlyer's REST API.",
    author="",
    author_email="",
    url="https://github.com/GRR6I2I2/bfex",
    install_requires=['requests'],
    keywords=["bitcoin", "bitflyer", "wrapper", "REST API"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
