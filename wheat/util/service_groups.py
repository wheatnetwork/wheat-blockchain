from __future__ import annotations

from typing import Generator, Iterable, KeysView

SERVICES_FOR_GROUP = {
    "all": [
        "wheat_harvester",
        "wheat_timelord_launcher",
        "wheat_timelord",
        "wheat_farmer",
        "wheat_full_node",
        "wheat_wallet",
        "wheat_data_layer",
        "wheat_data_layer_http",
    ],
    # TODO: should this be `data_layer`?
    "data": ["wheat_wallet", "wheat_data_layer"],
    "data_layer_http": ["wheat_data_layer_http"],
    "node": ["wheat_full_node"],
    "harvester": ["wheat_harvester"],
    "farmer": ["wheat_harvester", "wheat_farmer", "wheat_full_node", "wheat_wallet"],
    "farmer-no-wallet": ["wheat_harvester", "wheat_farmer", "wheat_full_node"],
    "farmer-only": ["wheat_farmer"],
    "timelord": ["wheat_timelord_launcher", "wheat_timelord", "wheat_full_node"],
    "timelord-only": ["wheat_timelord"],
    "timelord-launcher-only": ["wheat_timelord_launcher"],
    "wallet": ["wheat_wallet"],
    "introducer": ["wheat_introducer"],
    "simulator": ["wheat_full_node_simulator"],
    "crawler": ["wheat_crawler"],
    "seeder": ["wheat_crawler", "wheat_seeder"],
    "seeder-only": ["wheat_seeder"],
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups: Iterable[str]) -> Generator[str, None, None]:
    for group in groups:
        yield from SERVICES_FOR_GROUP[group]


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
