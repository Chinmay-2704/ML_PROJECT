# The whole project/application is put in setup.py file as a package. All the information is present in setup.py file.
# (Author, date , lisence, provider etc)

from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''This function will return the list of requirements from the requirements.txt file.'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'chinmay',
    author_email = 'chinmay@example.com',
    description = 'A machine learning project',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
    # get_requirements is a function which will read the requirements.txt file and return the list of requirements. We will define this function in a separate file called utils.py and import it here. 
)
