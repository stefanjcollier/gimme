import os
import subprocess
from core import folder_not_hidden
import learn

"""
    A dir is a repo if it contains a .git folder within it
"""
def is_repo(path):
    return '.git' in os.listdir(path)

"""
    Returns all the folders that are git repos
"""
def get_repos():
    output = subprocess.check_output([
        'find',
        os.path.expanduser('~'),
        '-name',
        '.git']).split('\n')[:-1]
    return (git_path[:-4] for git_path in output if folder_not_hidden(git_path[:-4]))

