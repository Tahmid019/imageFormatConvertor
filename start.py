import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "backend"))
sys.path.insert(0, str(Path(__file__).parent / "frontend"))

from frontend.app import main

if __name__ == "__main__":
    main()