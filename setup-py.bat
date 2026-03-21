@echo off
chcp 65001 >nul 2>&1

echo Installing modules...
python -m pip install requests flask pyngrok phonenumbers pefile python-magic-bin discord.py discord-webhook colorama PyQt5
echo.
echo Done!
echo.

where wt >nul 2>&1
if %errorlevel% == 0 (
    wt.exe --title "AltTool" python "%~dp0Alt-tool-Free.py"
    exit
)

powershell.exe -NoProfile -Command ^
    "[Console]::OutputEncoding=[System.Text.Encoding]::UTF8;" ^
    "[Console]::InputEncoding=[System.Text.Encoding]::UTF8;" ^
    "& python '%~dp0Alt-tool-Free.py'"

exit