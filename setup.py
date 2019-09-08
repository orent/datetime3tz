import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datetime3tz",
    version="3.8.0",
    author="Oren Tirosh",
    author_email="orent@hishome.net",
    description="Python 3.8 datetime module made timezone-aware by default",
    long_description=long_description,
    url="https://github.com/orent/datetime3tz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Python Software Foundation License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)

