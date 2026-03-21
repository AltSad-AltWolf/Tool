@echo off
chcp 65001 >nul 2>&1

echo Installing required Python modules...
python -m pip install --upgrade pip

python -m pip install requests flask pyngrok phonenumbers pefile python-magic-bin discord.py discord-webhook colorama PyQt5
python -m pip install keyboard pyautogui opencv-python pywin32

echo.
echo All modules installed!
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