import os 
from pathlib import Path
import sys
print(os.getcwd())
sys.path.append(Path(os.getcwd())/"uebungen")
from uebungen import *

