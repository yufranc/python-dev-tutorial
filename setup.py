from setuptools import setup, find_packages

setup(
    name='fizzbuzz',
    version="0.0.1",
    description='Fizz Buzz program.',
    author='yufranc',
    url='https://github.com/yufranc/python-dev-tutorial',
    author_email='yunafran@gmail.com',
    license='MIT',
    install_requires=[],
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License"
    ]
)