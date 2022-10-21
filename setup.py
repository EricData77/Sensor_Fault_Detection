from setuptools import find_packages, setup
from typing import List

def get_requirement() -> List[str]:
    """
    This function will return a list of requirements
    """
    requirement_list:List[str] = []
    """
    Write a code to read requirement.txt file and append each requirements in requirement_list variable
    """
    return requirement_list

setup(
    name = "sensor",
    version = "0.0.1",
    author = "Eric Tran",
    author_email = "ericdataguy77@gmail.com",
    packages = find_packages(),
    install_requires= get_requirement()#["pymongo==4.2.0"],
)

