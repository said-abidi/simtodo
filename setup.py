# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

readme = open('README.md').read()

setup(
    name='SimTodo',
    version='0.1',
    description=('TODO'),
    long_description=readme,
    author='Said Abidi',
    author_email='sabidi@zendeskcom',
    url='https://github.com/said-abidi/simtodo',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'tinydb'
    ],
    entry_points = {
        'console_scripts': ['simtodo=simtodo.simtodo:main'],
    },
    license='MIT',
    zip_safe=True,  # To be verified
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Office/Business :: Scheduling',
    ],
)
