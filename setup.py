import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-maddog", # Replace with your own username
    version="0.0.2",
    author="Matt Derasoirs",
    author_email="nothing@razorbla.de",
    scripts=["bin/whatever-okay"],
    description="package about nothing",
    url="http://razorbla.de",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
)
