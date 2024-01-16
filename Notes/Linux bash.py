----- MAKE DIR | mkdir <name> ---------------------------------------------------------------
----- REMOVE DIR | rmdir <name>
----- COPY copy this file at this directory to new directory | cp <path> <newpath> ---------------------------------------------------------------
cp ../filename.txt .  | .. = (old) parent directory  . = (new) current directory
----- COPY SIMPLE #1 | cp <oldname> <newname> ----
----- RENAME or MOVE | mv <oldname> <newname> ----
----- 
----- NEW FILE | touch filename.txt---------------------------------------------------------------
----- REMOVE | rm <filename>  ---------------------------------------------------------------
----- REMOVE ALL | rm *  ---------------------------------------------------------------
----- REDIRECT RESULTS/OUTPUT TO FILE | ./script.py > results.txt
      (CREATES NEW FILE IF DOESN'T EXIST AND ALWAYS OVERWRITES)
----- APPEND RESULTS/OUTPUT TO FILE | ./script.py >> results.txt
      (CREATES NEW FILE IF DOESN'T EXIST AND APPENDS)
----- REDIRECT INPUT TO A FILE | ./script.py < results.txt
       (input is in script, and fills input from results.txt)
----- REDIRECT ERRORS TO A NEW FILE | ./script.py < results.txt 2> errors.txt