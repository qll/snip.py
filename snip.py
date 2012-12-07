#!/usr/bin/env python
# symlink this to /usr/bin/ to access it from everywhere:
# ln -s snip.py /usr/bin/snip.py
# Works with Python 2.7 and 3
import sys
import os
import shutil


CFG_PATH = '~/.config/snip.py/'
STANDARD_CFG = """# snip.py standard configuration

# snip.py searches in all PATHs for snippets, upper ones have priority in case of duplicates
# snip.py will skip all hidden directories and files (starting with a dot)
SNIP_PATH = (
	'{file_path}',
#	'~/some/dir',
)
"""

def fill_snippets(path, snippets):
	""" Fill snippets with scripts from SNIP_PATH """
	path = path if path.endswith('/') else path + '/'
	for file_or_dir in os.listdir(path):
		if file_or_dir.startswith('.'):
			continue
		if os.path.isdir(path + file_or_dir):
			snippets[file_or_dir] = {}
			fill_snippets(path + file_or_dir, snippets[file_or_dir])
		elif os.path.isfile(path + file_or_dir):
			snippets[file_or_dir] = path + file_or_dir


# first start logic and loading settings
CFG_PATH = os.path.expanduser(CFG_PATH)
sys.path.append(CFG_PATH)
if not os.path.isfile(CFG_PATH + 'settings.py'):
	print('It seems as if you are using snip.py the first time. Have fun!')
	print('[INFO] Creating standard config in {0}settings.py'.format(CFG_PATH))
	if not os.path.exists(CFG_PATH):
		os.makedirs(CFG_PATH)
	with open(CFG_PATH + 'settings.py', 'w') as f:
		current_dir = os.path.dirname(os.path.realpath(__file__))
		f.write(STANDARD_CFG.format(file_path=current_dir))
from settings import *


# build list of all snippets
snippets = {}
# reversed makes sure the first entries have higher priority
for path in reversed(SNIP_PATH):
	path = os.path.expanduser(path) 
	if not os.path.isdir(path):
		print('[WARNING] {0} is not a directory. I will skip this.'.format(path))
		continue
	fill_snippets(path, snippets)	
if not snippets:
	print('[ERROR] No snippet found. Exiting.')
	sys.exit(1)


# program logic
if len(sys.argv) < 2:
	print('Usage: {0} /snip.py/path [dest_file]'.format(sys.argv[0]))
	sys.exit(1)
current_path = snippets
for path in sys.argv[1].split('/'):
	if not path:
		continue
	if path not in current_path:
		print('[ERROR] Snippet {0} not found.'.format(sys.argv[1]))
		sys.exit(1)
	current_path = current_path[path]
if isinstance(current_path, dict):
	print('\n'.join('DIR ' + k if isinstance(current_path[k], dict) else k for k in current_path))
elif len(sys.argv) > 2:
	try:
		shutil.copyfile(current_path, sys.argv[2])
	except FileNotFoundError as e:
		print('[ERROR] Could not copy snippet to {0}:'.format(sys.argv[2]))
		print(e)
	else:
		print('Copied snippet {0} to {1}'.format(sys.argv[1], sys.argv[2]))
else:
	with open(current_path, 'r') as f:
		print(f.read())
