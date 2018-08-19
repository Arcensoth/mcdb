from setuptools import find_packages, setup

with open('VERSION.txt') as fp:
    version = fp.read().strip()

with open('README.md') as fp:
    readme = fp.read()

with open('requirements.txt') as fp:
    requirements = fp.read().splitlines()

setup(
    name='mcdb',
    version=version,
    author='Arcensoth',
    author_email='arcensoth@gmail.com',
    url='https://github.com/Arcensoth/mcdb',
    license='MIT',
    description='Minecraft data query program for commands, NBT, blockstates, and more. Inspired by the in-game help command and auto-completion, with added features like multiple version support and expandable regex search.',
    long_description_content_type='text/markdown',
    long_description=readme,
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
    keywords='minecraft database cli help utility commands blocks nbt',
    classifiers=(
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
    )
)
