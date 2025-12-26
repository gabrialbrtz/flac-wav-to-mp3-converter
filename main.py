import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src"))

if __name__ == "__main__":
    from src import gui
    gui.root.mainloop()