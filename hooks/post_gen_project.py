import os
import subprocess

src = os.path.join(os.getcwd(), 'src', 'utils', 'prepare-commit-msg.py')
dst = os.path.join('.git', 'hooks', 'prepare-commit-msg')

subprocess.call(['git', 'init'])
os.symlink(src, dst)
subprocess.call(['git', 'add', '-A'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
