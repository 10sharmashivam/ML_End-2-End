from setuptools import find_packages,setup
from typing import List

# Constant for identifying the editable install mode
HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    Reads the requirements from a file and returns them as a list of strings.
    
    Args:
        file_path (str): The path to the requirements file.
    
    Returns:
        List[str]: A list of package requirements, excluding the editable mode indicator.
    """
    requirements = []
    # Open the requirements file and read the contents
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()       # Read all lines from the file
        # Remove newline characters from each line
        requirements = [req.replace("\n", "") for req in requirements]
        
        # Remove the editable mode indicator if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements 


# Setup configuration for the package
setup(
    name='ML_Project',
    version='0.0.1',
    author='Shivam',
    author_email='10sharmashivam@gmail.com',
    packages=find_packages(),               # Automatically find and include all packages in the project
    install_requires=get_requirements('requirements.txt')        # List of package dependencies
    
    
)