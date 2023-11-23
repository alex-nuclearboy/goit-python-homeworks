from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.1',
    description='A Python package for organizing and sorting files into categories based on file extensions',
    url='https://github.com/alex-nuclearboy/goit-python-homeworks/tree/main/goit-python-core-hw-07',
    author='Aleksander Khreptak',
    author_email='alex.nuclearboy@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['shutil']
)