import os
import pathlib

os.system('venv\Scripts\python.exe -m pip install --upgrade pip')
with pathlib.Path('./requirements.txt').open() as f:
    lib = f.read().splitlines()
for _ in lib:
    os.system('venv\Scripts\pip.exe install -U '+_)
os.system('venv\Scripts\pip.exe freeze > requirements.txt')
