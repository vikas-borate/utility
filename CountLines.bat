@echo off

REAM - This script creates a report with filenames and number of lines of each file in all subfolders of current folder

REM - Created by Vikas Borate

echo.> Count_Lines_Report.txt

FOR /F %%A IN ('DIR /B /S *.txt') do (

FOR /F %%B IN ('findstr /R /N "^" %%A ^| find /C ":"') DO (

ECHO %%~nxA,%%~dpA,%%B >>Count_Lines_Report.txt

)
)
