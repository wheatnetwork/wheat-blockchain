import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("WHEAT_ROOT", "~/.wheat/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("WHEAT_KEYS_ROOT", "~/.wheat_keys"))).resolve()
