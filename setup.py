from setuptools import setup, find_packages


setup(
    name="imagetitan",
    version="1.0",
    author = "Nikhil Jaiyam",
    author_email = "nikhiljaiyam6@gmail.com",
    packages=find_packages(),
    install_requires = [
        'numpy == 1.19.5',
        'matplotlib == 3.2.1',
        'PyQt5',
        'jupyterlab',
        'ipympl'
    ]
)
