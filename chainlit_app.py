import os
from subprocess import Popen

if __name__ == "__main__":
    os.system("pip install -r requirements.txt")
    Popen(["chainlit", "run", "your_chainlit_file.py", "--port", "8000", "--host", "0.0.0.0"])
