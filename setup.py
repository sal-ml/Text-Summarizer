import setuptools

with open("README.md", "r") as f:
    long_description = f.read()
    
__version__ = '0.1.0'

REPO_NAME = 'Text-Summarizer'
AUTHOR_USER_NAME = 'sal-ml'
SRC_REPO = 'Text-Summarizer'
AUTHOR_EMAIL = 'salkhan7964@gmail.com'

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package to summarize text data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src'),
)