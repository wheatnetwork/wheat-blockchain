from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from wheat.consensus.cost_calculator import NPCResult
from wheat.types.blockchain_format.sized_bytes import bytes32
from wheat.types.mempool_item import BundleCoinSpend
from wheat.types.spend_bundle import SpendBundle
from wheat.util.ints import uint32


@dataclass(frozen=True)
class InternalMempoolItem:
    spend_bundle: SpendBundle
    npc_result: NPCResult
    height_added_to_mempool: uint32
    # Map of coin ID to coin spend data between the bundle and its NPCResult
    bundle_coin_spends: Dict[bytes32, BundleCoinSpend]
