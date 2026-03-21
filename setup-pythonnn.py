import subprocess
import sys

modules = [
    "requests",
    "flask",
    "pyngrok",
    "phonenumbers",
    "pefile",
    "python-magic-bin",
    "discord.py",
    "discord-webhook",
    "colorama",
    "PyQt5"
]

for module in modules:
    print(f"Installing {module}...")
    subprocess.run([sys.executable, "-m", "pip", "install", module], check=True)

print("\nDone!")