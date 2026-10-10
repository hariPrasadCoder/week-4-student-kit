"""Create isolated lesson environments and register Jupyter kernels."""
import argparse
from pathlib import Path
import subprocess
import sys
import venv

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ["01-langfuse","02-litellm","03-evals"]
p = argparse.ArgumentParser(description=__doc__)
p.add_argument("lesson", nargs="?", choices=LESSONS)
a = p.parse_args()
if sys.version_info[:2] != (3, 12):
    raise SystemExit("Run setup with Python 3.12.")
for lesson in [a.lesson] if a.lesson else LESSONS:
    folder = ROOT / lesson
    env = folder / ".venv"
    venv.EnvBuilder(with_pip=True).create(env)
    python = env / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")
    subprocess.run([str(python), "-m", "pip", "install", "-r", str(folder / "requirements.txt")], check=True)
    subprocess.run([str(python), "-m", "pip", "check"], check=True)
    subprocess.run([str(python), "-m", "ipykernel", "install", "--user", "--name", "week4-" + lesson[3:], "--display-name", "Python (Week 4 " + lesson[3:] + ")"], check=True)
    print(f'Launch: cd "{folder}" then "{python}" -m jupyterlab', flush=True)
