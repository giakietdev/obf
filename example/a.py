import os, sys 
from giakiethoang import Colors, Colorate
import requests

python_version = sys.version_info[0:3]

info = f"Coder: Trương Quang Thắng\nProject: Obfuscate Python"
python = f"Python: {python_version[0]}.{python_version[1]}.{python_version[2]}"
os_info = f"OS: {os.name} - {os.sys.platform}"

print()
print(Colorate.Horizontal(Colors.yellow_to_neon, info))
print(Colorate.Horizontal(Colors.yellow_to_neon, python))
print(Colorate.Horizontal(Colors.yellow_to_neon, os_info))
print()