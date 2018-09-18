from setuptools import setup, find_packages

setup(
    name='awd',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click', 'boto3', 'tabulate'
    ],
    entry_points='''
        [console_scripts]
        awd=core:main
    ''',
)
