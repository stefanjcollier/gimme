#!/bin/bash

#---
# Description:
#
#
# Usage:
#
#
#---

#This is the basic function that will need to be changed
#You will need to 'find' the gimme.py and then you can use the function easy peasy

# Find the gimme.py file


function gimme {
	python #GIMME_HOME#/gimme.py $*
	if [ $? -eq 0 ]; then
		cd `cat  ~/.stools_config/gimme/gimme_hist.txt`
	fi
}
