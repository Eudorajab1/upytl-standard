import re
from setuptools import setup


def get_module_var(varname):
    src = 'upytl_standard'
    regex = re.compile(fr"^{varname}\s*\=\s*['\"](.+?)['\"]", re.M)
    mobj = next(regex.finditer(open(f"{src}/__init__.py").read()))
    return mobj.groups()[0]


__author__ = get_module_var('__author__')
__license__ = get_module_var('__license__')
__version__ = get_module_var('__version__')


setup(
    name="upytl_standard",
    version=__version__,
    url="https://github.com/Eudorajab1/upytl-standard",
    license=__license__,
    author=__author__,
    author_email="eudorajab1@gmail.com",
    maintainer=__author__,
    maintainer_email="eudorajab1@gmail.com",
    description="Standard UPYTL - Ultra Pythonic Template Language component library",
    platforms="any",
    keywords='python UPYTL webapplication html',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    install_requires=[
        "upytl>=0.0.6",
    ],
    python_requires='>=3.7',
    packages=['upytl_standard'],
)
