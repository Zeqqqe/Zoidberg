@echo off
setlocal

:: Get the directory where this script is located (and presumably Zoidberg.exe)
set "APP_DIR=%~dp0"
echo Application directory: "%APP_DIR%"

:: Check if the directory is already in the user's PATH to avoid duplicates
echo Checking if "%APP_DIR%" is already in PATH...
reg query HKCU\Environment /v Path | find /I "%APP_DIR%" > nul
if %errorlevel%==0 (
    echo Directory already in user PATH. No action needed.
) else (
    echo Adding "%APP_DIR%" to user PATH...
    :: Use setx to make the change persistent for the current user
    setx PATH "%PATH%;%APP_DIR%"
    echo Directory added to user PATH.
    echo Please open a NEW Command Prompt/PowerShell window for the change to take effect.
)

pause
endlocal