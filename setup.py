from setuptools import setup
import glob
import os
import sys
from hera_sim import version
import json

data = [version.git_origin, version.git_hash, version.git_description, version.git_branch]
with open(os.path.join('hera_sim', 'GIT_INFO'), 'w') as outfile:
    json.dump(data, outfile)

def package_files(package_dir,subdirectory):
    # walk the input package_dir/subdirectory
    # return a package_data list
    paths = []
    directory = os.path.join(package_dir, subdirectory)
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            path = path.replace(package_dir + '/', '')
            paths.append(os.path.join(path, filename))
    return paths
data_files = package_files('hera_sim','data')

setup_args = {
    'name': 'hera_sim',
    'author': 'HERA Team',
    'url': 'https://github.com/HERA-Team/hera_sim',
    'license': 'BSD',
    'description': 'collection of simulation routines describing the HERA instrument.',
    'package_dir': {'hera_sim': 'hera_sim'},
    'packages': ['hera_sim'],
    'include_package_data': True,
    #'scripts': ['scripts/firstcal_run.py', 'scripts/omni_apply.py',
    #            'scripts/omni_run.py', 'scripts/extract_hh.py'],
    'version': version.version,
    'package_data': {'hera_sim': data_files},
    'zip_safe': False,
}


if __name__ == '__main__':
    apply(setup, (), setup_args)
