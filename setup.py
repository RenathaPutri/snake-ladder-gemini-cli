from setuptools import setup


def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
        return long_description


setup(
    name='snake-ladder-gemini-cli',
    version='1',
    packages=['snake-ladder-gemini-cli'],
    url='https://github.com/RenathaPutri/snake-ladder-gemini-cli',
    license='MIT',
    author='Renatha Putri',
    author_email='renathaputri72@gmail.com',
    description='This package contains implementation of a command-line Snake and Ladder game with Google Gemini AI integrated into it.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    entry_points={
        "console_scripts": [
            "snake-ladder-gemini-cli=snake-ladder-gemini-cli.main:main",
        ]
    }
)
