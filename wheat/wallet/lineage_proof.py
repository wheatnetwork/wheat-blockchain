from dataclasses import dataclass
from typing import Optional

from wheat.types.blockchain_format.sized_bytes import bytes32
from wheat.util.ints import uint64
from wheat.util.streamable import Streamable, streamable


@dataclass(frozen=True)
@streamable
class LineageProof(Streamable):
    parent_name: bytes32
    inner_puzzle_hash: Optional[bytes32]
    amount: uint64
