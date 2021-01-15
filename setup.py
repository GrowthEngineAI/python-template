import os, sys
import os.path

from setuptools.command.install import install as _install
from setuptools import setup, find_packages

root = os.path.abspath(os.path.dirname(__file__))

package_name = "python_template"
binary_names = ["src"]
VERSION = "0.0.1"

packages = find_packages(
    include=[package_name, "src.*"]
)

with open(os.path.join(root, 'README.md'), 'rb') as readme:
    long_description = readme.read().decode('utf-8')

def _post_install():
    from subprocess import call
    call([sys.executable, 'config/post_install.py'], cwd=os.path.join(root, 'src'))

class install(_install):
    def run(self):
        _install.run(self)
        self.execute(_post_install, (self.install_lib,), msg="Running Post Installation")

setup(
    name=package_name,
    version=VERSION,
    description="short description",
    long_description=long_description,
    author='Your Name',
    cmdclass={'install': install},
    author_email='dev@growthengineai.com',
    url='http://github.com/GrowthEngineAI/{}'.format(package_name),
    python_requires='>3.6',
    install_requires=[
        "pysimdjson",
        "rich",
        "typer"
    ],
    package_data={
        'json': ['*.json'],
    },
    extras_require={
        'test': ['pytest'],
    },
    packages=packages,
    entry_points={
        "console_scripts": [
            "{} = {}.cli:cli".format(binary_name, package_name)
            for binary_name in binary_names
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
    ],
)