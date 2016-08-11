# Example Install
This is the expected output if you are a user 'stcollier' and your collection of git repos is at the path '/Users/stcollier/Git/'

```
stcollier@StefTop:~/Git/gimme$ ./install_gimme.sh /Users/stcollier/Git/
=============================
      Installing gimme
=============================
+Making folders
mkdir: /Users/stcollier/.stools_config: File exists
mkdir: /Users/stcollier/.stools_config/gimme: File exists
+Creating files
+Saving git home to file
install_gimme: Install complete


=============================
  Add this to your .bashrc
=============================

function gimme {
   python /Users/stcollier/Git/gimme/gimme.py $*
   if [ $? -eq 0  ]; then
       cd `cat ~/.stools_config/gimme/gimme_hist.txt`
   fi
}
stcollier@StefTop:~/.stefanscripts/gimme$
```
