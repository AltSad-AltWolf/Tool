@echo off
echo Installing required Python packages...

REM
python -m pip install --upgrade pip

REM
pip install phonenumbers requests discord.py flask colorama pillow PyInstaller pyngrok PyQt5 beautifulsoup4 reportlab python-magic-bin pefile lxml urllib3 PyPDF2 pywin32 cryptography psutil
python -m pip install phonenumbers requests discord.py flask colorama pillow PyInstaller pyngrok PyQt5 beautifulsoup4 reportlab python-magic-bin pefile lxml urllib3 PyPDF2 pywin32 cryptography psutil
echo.
echo All packages installed!
pause
