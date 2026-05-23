from typing  import List
from setuptools import find_packages, setup

def get_requirements() -> List[str]:
   """
   This function will return list of requirements
   """
   requirement_list:List[str] = []

   try:
      #Open and read the requirement.txt file
      with open('requirements.txt', 'r') as file:
         # Read lines from the file
         lines = file.readlines()
         # Process each line 
         for line in lines:
            # Strip whitespace and ignore empty lines
            requirement = line.strip()
            if requirement and requirement != '-e .':
               requirement_list.append(requirement)
   except FileNotFoundError:
      print("requirements.txt file not found. Please ensure it exists in the same directory as setup.py.")
   return requirement_list

print(get_requirements())
setup(
   name='AI-TRAVEL-PLANNER',
   version="0.0.1",
   author="Anuj Modi",
   author_email="modianuj7613@gmail.com",
   install_requires=get_requirements(),
   packages=find_packages()
)
