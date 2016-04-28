import os
import subprocess

project_dir = '{{cookiecutter.repo_name}}'
src = os.path.join(project_dir, 'src/utils/prepare-commit-msg.py')
dst = os.path.join(project_dir, '.git/hooks/prepare-commit-msg')

process = subprocess.call(['git', 'init', project_dir])
os.symlink(src, dst)
