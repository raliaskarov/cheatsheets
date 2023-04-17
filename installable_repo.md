**About** 
Instruction to enable pulling repository code to other environment using pip install

**Objective**
Assume you have table_profiling.py in repo data_analysis_package on git hub.
You want to access it from laptop using pip install.
Here's an example of how you could create a package for your table_profiling.py file

**Steps**:
Create a new directory for your package and name it something like data_analysis_package.

Create a subdirectory called data_analysis_package/data_analysis.

Move your table_profiling.py file into the data_analysis_package/data_analysis directory.

Create a file called __init__.py in the data_analysis_package/data_analysis directory. This file is necessary to tell Python that this directory should be treated as a package.

Create a setup.py file in the root directory of your data_analysis_package directory. This file is used by Python's packaging tools to build and install your package. Here's an example of what your setup.py file might look like:

```
from setuptools import setup

setup(
    name='data_analysis_package',
    version='0.1',
    packages=['data_analysis'],
    install_requires=[],
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for data analysis functions',
    url='https://github.com/yourusername/data_analysis_package'
)
```
In your other projects, you can then install your package using pip: pip install git+https://github.com/yourusername/data_analysis_package.git.

With this setup, you can easily reuse your profile_dataframe(df) function in multiple projects by simply importing it from your data_analysis package:
```
from data_analysis.table_profiling import profile_dataframe

# Use the function in your code
profile_dataframe(df)
```
