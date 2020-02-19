from setuptools import setup

from pkg_resources_removal import __version__


with open("README.md", "r") as f:
    readme = f.read()

setup(
    name="pkg-resources-removal",
    version=__version__,
    author="Aleksa Ćuković",
    author_email="aleksacukovic1@gmail.com",
    description="git pre-commit hook for removing pkg-resources from requirements.txt",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/AleksaC/pkg-resources-removal-hook",
    license="MIT",
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    packages=["pkg_resources_removal"],
    entry_points={
        "console_scripts": ["remove-pkg-resources = pkg_resources_removal.remove:main"]
    },
)
