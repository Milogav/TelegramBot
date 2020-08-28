import os
import setuptools


def get_requirements():
    cwd = os.path.dirname(os.path.realpath(__file__))
    req_file = os.path.join(cwd, 'requirements.txt')
    with open(req_file, 'r') as fp:
        reqs = fp.read().splitlines()

    return reqs


def get_version():
    cwd = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(cwd, 'pytelegram', '__init__.py'), 'r') as fp:
        lines = fp.read().splitlines()

    for line in lines:
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]

    raise Exception('Could not retrieve version number')


setuptools.setup(
    name="pytelegram",
    version=get_version(),
    author="Milogav",
    description="Python package to interact with the Telegram Bot API",
    url='https://https://github.com/Milogav/pytelegram',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[get_requirements()]
)
