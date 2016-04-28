import os
import subprocess

src = 'src/utils/prepare-commit-msg.py'
dst = '.git/hooks/prepare-commit-msg'

process = subprocess.call(['git', 'init'])
os.symlink(src, dst)
