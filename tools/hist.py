import gitrepo 
from os.path import isfile
import os


def locate_file():
    """
        Get the location of the repo file
    """
    return file_loc 


def get_last_git_repo():
    """
        Get the path of the last repo that was 'gimme'd
    """
    path = open(locate_file(), 'r').readline()
    if path and gitrepo.is_repo(path):
        return path
    else: 
        return None


def save_selected_git_repo(repo_path):
    """
        Store the path of the repo that will be 'gimme'd
    """
    repo_file = open(locate_file(), 'w')
    repo_file.write(repo_path)
    repo_file.close()
    print "Path set to %s" % repo_path

# Ensure that file exists
file_loc = '%s/.stools_config/gimme/gimme_hist.txt' % os.path.expanduser('~')
if not isfile(locate_file()):
    save_selected_git_repo('')
