import os
import shutil

os.system('python ./version/version.py')
os.system('pip freeze > ./requirements.txt')
shutil.rmtree('./build', ignore_errors=True)
shutil.rmtree('./dist', ignore_errors=True)
os.system('pyinstaller ./main.spec')