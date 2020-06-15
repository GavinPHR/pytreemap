import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name='pytreemap',
  packages=setuptools.find_packages(),
  version='0.2',
  license='gpl-2.0',
  description='High-performance Python Implementation of the Java TreeMap API',
  author_email='gavinsweden@gmail.com',
  url='https://github.com/GavinPHR/pytreemap',
  keywords=['python3', 'self-balancing', 'binary-search-tree', 'red-black-tree', 'java', 'treemap', 'treeset'],
  install_requires=[
      ],
  classifiers=[
    'Programming Language :: Python :: 3',
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
  ],
  python_requires='>=3.5',
  long_description=long_description,
  long_description_content_type='text/markdown'
)
