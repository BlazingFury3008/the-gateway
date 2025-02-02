@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

:: MySQL Credentials
SET MYSQL_USER=root
SET MYSQL_PASSWORD=Dasher123@bc
SET MYSQL_DATABASE=fastapi_db

:: Find MySQL Installation Path and mysql.exe dynamically
SET "MYSQL_CMD="

FOR /D %%D IN ("C:\Program Files\MySQL\*", "C:\Program Files (x86)\MySQL\*") DO (
    IF EXIST "%%D\bin\mysql.exe" (
        SET "MYSQL_CMD=%%D\bin\mysql.exe"
    )
)

:: If not found, check PATH variable
IF "%MYSQL_CMD%"=="" (
    FOR %%P IN (mysql.exe) DO SET "MYSQL_CMD=%%~$PATH:P"
)

:: Check if MySQL executable was found
IF "%MYSQL_CMD%"=="" (
    echo MySQL executable not found. Please install MySQL or add it to PATH.
    pause
    exit
)

:: Open MySQL terminal properly
echo Opening MySQL terminal...
start "MySQL Terminal" cmd /k ""%MYSQL_CMD%" -u %MYSQL_USER% -p"
