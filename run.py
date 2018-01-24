import time, shlex, subprocess, random
command = ['docker','exec', '75d8783920da0f497a65209fdca3c939b69c30ebeb60bdebc2b2e27bed4416cd'] + ['python3', 'prime.py', '{"from":"10", "to": "3000", "result_server":"http://localhost:8081/"}'] + ["10"]
output = subprocess.check_output(command)
print(output)