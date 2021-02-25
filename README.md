# Hello World

Just working through the "Hello World" example on how to publish a python module to PyPI from
[Publishing (Perfect) Python Packages on PyPi](https://www.youtube.com/watch?v=GIF3LaRqgXo)

Source Code: https://github.com/judy2k/publishing_python_packages_talk

## Build the pip package

```bash
pipenv install -e .
pipenv install --dev 'pytest>=3.7'
pipenv shell
# (helloworld)
pytest
```

## Source Distribution

```bash
# (helloworld)
python setup.py sdist
..writes dist/helloworld-msusol-0.0.1.tar.gz

tar tzf dist/helloworld-msusol-0.0.1.tar.gz
helloworld-msusol-0.0.1/
helloworld-msusol-0.0.1/LICENSE
helloworld-msusol-0.0.1/MANIFEST.in
helloworld-msusol-0.0.1/PKG-INFO
helloworld-msusol-0.0.1/Pipfile
helloworld-msusol-0.0.1/Pipfile.lock
helloworld-msusol-0.0.1/README.md
helloworld-msusol-0.0.1/pyproject.toml
helloworld-msusol-0.0.1/setup.cfg
helloworld-msusol-0.0.1/setup.py
helloworld-msusol-0.0.1/src/
helloworld-msusol-0.0.1/src/helloworld.py
helloworld-msusol-0.0.1/src/helloworld_msusol.egg-info/
helloworld-msusol-0.0.1/src/helloworld_msusol.egg-info/PKG-INFO
helloworld-msusol-0.0.1/src/helloworld_msusol.egg-info/SOURCES.txt
helloworld-msusol-0.0.1/src/helloworld_msusol.egg-info/dependency_links.txt
helloworld-msusol-0.0.1/src/helloworld_msusol.egg-info/requires.txt
helloworld-msusol-0.0.1/src/helloworld_msusol.egg-info/top_level.txt
helloworld-msusol-0.0.1/test_helloworld.py
helloworld-msusol-0.0.1/tox.ini
```

## Publish

```bash
twine check dist/*
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

...Uploading distributions to https://upload.pypi.org/legacy/
...Enter your username:
...Enter your password: 
...Uploading helloworld-msusol-0.0.1.tar.gz
```

Now available at: https://pypi.org/project/helloworld-msusol/

## Installation

Run the following to install:

```bash
pip install helloworld-msusol
```

## Usage

```python
from helloworld import say_hello

# Generate "Hello, World!"
say_hello()

# Generate "Hello, Everybody!"
say_hello("Everybody")
```