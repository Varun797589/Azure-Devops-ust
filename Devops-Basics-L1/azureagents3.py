import subprocess

def is_runner_alive():
    result = subprocess.run(
        ["ps", "-ef"],
        stdout=subprocess.PIPE,
        text=True
    )
    return "runsvc.sh" in result.stdout

if is_runner_alive():
    print("Runner is alive")
else:
    print("Runner is DOWN")
