from os import listdir
from os.path import join, isdir, isfile
from core import out
import os

# The location of the file that says where the git repo is stored
git_home_loc_path = '%s/.stools_config/gimme/git_home_loc.txt' % os.path.expanduser('~')

"""
    Asks the user for the git home
"""
def define_git_home():
    inp = raw_input("gimme: Please enter your the location of the folder holding all your git repos\n>")
    git_loc_file = open(git_home_loc_path, 'w')
    git_loc_file.write(inp)

"""
    A dir is a repo if it contains a .git folder within it
"""
def is_repo(path):
    return '.git' in listdir(path)

def locate_git():
    return git_home

"""
    Returns all the folders that are git repos
"""
def get_repos():
    git = locate_git()
    dirs = listdir(git)
    return [dir for dir in dirs if isdir(join(git,dir)) and is_repo(join(git,dir))]

# Ensure file exists and git_home is a real git folder
if not isfile(git_home_loc_path):
    define_git_home()

# Ensure the location in the file is valid
git_home = open(git_home_loc_path,'r').readline().rstrip()
if not git_home:
    out('The path to your git home is empty, please enter a new one')
    define_git_home()

elif not isdir(git_home):
    out('The chosen path (\'%s\') for your git home is not a valid path, please enter a new one' % git_home)
    define_git_home()

