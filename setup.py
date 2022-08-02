import setuptools

with open("README.md", 'r') as fopen:
    long_description = fopen.read()

setuptools.setup(name='pyCTDeface',
    version='0.1',
    description='Python package for defacing CT scans.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author='Thomas Maloney',
    author_email='malonetc@ucmail.uc.edu',
    license='GNUv3',
    packages=setuptools.find_packages(),
    install_requires=[
        'pydicom',
        'pathlib',
        'numpy'
    ],
    zip_safe=False,
    python_requires='>=3.6')
