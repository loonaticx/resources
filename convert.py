import os
import subprocess
import sys

arg = sys.argv[1]

if arg == '--to_egg':
	for fn in os.listdir('.'):
		if os.path.isfile(fn):
			if fn.endswith('.bam'):
				print(fn)
				subprocess.call(['panda_files/bam2egg.exe', fn, fn.replace('.bam', '.egg')])
elif arg == '--to_bam':
	for fn in os.listdir('.'):
		if os.path.isfile(fn):
			if fn.endswith('.egg'):
				print(fn)
				subprocess.call(['panda_files/egg2bam.exe', fn, fn.replace('.egg', '.bam')])
else:
	print('error')