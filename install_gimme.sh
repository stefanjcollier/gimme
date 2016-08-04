#!/bin/bash

#---
# Description:
#   Installs 'gimme' by including the structure:
#   
#   ~/
#   |-.stools_config/
#       |-gimme/
#           |-git_home_loc.txt
#           |-gimme_hist.txt
#
# Usage:
#    ./install_gimme.sh <path>      #Installs the gimme command
#
#  where <path> is the path to the users folder with all their git repos
#---
if [ -z $1 ]; then
    echo 'Usage:'
    echo '   ./install_gimme.sh <path>      Installs the gimme command' 
    echo ''
    echo '   Where <path> is the path to the users folder with all their git repos'

    exit -2
fi
echo '===================='
echo '  Installing gimme'
echo '===================='
echo '+Making folders'
mkdir ~/.stools_config && true
mkdir ~/.stools_config/gimme && true

echo '+Creating files'
touch ~/.stools_config/gimme/git_home_loc.txt
touch ~/.stools_config/gimme/gimme_hist.txt

echo '+Saving git home to file'
git_home=$1
if [ ! -d $git_home ]; then
    echo "install_gimme: '${git_home}' is not a valid directory"
    exit -1
fi

echo $git_home > ~/.stools_config/gimme/git_home_loc.txt
echo 'install_gimme: Install complete'

