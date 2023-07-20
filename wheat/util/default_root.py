from __future__ import annotations

import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("WHEAT_ROOT", "~/.wheat/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("WHEAT_KEYS_ROOT", "~/.wheat_keys"))).resolve()

SIMULATOR_ROOT_PATH = Path(os.path.expanduser(os.getenv("WHEAT_SIMULATOR_ROOT", "~/.wheat/simulator"))).resolve()
