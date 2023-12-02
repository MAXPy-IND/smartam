import re
from sys import argv

from setuptools import setup, find_packages

from compiler.api import compiler as api_compiler
from compiler.errors import compiler as errors_compiler

with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

with open("smartam/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

if len(argv) > 1 and argv[1] in ["bdist_wheel", "install", "develop"]:
    api_compiler.start()
    errors_compiler.start()

setup(
    name="Smartam",
    version=version,
    description="A Simple and Powerful TamTam API Framework in Python for users and bots..",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/MAXPy-IND/smartam",
    download_url="https://github.com/MAXPy-IND/smartam/releases/latest",
    author="JAZ",
    author_email="forgithuba@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks"
    ],
    keywords="tamtam chat messenger api client library python",
    project_urls={
        "Tracker": "https://github.com/MAXPy-IND/smartam/issues",
        "Community": "https://tt.me/smartam",
        "Source": "https://github.com/MAXPy-IND/smartam",
        "Documentation": "https://github.com/MAXPy-IND/smartam",
    },
    python_requires="~=3.7",
    package_data={
        "smartam": ["py.typed"],
    },
    packages=find_packages(exclude=["compiler*", "tests*"]),
    zip_safe=False,
    install_requires=requires
)
