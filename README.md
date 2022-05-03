# Utility Scripts

## Get Folder Size
### Problem: 
In Windows, when you want to clean up your HDD, you can sort files by size and then check what is required or not. However, you do not get folder sizes and hence you have to go each individual folder to check contents. 
### Solution: 
If you can get folders listed along with size of each folder you can easily see what is consuming your disk space. **get_folder_size_list.py** python script creates a list of folders along with their sizes by recuresively traversing the subfolders.

How to use this script:
- Download script and copy to any of your folders
- Add/change top level folder from which script should start scanning subfolders
- Change name of the csv file which is report showing folder names along with sizes
- Change/Add folders to skip like 'Program Files' is already added in script so script will not scan Program Files folder
- Save the script and run it using python command
- After script run is complete, you should see csv report created in the same folder or whatever path you specified in script

## Get number of lines 
### Problem:
When you want to do rough estimates based on lines of codes for legacy apps(C, COBOL, Java, Ksh etc), you need quick report of lines of code(LOC). Your code might be in different subfolders which makes in difficult ot do it in single command

### Solution:
You can get report of program/script names along with number of lines in each program. You can use Windows batch file **CountLines.bat** to get such report in csv format.
This is windows batch script so you cna run it wihout installing any other programming langauage or any IDE

How to use this script:
- Download script and copy to top level folder of your codebase
- Change report file names mentioned in code
- Add/change file extensions on line number 9
- Save and run the script from dos command line or powershell
- After script run is complete you should find csv report in the same folder from where you ran the script





