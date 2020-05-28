import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autonaomi",
    version="0.0.0.0.0.0.0.0.0000001",
    author="Yuval Barak",
    author_email="yuvalyehudab@mail.tau.ac.il",
    description="A small example package... indeed",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yuvalyehudab/autonaomi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)