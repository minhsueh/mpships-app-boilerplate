from __future__ import print_function

import shlex
import sys
import os
import shutil
import subprocess

install_deps = '{{cookiecutter.install_dependencies}}'
project_shortname = '{{cookiecutter.project_shortname}}'


is_windows = sys.platform == 'win32'

if is_windows:
    python_executable = os.path.join('.venv', 'Scripts', 'python')
else:
    python_executable = os.path.join('.venv', 'bin', 'python')


def _execute_command(cmd):
    line = shlex.split(cmd, posix=not is_windows)

    print('Executing: {}'.format(cmd))

    # call instead of Popen to get realtime output
    status = subprocess.call(line, shell=is_windows)

    if status != 0:
        print('post_gen_project command failed: {}'.format(cmd),
              file=sys.stderr)
        sys.exit(status)

    return status


if install_deps != 'True':
    print('`install_dependencies` is false!!', file=sys.stderr)
    print('Please create a venv in your project root'
          ' and install the dependencies in requirements.txt',
          file=sys.stderr)
    sys.exit(0)

# Create a virtual env
venv = '{} -m venv .venv'.format(sys.executable)

# noinspection PyBroadException
try:
    _execute_command(venv)
except BaseException:
    print(
        '''
        venv creation failed.
        Make sure you have installed virtualenv on Python 2.
        ''',
        file=sys.stderr
    )
    raise

print('\n\nInstalling dependencies\n', file=sys.stderr)

# Install Python requirements.
_execute_command(
    r'{} -m pip install .'.format(python_executable)
)

activate_cmd = '.venv\\Scripts\\activate' if is_windows else 'source .venv/bin/activate'

print('\n[DONE] {} ready!\n'.format(project_shortname))
print("To get started, run the following commands:")
print(f"  cd {project_shortname}")
print(f"  {activate_cmd}")

sys.exit(0)
