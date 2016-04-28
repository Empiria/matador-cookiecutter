import os

src = '{{cookiecutter.repo_name}}/src/utils/prepare-commit-msg.py'
dst = '{{cookiecutter.repo_name}}/.git/hooks/prepare-commit-msg'

os.mkdir('{{cookiecutter.repo_name}}/.git/hooks')
os.symlink(src, dst)
