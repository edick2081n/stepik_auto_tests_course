import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
file_path = os.path.join(BASE_DIR, 'lesson2_1_step5.py')
print(os.path.abspath(__file__))