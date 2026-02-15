@echo off
echo Installing required Python packages...

REM
python -m pip install --upgrade pip

REM
pip install phonenumbers requests discord.py pyngrok flask colorama pillow pyinstaller certifi

echo.
echo All packages installed!
pause
