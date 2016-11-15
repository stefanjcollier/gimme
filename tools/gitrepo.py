import os
import subprocess
from core import folder_not_hidden
from os.path import isfile, isdir

file_loc = '%s/.stools_config/gimme/other_search_locs.txt' % os.path.expanduser('~')


class PathDoesNotExistException(Exception):
    pass


def is_repo(path):
    """ A dir is a repo if it contains a .git folder within it
    :param path -- The single location
    :return True if the path is a code repository
    """
    return '.git' in os.listdir(path)


def get_repos():
    """ Returns all the folders that are git repos """
    output = subprocess.check_output([
        'find',
        os.path.expanduser('~')] +
        other_search_locations()
        + ['!', '-perm', '-g+r,u+r,o+r', '-prune',  # Ignore 'Permission Denied' folders
        '-o',
        '-type',
        'd',
        '-name',
        '.git',
        '-print'
    ]).split('\n')[:-1]
    return (git_path[:-4] for git_path in output if folder_not_hidden(git_path[:-4]))


def append_to_search_file(new_search_path):
    """ Add a path to the file that contains the extra paths to find repos in """
    # Ensure path exists
    if not isdir(new_search_path):
        raise PathDoesNotExistException('The path {} does not exist on this machine'.format(new_search_path))

    # Add it to the file!
    with open(file_loc, 'a+') as repo_file:
        repo_file.write(new_search_path+'\n')
    print "Appended \'{}\' to search paths".format(new_search_path)


def other_search_locations():
    """ Return a list of string paths for places other than ~ to start looking from """
    other_locs = []
    with open(file_loc, 'r') as loc_file:
        for loc in loc_file:
            other_locs += [loc.rstrip('\n')]
    if len(other_locs) > 0:
        print "Searching in: {}".format([os.path.expanduser('~')]+other_locs).replace(']', '').replace('[', '')
    return other_locs


# Ensure that file exists
if not isfile(file_loc):
    with open(file_loc, 'w') as f:
        f.write(' ')
