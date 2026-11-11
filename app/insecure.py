import subprocess


def run_user_command(user_input):
    # Injection: whatever the user types goes straight to a shell
    subprocess.run(user_input, shell=True)
