from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="helloworld-msusol",
    version="0.0.2",
    description="Say hello!",
    py_modules=["helloworld"],
    package_dir={"": "src"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/msusol/helloworld",
    author="Mark Susol",
    author_email="marksusol@gmail.com",

    install_requires=[
        "blessings ~= 1.7",
    ],

    extras_require={
        "dev": [
            "pytest >= 3.7",
            "check-manifest",
            "twine",
        ],
    },
)
