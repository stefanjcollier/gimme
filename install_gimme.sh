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
#    ./install_gimme.sh       #Installs the gimme command
#
#---


echo '=================================='
echo '         Running Checks'
echo '=================================='
printf '+Installer running in correct pwd  '
if [ -f ./gimme.py ] && [ -e ./.git ]; then
	echo '[Pass]'
else
	echo '[Fail]'
	echo 'Please run the installer in the gimme directory'
	echo;
	exit -1
fi
echo;
echo '=================================='
echo '         Installing gimme'
echo '=================================='
echo '+Making folders'
mkdir ~/.stools_config && true
mkdir ~/.stools_config/gimme && true

echo '+Creating files'
touch ~/.stools_config/gimme/gimme_hist.txt
touch ~/.stools_config/gimme/votes.csv
touch ~/.stools_config/gimme/gimme_function.sh

echo '+Creating function file'
touch ~/.stools_config/gimme/gimme_function.sh
cat gimme_function.sh | sed "s|#GIMME_HOME#|${PWD}|" > ~/.stools_config/gimme/gimme_function.sh
echo 'install_gimme: Install complete'
echo ''
echo '=================================='
echo '  Add this line to your .bashrc:'
echo '=================================='
echo "If you don't, the command won't be in scope!"
echo;
echo 'source ~/.stools_config/gimme/gimme_function.sh'
echo;
