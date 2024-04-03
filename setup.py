# pylint: disable=C0114
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "StyleTransfer"
AUTHOR_USER_NAME = "RachanaHS"
AUTHOR_EMAIL = "rachuh2@gmail.com"

COAUTHOR_USER_NAME='AbhayaHanuma'
COAUTHOR_EMAIL='abhayabhi987@gmail.com'

SRC_REPO = "src"


setuptools.setup(
    name="styletransfer",
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    co_author=COAUTHOR_USER_NAME,
    co_author_email=COAUTHOR_EMAIL,
    description="A Style transfer project",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": SRC_REPO},
    packages=setuptools.find_packages(where=SRC_REPO)
)
