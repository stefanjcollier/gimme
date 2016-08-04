from gitrepo import is_repo
from os.path import isfile

file_loc = None

"""
    Initialize the file_loc based on something 
"""
def init_file_loc():
    global file_loc
    file_loc = '/Users/stcollier/.gimme.properties'

"""
    Get the location of the repo file
"""
def locate_file():
    return file_loc 

"""
    Ensure the repo file exists at the given location
"""
def assert_file():
    init_file_loc()
    if not isfile(locate_file()):
        save_selected_git_repo('')

"""
    Get the path of the last repo that was 'gimme'd
"""
def get_last_git_repo():
    path = open(locate_file(),'r').readline()
    if is_repo(path):
        return path
    else: 
        return None
"""
    Store the path of the repo that will be 'gimme'd
"""
def save_selected_git_repo(repo_path):
    repo_file = open(locate_file(), 'w')
    repo_file.write(repo_path)
    repo_file.close()
    print "Path set to %s" % repo_path


