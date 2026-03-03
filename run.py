import sys
import os

# Add src to the path so we can import directly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from main import main

if __name__ == "__main__":
    main()
