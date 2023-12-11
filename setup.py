# install local packages for that reason it requires setup.py

from setuptools import find_packages,setup

setup(
    name='py_utils',
    version='0.0.1',
    author='saroj',
    author_email='sarojekka@cloudgenx.com',
    install_requires=['openai','langchain','streamlit','python-dotenv','pyPDF2'],
    packages=find_packages(),
)