import setuptools

# read the contents of your README file
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'pytreemap',         # How you named your package folder (MyLib)
  # packages=setuptools.find_packages(),
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='gpl-2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'High-performance Python Implementation of the Java TreeMap API',   # Give a short description about your library
  author = 'Haoran Peng',                   # Type in your name
  author_email = 'gavinsweden@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/GavinPHR/pytreemap',   # Provide either the link to your github or to your website
  keywords = ['python3', 'self-balancing', 'binary-search-tree', 'red-black-tree', 'java', 'treemap', 'treeset'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          # 'numpy',
          # 'scipy',
          # 'space-time-astar'
      ],
  classifiers=[
    'Programming Language :: Python :: 3',
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',   # Again, pick a license
  ],
  python_requires='>=3.5',
  long_description=long_description,
  long_description_content_type='text/markdown'
)