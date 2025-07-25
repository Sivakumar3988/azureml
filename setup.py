from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->list[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name='azuremlproject',
    version='0.0.1',
    author='Siva',
    author_email='sivakumarbokam22@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)