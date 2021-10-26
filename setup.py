import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='kranthitest',
    version='0.0.1',
    author='Kranthi',
    author_email='kranthi.des@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/kranthides/kranthi-test',
    project_urls={
        "Bug Tracker": "https://github.com/kranthides/kranthi-test"
    },
    license='MIT',
    packages=['kranthitest'],
    install_requires=['requests'],
)
