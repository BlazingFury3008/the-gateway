@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

:: MySQL Credentials
SET MYSQL_USER=root
SET MYSQL_PASSWORD=Dasher123@bc
SET MYSQL_DATABASE=fastapi_db
SET MYSQL_HOST=localhost

:: Find MySQL Installation Path and mysql.exe dynamically (Handling Spaces Properly)
SET MYSQL_CMD=""
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

:: Find the MySQL Service Name dynamically
FOR /F "tokens=2 delims=: " %%I IN ('sc query state^= all ^| findstr /I "MySQL"') DO SET "MYSQL_SERVICE=%%I"

:: Check if MySQL is running
tasklist | find /i "mysqld.exe" >nul
IF ERRORLEVEL 1 (
    echo MySQL server is not running. Attempting to start it...
    net start "!MYSQL_SERVICE!"
    
    :: Wait a few seconds to allow MySQL to start
    timeout /t 5 /nobreak >nul

    :: Check again if MySQL started successfully
    tasklist | find /i "mysqld.exe" >nul
    IF ERRORLEVEL 1 (
        echo Failed to start MySQL. Please start it manually.
        pause
        exit
    ) ELSE (
        echo MySQL started successfully.
    )
) ELSE (
    echo MySQL server is already running.
)

:: Check if the database exists, create it if not
echo Checking if database %MYSQL_DATABASE% exists...
echo CREATE DATABASE IF NOT EXISTS %MYSQL_DATABASE%; | "!MYSQL_CMD!" -h %MYSQL_HOST% -u %MYSQL_USER% -p"%MYSQL_PASSWORD%"
IF ERRORLEVEL 1 (
    echo Failed to check/create database. Please verify credentials.
    pause
    exit
) ELSE (
    echo Database %MYSQL_DATABASE% is ready.
)

:: Execute all SQL files in the current directory
echo Running SQL scripts...
for %%f in (*.sql) do (
    echo Executing %%f...
    "!MYSQL_CMD!" -h %MYSQL_HOST% -u %MYSQL_USER% -p"%MYSQL_PASSWORD%" %MYSQL_DATABASE% < "%%f"
)

echo SQL execution completed.
pause
