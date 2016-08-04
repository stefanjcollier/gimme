from os import listdir
from os.path import join, isdir


def locate_git():
    return '/Users/stcollier/Git/'

"""
    A dir is a repo if it contains a .git folder within it
"""
def is_repo(path):
    return '.git' in listdir(path)

"""
    Returns all the folders that are git repos
"""
def get_repos(git):
    dirs = listdir(git)
    return [dir for dir in dirs if isdir(join(git,dir)) and is_repo(join(git,dir))]


