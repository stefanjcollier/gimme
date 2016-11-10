import os
import subprocess
from core import folder_not_hidden


def is_repo(path):
    """
        A dir is a repo if it contains a .git folder within it
    """
    return '.git' in os.listdir(path)


def get_repos():
    """
        Returns all the folders that are git repos
    """
    output = subprocess.check_output([
        'find',
        os.path.expanduser('~'),
        '!', '-perm', '-g+r,u+r,o+r', '-prune',  # Ignore 'Permission Denied' folders
        '-o',
        '-type',
        'd',
        '-name',
        '.git',
        '-print'
    ]).split('\n')[:-1]
    return (git_path[:-4] for git_path in output if folder_not_hidden(git_path[:-4]))
