@echo off
echo Installing modules...

python -m pip install requests flask pyngrok phonenumbers pefile python-magic-bin discord.py discord-webhook colorama PyQt5

echo.
echo Done!
pause