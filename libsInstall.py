import sys
import subprocess

subprocess.check_call([sys.executable, "-m","pip","install","simple_chalk"])
subprocess.check_call([sys.executable, "-m","pip","install","pyperclip"])

reqs = subprocess.check_output([sys.executable, "-m","pip","freeze"])
installed_packages = [r.decode().split("==")[0] for r in reqs.split()]
print("The following packages:")
print(installed_packages)
print("\bHave been installed")