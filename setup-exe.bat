@echo off
chcp 65001 >nul 2>&1

echo Installing modules...
python -m pip install requests flask pyngrok phonenumbers pefile python-magic-bin discord.py discord-webhook colorama PyQt5
echo.
echo Done!
echo.

"%~dp0Alt-tool-free.exe"

exit