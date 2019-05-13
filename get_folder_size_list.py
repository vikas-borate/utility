import os
import sys

subject_dir='C:\\'

def get_size(start_path):
    total_size = 0
    fl_cnt = 0
    fld_cnt = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            fl_cnt = fl_cnt + 1
            total_size += os.path.getsize(fp)
        for d in dirnames:
        	fld_cnt = fld_cnt + 1
    total_size_mb=(total_size/1024)/1024
    return total_size_mb,fl_cnt,fld_cnt

flw=open("dir_size_report_apr-19.csv","w")

print("Getting size for folders ..",end='',flush=True)
for dirname in os.listdir(subject_dir):
   if "." not in dirname and "Program Files" not in dirname:
       folder_size, child_files, child_folders=get_size(subject_dir + "\\" + dirname)
       #print(folder_size)
       if folder_size < 1:
           folder_size = round(folder_size*1024, 2)
           size_unit="KB"
           #folder_size_str=str(folder_size)+ " KB"
       else:
           folder_size = round(folder_size, 2)
           #folder_size_str = str(folder_size) + " MB"
           size_unit = "MB"
       #print(dirname,folder_size)
       print(".",end='',flush=True)
       flw.write(dirname + "," + str(folder_size) + "," + size_unit + "\n")

print("report generated")
flw.close()
