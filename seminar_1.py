import subprocess
import os

def check_command(command, text):
    process_exec_command = subprocess.run(command, encoding="UTF-8", stdout=subprocess.PIPE)
    out_code = process_exec_command.returncode
    out_exec_command = process_exec_command.stdout

    if text in out_exec_command and out_code == 0:
        print("Success")
    else:
        print("Fail")

environ = os.environ
env = environ.get('HOME')

check_command('pwd', env)
check_command('ls', "pim")