import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.test_file import greet


if __name__ == "__main__":
    print(greet('Wolrd'))
