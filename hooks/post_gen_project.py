import os
import subprocess

project_dir = '{{cookiecutter.repo_name}}'
hooks_dir = os.path.join(project_dir, '.git/hooks')

src = os.path.join(project_dir, 'src/utils/prepare-commit-msg.py')
dst = os.path.join(hooks_dir, 'prepare-commit-msg')

process = subprocess.call(['git', 'init', project_dir])

os.mkdir('{{cookiecutter.repo_name}}/.git/hooks')
os.symlink(src, dst)
