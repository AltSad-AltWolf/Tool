@echo off
chcp 65001 >nul 2>&1

echo Installing required Python modules...
python -m pip install --upgrade pip

:: Modules externes requis
python -m pip install requests flask pyngrok phonenumbers pefile python-magic-bin discord.py discord-webhook colorama PyQt5 keyboard pyautogui opencv-python pywin32

echo.
echo All modules installed!
echo.

:: Run the executable
"%~dp0Alt-tool-free.exe"

exit