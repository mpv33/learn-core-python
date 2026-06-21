"""02 — Using a Local Module"""

import sys
from pathlib import Path

# Add demo_package parent to path so we can import it
sys.path.insert(0, str(Path(__file__).parent))

from demo_package import greet, add, APP_VERSION

print(greet("Learner"))
print(f"2 + 3 = {add(2, 3)}")
print(f"Version: {APP_VERSION}")

# Direct module import
from demo_package import mymodule
print(f"Direct: {mymodule.greet('Direct import')}")
