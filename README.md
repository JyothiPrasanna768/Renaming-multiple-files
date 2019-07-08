# Renaming-multiple-files
How to rename multiple files or data sets  which is in Google drive using Python ?
Renaming the multiple files is a difficult task .It is simply  achieved using the rename() and listdir() methods in os module.

Let we achieve this in 4 steps.
 
Step 1: Open Google Colaboratory .Import drive and files in a google colab by using below commands. Here I want to rename files  which is in data_label folder.So, I had given a path in data variable
Step 2: Here listdir() function is used to list out all the content in a given directory. 
Step 3: Now, define a function to rename multiple files . Here I used split function to divide the name of a file into 2 keywords.And I am renaming the file with first keyword with .png extension.
Step 4: Call the main function
