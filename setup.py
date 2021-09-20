from setuptools import setup, find_packages


setup(
    name="imageutils",
    version="1.0",
    author = "Nikhil Jaiyam",
    author_email = "nikhiljaiyam6@gmail.com",
    packages=find_packages(),
    install_requires = [
        'numpy == 1.17.4',
        'matplotlib == 3.1.2'
    ]
)