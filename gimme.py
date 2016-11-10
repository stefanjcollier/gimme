#!/usr/bin/env python

#---
# Description:
#   A script to find a git repository based on a subset of the name
# 
# Usage:
#   $gimme <substring>                      # Return the path to the repo that contains that substring
#   $gimme [-f | --force-first] <substring> # Return the first path to the repo that contains that substring
#   $gimme [-a | --add-path] <path>         # Add a path to search tree
#   $gimme -                                # Return the last repo that was searched for
#
# Example:
#   $gimme example
#   >/Users/MyUser/Git/my-example-repo/
#
#---

import sys

from tools.core import *
from tools.gitrepo import *
from tools.hist import *
import learn


def substring_of_any_path(substring, paths):
    """ Return TRUE if the substring is a subtring of any the paths """
    return substring != '' and any([substring in path for path in paths])


def option_in_range(option,paths):
    """ Return TRUE if the option is a valid index to one of the paths """
    return option.isdigit() and int(option) in range(len(paths))


def narrow_search_down(paths):
    """
        Given the reduced options (from the command argument).
        Loop allowing the user to reduce the results and choose an option
    """
    print_options(paths)
    print 'Select an option by entering an option, e.g. $ 2'
    print '  or enter another substring to narrow it down e.g. $ chef'
    choice = user_input()

    # Ensure that the user chooses a valid substring or index
    while not (substring_of_any_path(choice, paths) or option_in_range(choice, paths)):
        print 'Enter a valid string (see above).'
        choice = user_input() 

    # Determine if it was a index
    if option_in_range(choice, paths):
        path = paths[int(choice)]
        
        learn.choose(path)
        save_selected_git_repo(path)
        exit(0)

    # Or if it was a substring
    elif substring_of_any_path(choice, paths):
        less_paths = list(set([path for path in paths if choice in path]))
        if len(less_paths) == 1:
            selected_repo = less_paths[0]
            learn.choose(selected_repo)
            save_selected_git_repo(selected_repo)
            exit(0)
        else:
            narrow_search_down(less_paths)


# Find the repo based on search
def find_matching_repo(search_term, allow_first=False):
    # Find the repos that match the search string
    matchers = list(set([repo for repo in get_repos() if search_term in repo]))
    if len(matchers) == 0:
        out('No repo matches the description \'%s\'' % search_term)
        exit(-1)

    # Only found one matching repo
    elif len(matchers) == 1:
        selected_repo = matchers[0]
        save_selected_git_repo(selected_repo)
        exit(0)

    else:
        matchers = learn.sort(matchers)
        if allow_first:
            first_repo = matchers[0]
            save_selected_git_repo(first_repo)
            exit(0)
        else:
            out('Your search produced more than one repo:')
            print 'Please be more specific'
            narrow_search_down(matchers)
            exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] == '--help':
        display_usage()
        exit(5)

    first_arg = sys.argv[1]

    if first_arg == '-':
        if not get_last_git_repo():
            out('You have not yet used \'gimme\' to get to a repo')
            exit(2)

    elif first_arg in ['-f', '--force-first']:
        search = ' '.join(sys.argv[2:])
        find_matching_repo(search, True)

    elif first_arg in ['-a', '--add-path']:
        new_search_path = ' '.join(sys.argv[2:])
        if new_search_path:
            try:
                gitrepo.append_to_search_file(new_search_path)
            except PathDoesNotExistException as ex:
                print ex.message
        else:
            out('That was blank, please enter a valid path next time')

    else:
        search = ' '.join(sys.argv[1:])
        find_matching_repo(search)
