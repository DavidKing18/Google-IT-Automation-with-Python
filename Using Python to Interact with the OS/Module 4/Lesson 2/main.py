import subprocess
import os

# subprocess.run(["dir"])

# subprocess.run(["sleep", "2"])

result = subprocess.run(['host', '8.8.8.8'], capture_output=True)
print(result.returncode)

print(result.stdout)

print(result.stdout.decode().split())

result = subprocess.run(["rm", " does_not_exist"], capture_output=True)
print(result.returncode)

print(result.stdout)

print(result.stderr)




my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)
  