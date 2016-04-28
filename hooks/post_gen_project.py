import os
import subprocess


src = os.path.join(os.getcwd(),'src', 'utils', 'prepare-commit-msg.py')
dst = os.path.join('.git', 'hooks', 'prepare-commit-msg')

process = subprocess.call(['git', 'init'])
os.symlink(src, dst)
