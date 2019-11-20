import os 
  
# Get the list of all files and directories 
path = "/"
dir_list = os.listdir(path)
dir_list = os.path.isdir(path)
  
print("Files and directories in '", path, "' :")  
print(dir_list) 
