@echo off
setlocal

:: Get the directory where this script is located (and presumably Zoidberg.exe)
set "APP_DIR=%~dp0"
echo Application directory: "%APP_DIR%"

:: Check for administrative privileges
NET SESSION >nul 2>&1
if %errorlevel% == 0 (
    echo Running with Administrator privileges.
) else (
    echo ERROR: This script needs to be "Run as administrator" to modify system PATH.
    echo Right-click this .bat file and select "Run as administrator".
    pause
    exit /b 1
)

:: Check if the directory is already in the system PATH to avoid duplicates
echo Checking if "%APP_DIR%" is already in system PATH...
reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path | find /I "%APP_DIR%" > nul
if %errorlevel%==0 (
    echo Directory already in system PATH. No action needed.
) else (
    echo Adding "%APP_DIR%" to system PATH...
    :: Use setx to make the change persistent for the entire system
    :: The /M switch indicates a machine-wide (system) variable
    setx PATH "%PATH%;%APP_DIR%" /M
    echo Directory added to system PATH.
    echo Please open a NEW Command Prompt/PowerShell window for the change to take effect.
)

pause
endlocal