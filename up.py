#!/usr/bin/env python3


import argparse
import subprocess
import shlex

parser = argparse.ArgumentParser()
#group = parser.add_mutually_exclusive_group()
parser.add_argument("--setup", help="initial setup", action='store_true')
parser.add_argument("--start", help="start the app", action='store_true')
parser.add_argument("--stop", help="stop the app", action='store_true')
#parser.add_argument("-p", "--port", help="port to run the app on.")
args = parser.parse_args()

containerName = 'grasa_event_locator'
imageName = 'gel'

def cmd_run(command):
    """Executes command in via subprocess on the server it is run.
    Returns a 3-way tuptle with exit code, stdout and stderr"""

    # Escape special chars
    command = shlex.quote(command)
    command = shlex.split(command)
    #maybe try catch here...
    process = subprocess.Popen(command, stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    stdout, stderr = process.communicate()
    stdout = stdout.decode().strip()
    stderr = stderr.decode().strip()
    status = process.returncode

    return status, stdout, stderr

def setup():
    print('building container:')
    results = cmd_run('docker build -t {} .'.format(imageName))
    print(results[2])
    results = cmd_run('sudo docker run -it --entrypoint "./manage.py" {} "migrate"'.format(imageName))
    print(results[2])

def start():
    command = "docker run --name {name} -d -p {port}:8000 {uuid}".format(name=containerName, port='8000', uuid = imageName)
    print(command)
    results = cmd_run(command)
    print(results[2])
    results = cmd_run('yes | docker exec -i {} ./manage.py rebuild_index'.format(containerName))
    print(results[2])

def stop():
    results = cmd_run("docker stop grasa_event_locator")
    print(results[2])

if args.setup:
    setup()
elif args.start:
    start()
elif args.stop:
    stop()
