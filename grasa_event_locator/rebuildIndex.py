import subprocess
import shlex
import os


def rebuildWhooshIndex():
    PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
    command = 'cd {}; yes | python3 manage.py rebuild_index'.format(PROJECT_PATH)
    command = shlex.quote(command)
    command = shlex.split(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    stdout, stderr = process.communicate()
    stdout = stdout.decode().strip()
    stderr = stderr.decode().strip()
    status = process.returncode



    if status == 0:
            print(stdout)
            print('\nindex rebuilt')
    else:
            print(stderr)
            print('\nCould not rebuild index')