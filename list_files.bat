@echo off

REM Create html file of all files with filespath in current and all subfolders

REM  Created by Vikas Borate

echo.>List_Files.html
FOR /F "delims==" %%A IN ('DIR /B /S *.*') do (
rem echo %%~nxA,%%~fpA                     

set str=a href

ECHO ^<a^ href^=^'%%~fpA^'^>%%~nxA^<a^>^ ^|^ %%~dpA >>List_Files.html

ECHO ^<br^> >>List_Files.html
)
