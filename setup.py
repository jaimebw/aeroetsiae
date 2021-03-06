from setuptools import find_packages, setup

setup(
    name = 'aeroETSIAE',
    packages=find_packages(include=['aerodynamics]),
    version= '0.1.0',
    description='Easy implementation of Potential theory equations',
    author='Jaime Bowen',
    author_email="jaimebwv@gmail.com",
    install_requires = [],
    license='MIT',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    url="https://github.com/jaimebw/easyISA",
    python_requires='>=3.6'
)