from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_requires=[
        'pytest',
        'coverage'
    ],
    install_requires=[
        'flask',
    ],
)