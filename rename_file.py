# Переименование файлов с заменой 
# американского формата дат европейским 
import re
import os
import shutil

datePattern = re.compile(r'''
	((0|1)?\d)-
	((0|1|2|3)?\d)-
	((19|20)?\d\d)
	(.*)$
''', re.VERBOSE
)

path = os.getcwd()

for file in os.listdir(path):
	mo = datePattern.search(file)

	if mo == None:
		continue

	month = mo.group(1)
	date = mo.group(3)
	year = mo.group(5)
	ext = mo.group(7)

	eurofile = date + '-' + month + '-' + year + ext
	absworkDir = os.path.join(path, eurofile)

	shutil.move(os.path.join(path, file), eurofile)