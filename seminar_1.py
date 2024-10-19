import subprocess
import os

def check_command(command, text):
    process_exec_command = subprocess.run(command, stdout=subprocess.PIPE)
    out_code = process_exec_command.returncode
    out_exec_command = process_exec_command.stdout
    command_find_text = "grep " + text
    process_find_text_in_out_exec_command = subprocess.run(command_find_text, shell=True, input=out_exec_command)
    if process_find_text_in_out_exec_command.returncode == 0 and out_code == 0:
        print("Success")
    else:
        print("Fail")

environ = os.environ
env = environ.get('HOME')

check_command('pwd', env)
check_command('ls', "pim")