import glob
import os

# Dynamically loads fixtures from all python files.

pytest_modules = list()
for python_file in glob.glob("**/*[!test_|__init__|conftest]*.py", recursive=True):
    path_list = python_file.split(os.sep)
    module_name = path_list[-1][:-3]
    pytest_modules.append(".".join(path_list[:-1]) + "." + module_name)

pytest_plugins = pytest_modules
