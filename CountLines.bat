@echo off

REM - Created by Vikas Borate

echo.> Count_Lines_Report.csv

ECHO "Report Process Started"

FOR /F "delims=" %%A IN ('DIR /B /S *.*') do (

FOR /F %%B IN ('findstr /R /N "^" ^"%%A^" ^| find /C ":"') DO (

ECHO %%~nxA,%%~dpA,%%B >>Count_Lines_Report.csv

)
)

ECHO "Report Generated"
