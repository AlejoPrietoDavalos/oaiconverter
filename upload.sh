#!/bin/bash
rm -rf build dist oaiconverter.egg-info
python3 setup.py sdist bdist_wheel
twine upload dist/*
