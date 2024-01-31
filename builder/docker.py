from pathlib import Path
import subprocess
import time, os

def run_via_docker(compose_file: Path, log_path: Path):
    bash_command = f"docker-compose -f {compose_file} up -d",
    with open(log_path / "compose.log", "w+") as f:
        subprocess.run(
            bash_command,
            shell=True,
            stdout=f,
            stderr=f
        )
    while not f.closed:
        time.sleep(0.1)
    print(f"{os.linesep} COMMAND {bash_command} LOG OUTPUT:")
    with open(log_path / "compose.log", "r") as output:
        for line in output:
            print(line)

def stop_via_docker(compose_file: Path, log_path: Path):
    bash_command = f"docker-compose -f {compose_file} down -v",
    with open(log_path / "compose.log", "w+") as f:
        subprocess.run(
            bash_command,
            shell=True,
            stdout=f,
            stderr=f
        )
    while not f.closed:
        time.sleep(0.1)
    print(f"{os.linesep} COMMAND {bash_command} LOG OUTPUT:")
    with open(log_path / "compose.log", "r") as output:
        for line in output:
            print(line)