import pyinstaller_versionfile
import datetime
import pathlib

author = 'Angel Liao'
ProjectName = 'TBD'
today = datetime.datetime.today()
major = 0
minor = 1
revise = str(today.isocalendar().year)[-2:] + '{:02d}'.format(today.isocalendar().week)
build = str(today.isoweekday())  # + '{:02d}{:02d}'.format(today.hour, today.minute)
version = str(major)+'.'+str(minor)+'.'+revise+'.'+str(build)
strMsg = '__version__ = "' + version + '"\n' + \
         '__author__ = "' + author + '"'

pathlib.Path('./src/__init__.py').open('w').write(strMsg)

pyinstaller_versionfile.create_versionfile(
    # output_file="versionfile.txt",
    output_file=pathlib.Path("./version/versionfile.txt"),
    # version=str(major)+'.'+str(minor)+'.'+revise+'.'+str(build),
    version=version,
    # version="0.1.0.0",
    company_name="Jay Su Imaginary Company",
    file_description=ProjectName,
    internal_name=ProjectName,
    legal_copyright="© Jay Su Imaginary Company. All rights reserved.",
    original_filename=ProjectName+".exe",
    product_name=ProjectName
)
