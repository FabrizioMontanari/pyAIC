import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyAIC", # Replace with your own username
    version="0.0.1",
    author="FabrizioMontanari",
    author_email="",
    description="A package to manipulate, convert validate AIC codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FabrizioMontanari/pyAIC",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
