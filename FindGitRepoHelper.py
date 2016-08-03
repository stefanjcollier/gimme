from os import listdir
from os.path import join, isdir

def out(text):
    print "gimme: %s" % text

def init_git():
    return '/Users/stcollier/Git/'

"""
    A dir is a repo if it contains a .git folder within it
"""
def is_repo(git, repo):
    test_repo = join(git,repo) 
    return '.git' in listdir(test_repo)

"""
    Returns all the folders that are git repos
"""
def get_repos(git):
    dirs = listdir(git)
    return [dir for dir in dirs if isdir(join(git,dir)) and is_repo(git, dir)]


