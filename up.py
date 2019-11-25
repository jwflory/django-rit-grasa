#!/usr/bin/env python3


import argparse
import subprocess
import shlex

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("--setup", help="initial setup", action="store_true")
group.add_argument("--start", help="start the app", action="store_true")
group.add_argument("--stop", help="stop the app", action="store_true")
group.add_argument(
    "--restart", help="Restart the container without rebuilding", action="store_true"
)
parser.add_argument("-p", "--port", help="port to run the app on.", required=False)
args = parser.parse_args()

containerName = "grasa_event_locator"
imageName = "gel"


def cmd_run(command):
    """Executes command in via subprocess on the server it is run.
    Returns a 3-way tuptle with exit code, stdout and stderr"""

    # Escape special chars
    command = shlex.quote(command)
    command = shlex.split(command)
    # maybe try catch here...
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    stdout, stderr = process.communicate()
    stdout = stdout.decode().strip()
    stderr = stderr.decode().strip()
    status = process.returncode

    return status, stdout, stderr


def checkResults(results):
    if results[0] != 0:
        print("ran into an error.  Please check the docker logs for details")
        print(results[2])
        exit(1)


def checkPort():
    if not args.port:
        print(
            "please specify the local port to run the container on using the -p/--port flag."
        )
        exit(1)
    else:
        return True


def setup():
    print("building container:")
    results = cmd_run("docker build -t {} .".format(imageName))
    checkResults(results)

    print("Migrating Database:")
    results = cmd_run(
        'sudo docker run --rm -it --entrypoint "./manage.py" {} "migrate"'.format(
            imageName
        )
    )
    checkResults(results)

    print("Successfully build the container.")


def start(port_number):
    print("starting...")
    command = "docker run --rm --name {name} -d -p {port}:8000 {uuid}".format(
        name=containerName, port=port_number, uuid=imageName
    )
    results = cmd_run(command)
    checkResults(results)

    cmd_run("yes | docker exec -i {} ./manage.py rebuild_index".format(containerName))

    results = cmd_run("docker ps")
    checkResults(results)
    if containerName in results[1]:
        print("Sucessfully started the container.")
    else:
        print("Could not start the container.  Please investigate.")


def stop():
    print("Stopping...")
    results = cmd_run("docker stop {}".format(containerName))
    checkResults(results)

    results = cmd_run("docker ps")
    checkResults(results)
    if containerName not in results[1]:
        print("Sucessfully stopped the container.")
    else:
        print("Could not stop the container.  Please investigate.")


def restart():
    stop()
    start(args.port)


if args.setup:
    setup()
elif args.start and checkPort():
    start(args.port)
elif args.stop:
    stop()
elif args.restart and checkPort():
    restart()
