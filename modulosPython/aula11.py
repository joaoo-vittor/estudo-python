"""
Aula 11

Subprocess - Executando programas e comandos externos

"""
import subprocess

# ping 127.0.0.1 -c 4

proc = subprocess.run(
    ['ping', '127.0.0.1', '-c', '4'],
    capture_output=True,
    text=True
)

print(proc.stdout)
