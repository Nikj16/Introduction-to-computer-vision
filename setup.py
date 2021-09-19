from setuptools import setup, find_packages


setup(
    name="image_utils",
    version="1.0",
    packages=find_packages(include=['image_utils', 'image_utils.*']),
)