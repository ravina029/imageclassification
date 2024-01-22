from setuptools import setup,find_packages
from typing import List
def get_requirements(file_path:str)->List[str]:
  '''this function will return the list of requirements
   '''

  HYPHEN_E_DOT='-e .'
  with open(file_path) as file_obj:
       requirements=file_obj.readlines()
       requirements=[req.replace("\n","")for req in requirements]

       if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

  return requirements        

with open('README.md','r', encoding='utf-8') as f:
    long_description=f.read()




setup(
    name='imageclassifier',
    version='0.0.1',
    author='ravina',
    author_email='vermaravina029@gmail.com',
    description='image classification app',
    long_description=long_description,
    long_description_content='text/markdown',
    url=f'https://github.com/ravina029/imageclassification',
    project_urls={"Bug Tracker":f'https://github.com/ravina029/mlflow_project/issues',},
    package_dir={"":"src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements('requirements.txt')
    )